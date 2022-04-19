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
    "version": (1, 1),
    "blender": (3,1,2),
    "location": "",
    "description": "Maya and Motionbuilder tool,Must have tool to work with Animation NLA layers. Sets a zero key for the control to blend back to the source motion",
    "warning": "",
    "wiki_url": "",
    "category": "Animation",
}


import bpy

obj = bpy.context.active_object         
animData = obj.animation_data
action = animData.action
cf = bpy.context.scene.frame_current
selBones = bpy.context.selected_pose_bones

##insert keyframes on the selected bones on the current frame
if animData is not None and action is not None:
    fcurves = action.fcurves
    if len(selBones) != 0: 
        for bone in selBones:
            bone_path = 'pose.bones["%s"]' % bone.name
            for curve in fcurves:
                if curve.data_path.startswith(bone_path) and not curve.data_path.endswith("scale"):
                    keyframePoints = curve.keyframe_points
                keyframePoints.insert (cf,0, options = {'NEEDED'})
    else:
        print ("no bone selected")
else:
    bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')
        
bpy.context.scene.frame_current=cf
