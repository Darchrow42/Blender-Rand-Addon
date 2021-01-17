bl_info = {
    "name": "Rand",
    "descreption": "An add-on that allows you to randomize the transforms of multiple objects at once. You can chose which axis is affected, and which operations are performed",
    "author": "Hosein Sabzpoosh",
    "version": (1, 0),
    "blender": (2, 91, 0),
    "location": "3D View-> Properties",   
    "category": "Object",
}





import bpy
import random


bpy.types.WindowManager.scale_min= bpy.props.FloatProperty(name="min",
                                    description="Minimum scaling applied",
                                    min=0,
                                    soft_min=0,
                                    default=0.5,
                                    subtype="NONE")
                                    
                                    
bpy.types.WindowManager.scale_max= bpy.props.FloatProperty(name="max",
                                    description="Maximum scaling applied",
                                    min=0,
                                    soft_min=0,
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
                                    
bpy.types.WindowManager.randomize_scale= bpy.props.BoolProperty(name="Randomize Scale",
                                    description="Whether scale is randomized or not",
                                    default=True,
                                    get= None,
                                    subtype="NONE")
                                    
bpy.types.WindowManager.randomize_rotation= bpy.props.BoolProperty(name="Randomize Rotation",
                                    description="Whether rotation is randomized or not",
                                    default=True,
                                    get= None,
                                    subtype="NONE")     
                                    
bpy.types.WindowManager.x_rotation= bpy.props.BoolProperty(name="X",
                                    description="rotation around x",
                                    default=True,
                                    get= None,
                                    subtype="NONE")        
                                    
bpy.types.WindowManager.y_rotation= bpy.props.BoolProperty(name="Y",
                                    description="rotation around y",
                                    default=True,
                                    get= None,
                                    subtype="NONE")

bpy.types.WindowManager.z_rotation= bpy.props.BoolProperty(name="Z",
                                    description="rotation around Z",
                                    default=True,
                                    get= None,
                                    subtype="NONE")
                                    
bpy.types.WindowManager.x_scale= bpy.props.BoolProperty(name="X",
                                    description="scaling on x",
                                    default=True,
                                    get= None,
                                    subtype="NONE")        
                                    
bpy.types.WindowManager.y_scale= bpy.props.BoolProperty(name="Y",
                                    description="scaling on y",
                                    default=True,
                                    get= None,
                                    subtype="NONE")

bpy.types.WindowManager.z_scale= bpy.props.BoolProperty(name="Z",
                                    description="scaling on Z",
                                    default=True,
                                    get= None,
                                    subtype="NONE")     
                                    
                   
                                    
                                    
                                    

class RandomizeScale(bpy.types.Operator):
    bl_idname = "object.rndscale"
    bl_label = "Randomize"
    bl_description = "Randomly scale all selected objects within the range"


    def execute(self, context):
        GlobalRandom = 1.0
        RotationRandom = 0.0
        for obj in bpy.context.selected_objects:
            GlobalRandom = random.uniform(bpy.context.window_manager.scale_min,bpy.context.window_manager.scale_max)
            RotationRandom = random.uniform(bpy.context.window_manager.rotation_min, bpy.context.window_manager.rotation_max)
            if bpy.context.window_manager.randomize_scale == 1:
                if bpy.context.window_manager.x_scale == 1:
                    obj.scale.x*=GlobalRandom
                if bpy.context.window_manager.y_scale == 1:
                    obj.scale.y*=GlobalRandom
                if bpy.context.window_manager.z_scale == 1:
                    obj.scale.z*=GlobalRandom
            if bpy.context.window_manager.randomize_rotation == 1: 
                if bpy.context.window_manager.x_rotation == 1:           
                    obj.rotation_euler[0]+= 3.1415*2*RotationRandom
                if bpy.context.window_manager.y_rotation == 1:
                    obj.rotation_euler[1]+= 3.1415*2*RotationRandom
                if bpy.context.window_manager.z_rotation == 1:
                    obj.rotation_euler[2]+= 3.1415*2*RotationRandom
            
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
        
        layout.label(text="Parameters:")
        layout = self.layout
        layout.prop(bpy.context.window_manager, "randomize_scale")
        layout.prop(bpy.context.window_manager, "randomize_rotation")
        
        layout.label(text="Rotation axis settings")
        row=layout.row()
        row.prop(bpy.context.window_manager, "x_rotation")
        row.prop(bpy.context.window_manager, "y_rotation")
        row.prop(bpy.context.window_manager, "z_rotation")
        
        layout.label(text="Scale axis settings")
        row=layout.row()
        row.prop(bpy.context.window_manager, "x_scale")
        row.prop(bpy.context.window_manager, "y_scale")
        row.prop(bpy.context.window_manager, "z_scale")


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