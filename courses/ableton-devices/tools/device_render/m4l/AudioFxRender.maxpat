{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 6,
			"revision" : 0,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 100.0, 100.0, 760.0, 540.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"assistshowspatchername" : 0,
		"boxes" : [
			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 20.0, 20.0, 720.0, 80.0 ],
					"text" : "AudioFxRender — render demos by applying LOM params to an audio FX chain and freezing the track.\n\nTrack layout: [0] this device  [1+] target FX chain. Audio source: clip in slot 0.\nWorkflow: 1) drop audio source into slot 0, 2) edit spec path, 3) LOAD SPEC, 4) RENDER."
				}
			},
			{
				"box" : 				{
					"id" : "obj-3",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 20.0, 150.0, 720.0, 22.0 ],
					"text" : "load_spec /Users/zak/zacharysbrown/idm-course/build/ableton-devices/tmp/device-render/e05-warp-modes/spec.json"
				}
			},
			{
				"box" : 				{
					"id" : "obj-2",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 20.0, 120.0, 200.0, 22.0 ],
					"text" : "Spec path (edit me):"
				}
			},
			{
				"box" : 				{
					"id" : "obj-5",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 20.0, 225.0, 32.0, 32.0 ]
				}
			},
			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 70.0, 230.0, 80.0, 22.0 ],
					"text" : "render"
				}
			},
			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 20.0, 305.0, 280.0, 22.0 ],
					"text" : "render_one warp-mode-beats"
				}
			},
			{
				"box" : 				{
					"id" : "obj-10",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "" ],
					"patching_rect" : [ 20.0, 360.0, 220.0, 22.0 ],
					"saved_object_attributes" : 					{
						"filename" : "audio_fx_render.js",
						"parameter_enable" : 0
					}
,
					"text" : "js audio_fx_render.js"
				}
			},
			{
				"box" : 				{
					"id" : "obj-11",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 20.0, 420.0, 120.0, 22.0 ],
					"text" : "print fx.status"
				}
			},
			{
				"box" : 				{
					"id" : "obj-12",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 160.0, 420.0, 140.0, 22.0 ],
					"text" : "print fx.done"
				}
			},
			{
				"box" : 				{
					"id" : "obj-13",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 320.0, 420.0, 140.0, 22.0 ],
					"text" : "print fx.error"
				}
			}
		],
		"lines" : [
			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"source" : [ "obj-3", 0 ]
				}
			},
			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"source" : [ "obj-5", 0 ]
				}
			},
			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"source" : [ "obj-6", 0 ]
				}
			},
			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"source" : [ "obj-9", 0 ]
				}
			},
			{
				"patchline" : 				{
					"destination" : [ "obj-11", 0 ],
					"source" : [ "obj-10", 0 ]
				}
			},
			{
				"patchline" : 				{
					"destination" : [ "obj-12", 0 ],
					"source" : [ "obj-10", 1 ]
				}
			},
			{
				"patchline" : 				{
					"destination" : [ "obj-13", 0 ],
					"source" : [ "obj-10", 2 ]
				}
			}
		],
		"dependency_cache" : [
			{
				"name" : "audio_fx_render.js",
				"bootpath" : "~/Documents/Max 8/Library",
				"patcherrelativepath" : ".",
				"type" : "TEXT",
				"implicit" : 1
			}
		]
	}
}
