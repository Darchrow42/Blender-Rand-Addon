import bpy
import random

bpy.types.WindowManager.min= bpy.props.FloatProperty(name="min",
                                    description="Some elaborate description",
                                    subtype="NONE")
bpy.types.WindowManager.max= bpy.props.FloatProperty(name="max",
                                    description="Some elaborate description",
                                    subtype="NONE")

class RandomizeScale(bpy.types.Operator):
    bl_idname = "object.rndscale"
    bl_label = "Randomize Scale In Range"


    def execute(self, context):
        SRandom = random.uniform(context.scene.worth_group_tools.min,context.scene.worth_group_tools.max)
        for obj in bpy.context.selected_objects:
            obj.scale.x*=SRandom
            SRandom = random.uniform(context.scene.worth_group_tools.min,context.scene.worth_group_tools.max)
        
        return {'FINISHED'}










bl_label = "WorthGroup Tools Panel"
bl_category = "WorthGroup Tools Addon"
bl_space_type = "VIEW_3D"
bl_region_type = "UI"

def draw(self, context):
    layout = self.layout
    worth_group_tools = context.scene.worth_group_tools
    split = layout.split()
    col = split.column(align=True)
    col.label(text="Range:")
    col.prop(worth_group_tools, "min")
    col.prop(worth_group_tools, "max")
    
    layout.label(text="Randomize:")
    row = layout.row()
    row.scale_y = 3.0
    row.operator("object.rndscale")


classes = (RandomizeScale)


def register():
    bpy.utils.register_class(RandomizeScale)
        




def unregister():
    bpy.utils.unregister_class(RandomizeScale)
 




if __name__ == "__main__":
    register()