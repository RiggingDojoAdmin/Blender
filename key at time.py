import bpy

#Key Current Pose Over Time
#bclark Rigging Dojo
cop = bpy.context.copy()
cop["ao"] = bpy.context.active_object
bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')

curframe = bpy.context.scene.frame_current 
bpy.ops.pose.copy()
#set current frame to 5

bpy.context.scene.frame_set(curframe+1)
bpy.ops.pose.paste(flipped=False)
#bpy.ops.pose.propagate(mode='WHILE_HELD')

