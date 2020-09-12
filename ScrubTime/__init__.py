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
	"name": "Scrub Time",
	"author": "Brad Clark Rigging Dojo",
	"version": (1, 1),
	"blender": (2, 80, 0),
	"location": "",
	"description": "Scrub timeline from viewport like Maya K key scrub assigning it to the J key in Blender",
	"warning": "",
	"wiki_url": "https://vimeo.com/452683870",
	"category": "Animation",
}


import bpy
from bpy.props import IntProperty, FloatProperty


class ScrubTime_MO(bpy.types.Operator):

	bl_idname = "scene.scrub_time"
	bl_label = "Scrub Time"

	first_mouse_x: IntProperty()
	first_value: FloatProperty()

	def modal(self, context, event):
		if event.type == 'MOUSEMOVE':
			scn = bpy.context.scene
			delta = self.first_mouse_x - event.mouse_x
			scn.frame_current = sorted([scn.frame_start,(self.first_value - delta * 1), scn.frame_end])[1]

		elif event.type == 'LEFTMOUSE':
			return {'FINISHED'}

		elif event.type in {'RIGHTMOUSE', 'ESC'}:
			context.scene.frame_current = self.first_value
			return {'CANCELLED'}

		return {'RUNNING_MODAL'}

	def invoke(self, context, event):
		if context.scene:
			self.first_mouse_x = event.mouse_x
			self.first_value = context.scene.frame_current

			context.window_manager.modal_handler_add(self)
			return {'RUNNING_MODAL'}
		else:
			self.report({'WARNING'}, "Zero Frame Range, could not finish")
			return {'CANCELLED'}




addon_keymaps = []
	
	
	
def register():
	bpy.utils.register_class(ScrubTime_MO)
	
# Keymap reg
	wm = bpy.context.window_manager
	kc = wm.keyconfigs.addon
	if kc:
		km = kc.keymaps.new(name='Window', space_type='EMPTY' )
		kmi = km.keymap_items.new("scene.scrub_time", type='J', value='PRESS') # activate scrub time
		addon_keymaps.append((km, kmi))



def unregister():

	# Keymap unreg
	for km, kmi in addon_keymaps:
		km.keymap_items.remove(kmi)
	addon_keymaps.clear()

	bpy.utils.unregister_class(ScrubTime_MO)


if __name__ == "__main__":
	register()
	

	# test call
	#bpy.ops.scene.scrub_time('INVOKE_DEFAULT')
	
