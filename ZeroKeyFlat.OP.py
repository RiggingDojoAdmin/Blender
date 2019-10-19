import bpy


def main(context):
    for ob in context.scene.objects:
        print(ob.name)
        print ("working")


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "anim.simple_operator"
    bl_label = "Flat Zero Key"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)

        context = bpy.context
        areatype = context.area.type
        #bpy.context.area.type = 'GRAPH_EDITOR' 

        if bpy.ops.graph.keyframe_insert.poll() != False :


            bpy.ops.graph.select_all(action='DESELECT')

            bpy.ops.graph.keyframe_insert(type='ALL')
            bpy.ops.graph.select_all(action='DESELECT')
            bpy.ops.graph.select_column(mode='CFRA')


            bpy.context.space_data.cursor_position_y = 0
            bpy.ops.graph.snap(type='VALUE')
            bpy.ops.graph.snap(type='HORIZONTAL')
            print ("keys set to zero")


        return {'FINISHED'}


def register():
    bpy.utils.register_class(SimpleOperator)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.anim.simple_operator()
