# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Zero Key",
    "author": "Brad Clark Rigging Dojo",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "",
    "description": "Maya and Motionbuilder toold,Must have tool to work with Animation NLA layers. Sets a zero key for the control to blend back to the sorce motion",
    "warning": "",
    "wiki_url": "",
    "category": "Animation",
}


import bpy


cf = bpy.context.scene.frame_current
ob = bpy.context.active_object
value = 0

if bpy.context.selected_pose_bones == None:
    ob.keyframe_insert(data_path="location", index=-1)
    if ob.rotation_mode == 'QUATERNION':
        ob.keyframe_insert(data_path="rotation_quaternion", index=-1)
    else: 
        ob.keyframe_insert(data_path="rotation_euler", index=-1)
        
else:
    for bone in bpy.context.selected_pose_bones:    
        bone.keyframe_insert(data_path="location", index=-1)
        if bone.rotation_mode == 'QUATERNION':
            bone.keyframe_insert(data_path="rotation_quaternion", index=-1, options={'INSERTKEY_VISUAL'})
        else: 
            bone.keyframe_insert(data_path="rotation_euler", index=-1, options={'INSERTKEY_VISUAL'})


#Find the selected object that has keys and set the keys at the current frame to a value of 0
animData = ob.animation_data
action = animData.action
fcurves = action.fcurves

for curve in fcurves:
    keyframePoints = curve.keyframe_points
    for keyframe in keyframePoints:
        if  keyframe.co[0] == cf :
            print ( keyframe.select_control_point)
            keyframe.co[1] = value
            keyframe.handle_left[1] = value
            keyframe.handle_right[1] = value
           
    
#redraw hack until a better way is learned set the current frame to itself
bpy.context.scene.frame_current = cf
