# 2019
# alphaBuild
# Rigging Dojo
# help@riggingdojo.com
# Blender NLA Python Script 2.80
# Frame Timeline start and end to match NLA total clips

import bpy

context = bpy.context
object = context.object
scene = context.scene
frame = scene.frame_current


frameRange = []
frameStart = []


if object.animation_data is not None:
	track = object.animation_data.nla_tracks
	if object.animation_data and object.animation_data.nla_tracks:
		for track in object.animation_data.nla_tracks:
				#set start 
			for strip in track.strips:
				frameStart.append(strip.frame_start)
				scene.frame_start = (min(frameStart))
			for strip in track.strips:
				frameRange.append(strip.frame_end)
				scene.frame_end = (max(frameRange))
				print(max(frameRange))
								

