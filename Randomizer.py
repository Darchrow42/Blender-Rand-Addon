import bpy
import random


bpy.types.WindowManager.scale_min= bpy.props.FloatProperty(name="min",
                                    description="Minimum scaling applied",
                                    default=1.0,
                                    subtype="NONE")
                                    
                                    
bpy.types.WindowManager.scale_max= bpy.props.FloatProperty(name="max",
                                    description="Maximum scaling applied",
                                    default=1.0,
                                    subtype="NONE")
                                    
bpy.types.WindowManager.rotation_min= bpy.props.FloatProperty(name="min",
                                    description="Minimum rotation applied",
                                    min=0,
                                    soft_min=0,
                                    max=1,
                                    soft_max=1,
                                    default=0.0,
                                    subtype="NONE")
                                    
bpy.types.WindowManager.rotation_max= bpy.props.FloatProperty(name="max",
                                    description="Minimum rotation applied",
                                    min=0,
                                    soft_min=0,
                                    max=1,
                                    soft_max=1,
                                    default=0.0,
                                    subtype="NONE")
                                    
                                    
                                    

class RandomizeScale(bpy.types.Operator):
    bl_idname = "object.rndscale"
    bl_label = "Randomize Scale In Range"
    bl_description = "Randomly scale all selected objects within the range"


    def execute(self, context):
        GlobalRandom = 1.0
        for obj in bpy.context.selected_objects:
            GlobalRandom = random.uniform(bpy.context.window_manager.scale_min,bpy.context.window_manager.scale_max)
            obj.scale.x*=GlobalRandom
            obj.scale.y*=GlobalRandom
            obj.scale.z*=GlobalRandom
            obj.rotation_euler[2]+=1
            
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
        col.prop(bpy.context.window_manager, "scale_min")
        col.prop(bpy.context.window_manager, "scale_max")
        


        col = split.column(align=True)
        col.label(text="Rotation Random Range:")
        col.prop(bpy.context.window_manager, "rotation_min")
        col.prop(bpy.context.window_manager, "rotation_max")
        
        
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