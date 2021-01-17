import bpy
import random


class Randomizer(bpy.types.PropertyGroup):
    min: bpy.props.FloatProperty(name="min",
                                        description="Some elaborate description",
                                        subtype="NONE")
    max: bpy.props.FloatProperty(name="max",
                                        description="Some elaborate description",
                                        subtype="NONE")


class RandomizeScale(bpy.types.Operator):
    bl_idname = "object.rndscale"
    bl_label = "Randomize Scale In Range"


    def execute(self, context):
        SRandom = random.uniform(0.8,1.2)
        for obj in bpy.context.selected_objects:
            obj.scale.x*=SRandom
            SRandom = random.uniform(0.8,1.2)
        
        return {'FINISHED'}









class RAND_Panel(bpy.types.Panel):
    bl_label = "WorthGroup Tools Panel"
    bl_category = "WorthGroup Tools Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        worth_group_tools = context.scene.worth_group_tools
        split = layout.split()
        col = split.column(align=True)
        col.label(text="Column Two:")
        col.prop(worth_group_tools, "min")
        col.prop(worth_group_tools, "max")
        
        layout.label(text="Big Button:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.rndscale")


classes = (Randomizer,
           RAND_Panel,
           RandomizeScale)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
    bpy.types.Scene.worth_group_tools = bpy.props.PointerProperty(type=Randomizer)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
 
    del bpy.types.Scene.worth_group_tools



if __name__ == "__main__":
    register()