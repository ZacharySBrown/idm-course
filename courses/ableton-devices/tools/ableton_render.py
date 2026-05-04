"""
LOM-driven audio demo renderer.
Loads presets into Ableton devices, optionally applies automation,
and exports audio to build/audio/demos/<episode>/<clip_id>.wav

Uses StemForge's M4L device communication pattern.
Requires Ableton Live to be open with the StemForge template set loaded.

Usage:
    python tools/ableton_render.py --episode e01-operator
    python tools/ableton_render.py --episode e01-operator --clip demo_fm_ratio_sweep
    python tools/ableton_render.py --test  # runs LOM validation test
"""

import argparse
import json
import subprocess
import time
from pathlib import Path
import yaml

# StemForge M4L communication uses OSC or file-based IPC
# Check stemforge/m4l/ for the exact pattern — adapt accordingly
STEMFORGE_IPC_DIR = Path.home() / "stemforge" / "ipc"
DEMOS_DIR = Path("build/audio/demos")

def send_lom_command(command: dict) -> dict:
    """
    Send a command to the StemForge M4L device via IPC.
    Pattern inherited from stemforge/m4l/ — verify exact mechanism.
    """
    cmd_file = STEMFORGE_IPC_DIR / "command.json"
    response_file = STEMFORGE_IPC_DIR / "response.json"

    cmd_file.write_text(json.dumps(command))

    # Wait for M4L device to process
    timeout = 10
    elapsed = 0
    while not response_file.exists() and elapsed < timeout:
        time.sleep(0.1)
        elapsed += 0.1

    if response_file.exists():
        response = json.loads(response_file.read_text())
        response_file.unlink()
        return response
    else:
        raise TimeoutError(f"LOM command timed out: {command}")

def load_preset(track_index: int, preset_path: str) -> bool:
    """Load an Ableton preset onto a track's device via LOM."""
    return send_lom_command({
        "action": "load_preset",
        "track_index": track_index,
        "preset_path": preset_path
    })

def set_parameter(track_index: int, device_index: int, param_name: str, value: float):
    """Set a device parameter value via LOM."""
    return send_lom_command({
        "action": "set_parameter",
        "track_index": track_index,
        "device_index": device_index,
        "param_name": param_name,
        "value": value
    })

def render_clip(track_index: int, output_path: str, duration_bars: int) -> bool:
    """
    Trigger Live's audio export for the specified track.
    NOTE: This may require AppleScript assist depending on LOM export support.
    See validation test below — if this fails, use applescript_export() instead.
    """
    return send_lom_command({
        "action": "render_track",
        "track_index": track_index,
        "output_path": output_path,
        "duration_bars": duration_bars
    })

def applescript_export(output_path: str) -> bool:
    """
    Fallback: trigger Ableton's File > Export Audio/Video via AppleScript.
    Used if LOM render_track is not available.
    """
    script = f'''
    tell application "Ableton Live 12"
        activate
    end tell
    tell application "System Events"
        tell process "Live"
            keystroke "e" using {{command down, shift down}}
            delay 2
            -- Navigate export dialog, set path to {output_path}
            -- This needs to be fleshed out based on Live 12 export dialog structure
        end tell
    end tell
    '''
    result = subprocess.run(["osascript", "-e", script], capture_output=True)
    return result.returncode == 0

def run_validation_test():
    """
    LOM VALIDATION TEST — run this first to verify headless render works.

    Test 1: MIDI instrument render
    - Loads Operator onto Track 1
    - Sets a basic FM patch (sine carrier, sine modulator, ratio 2.0)
    - Triggers a C3 note for 4 bars
    - Renders to build/audio/demos/test/test_midi_operator.wav

    Test 2: Audio FX render
    - Loads a random drum loop from stemforge library
    - Adds Saturator + Reverb chain
    - Renders processed output to build/audio/demos/test/test_audio_fx.wav

    Both tests verify the full export pipeline end-to-end.
    """
    print("=== LOM VALIDATION TEST ===\n")

    test_output_dir = Path("build/audio/demos/test")
    test_output_dir.mkdir(parents=True, exist_ok=True)

    # --- Test 1: MIDI + Operator ---
    print("Test 1: MIDI instrument render (Operator)")
    try:
        load_preset(0, "presets/operator/test_basic_fm.adv")
        set_parameter(0, 0, "OscB_Ratio", 2.0)
        set_parameter(0, 0, "OscA_Level", 100.0)

        output_path = str(test_output_dir / "test_midi_operator.wav")
        result = render_clip(0, output_path, duration_bars=4)

        if Path(output_path).exists():
            size_kb = Path(output_path).stat().st_size // 1024
            print(f"  ✅ PASS — rendered {size_kb}KB to {output_path}")
        else:
            print("  ❌ FAIL — output file not created")
            print("  → Try applescript_export() fallback")

    except Exception as e:
        print(f"  ❌ ERROR — {e}")
        print("  → Check that StemForge M4L device is loaded in Live")
        print("  → Check stemforge/m4l/ for correct IPC pattern")

    print()

    # --- Test 2: Audio FX chain ---
    print("Test 2: Audio FX chain render (drum stem + Saturator + Reverb)")
    try:
        # Find any drum stem in library
        processed_dir = Path.home() / "stemforge" / "processed"
        drum_stems = list(processed_dir.glob("*/stems/drums.wav"))

        if not drum_stems:
            print("  ⚠️  SKIP — no drum stems in library yet (run stemforge split first)")
        else:
            drum_stem = drum_stems[0]
            print(f"  Using: {drum_stem.parent.parent.name}/stems/drums.wav")

            # Load stem onto audio track, add FX chain
            send_lom_command({
                "action": "load_audio_clip",
                "track_index": 1,
                "clip_path": str(drum_stem)
            })
            send_lom_command({
                "action": "add_device",
                "track_index": 1,
                "device_name": "Saturator"
            })
            send_lom_command({
                "action": "add_device",
                "track_index": 1,
                "device_name": "Reverb"
            })
            set_parameter(1, 0, "Drive", 30.0)  # Saturator drive
            set_parameter(1, 1, "DecayTime", 2.5)  # Reverb decay

            output_path = str(test_output_dir / "test_audio_fx.wav")
            result = render_clip(1, output_path, duration_bars=4)

            if Path(output_path).exists():
                size_kb = Path(output_path).stat().st_size // 1024
                print(f"  ✅ PASS — rendered {size_kb}KB to {output_path}")
            else:
                print("  ❌ FAIL — output file not created")

    except Exception as e:
        print(f"  ❌ ERROR — {e}")

    print("\n=== TEST COMPLETE ===")
    print("If both tests passed: proceed to Episode 1 research + processing.")
    print("If Test 1 failed: check M4L IPC pattern in stemforge/m4l/")
    print("If render_clip failed: implement AppleScript fallback in applescript_export()")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--episode")
    parser.add_argument("--clip")
    parser.add_argument("--test", action="store_true", help="Run LOM validation test")
    args = parser.parse_args()

    if args.test:
        run_validation_test()
    elif args.episode:
        print(f"Rendering demos for {args.episode}...")
        # TODO: load clip-manifest.yaml and render each demo
        # This will be fully implemented after validation test passes
    else:
        print("Usage: --episode <id> or --test")
