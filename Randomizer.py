import bpy


class WorthGroupToolsSettings(bpy.types.PropertyGroup):
    ass: bpy.props.FloatProperty(name="ass",
                                        description="Some elaborate description",
                                        subtype="NONE")
    max: bpy.props.FloatProperty(name="max",
                                        description="Some elaborate description",
                                        subtype="NONE")


class WORTHGROUPTOOLS_PT_panel(bpy.types.Panel):
    bl_label = "WorthGroup Tools Panel"
    bl_category = "WorthGroup Tools Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        row = layout.row()

        worth_group_tools = context.scene.worth_group_tools
        row.prop(worth_group_tools, "ass")
        row.prop(worth_group_tools, "max")
        


classes = (WorthGroupToolsSettings,
           WORTHGROUPTOOLS_PT_panel)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.worth_group_tools = bpy.props.PointerProperty(type=WorthGroupToolsSettings)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.worth_group_tools


if __name__ == "__main__":
    register()