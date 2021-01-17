import bpy
import random


bpy.types.WindowManager.min= bpy.props.FloatProperty(name="min",
                                    description="Minimum scaling applied",
                                    subtype="NONE")
bpy.types.WindowManager.max= bpy.props.FloatProperty(name="max",
                                    description="Maximum scaling applied",
                                    subtype="NONE")


class RandomizeScale(bpy.types.Operator):
    bl_idname = "object.rndscale"
    bl_label = "Randomize Scale In Range"
    bl_description = "Randomly scale all selected objects within the range"


    def execute(self, context):
        GlobalRandom = 1.0
        for obj in bpy.context.selected_objects:
            GlobalRandom = random.uniform(bpy.context.window_manager.min,bpy.context.window_manager.max)
            obj.scale.x*=GlobalRandom
            obj.scale.y*=GlobalRandom
            obj.scale.z*=GlobalRandom
        return {'FINISHED'}









class RAND_Panel(bpy.types.Panel):
    bl_label = "Rand"
    bl_category = "Rand"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        split = layout.split()
        col = split.column(align=True)
        col.label(text="Scale Multiplier Range:")
        col.prop(bpy.context.window_manager, "min")
        col.prop(bpy.context.window_manager, "max")
        
        layout.label(text="Randomize:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.rndscale")


classes = (RAND_Panel,
           RandomizeScale)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        




def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
 
    del bpy.types.Scene.worth_group_tools



if __name__ == "__main__":
    register()