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
    "name": "ctrlDisplayCycle",
    "author": "Brad Clark Rigging Dojo",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "",
    "description": "Cycle display in Pose mode of bones, like MotionBuilder and Maya hotkey",
    "warning": "",
    "wiki_url": "",
    "category": "",
}

import bpy


def main(context):

    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    
                    if space.overlay.show_xray_bone == False and space.overlay.show_bones == False:
                        space.overlay.show_bones = True
                        space.overlay.show_xray_bone = True
                        
                    elif space.overlay.show_xray_bone == True:
                        space.overlay.show_bones = True
                        space.overlay.show_xray_bone = False
                        
                    elif space.overlay.show_xray_bone == False:
                          space.overlay.show_bones = False
                          space.overlay.show_xray_bone = False
                    break

class SimpleMacro(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "anim.ctrldisplayctnycle"
    bl_label = "ctrl Display Cycle"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}
    
addon_keymaps = []

def register():
    bpy.utils.register_class(SimpleMacro)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Window', space_type='EMPTY' )
        kmi = km.keymap_items.new("anim.ctrldisplayctnycle", type= 'F1', value= 'PRESS', alt= True)
        addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(SimpleMacro)
    for km,kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()    

if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.anim.ctrldisplayctnycle()
