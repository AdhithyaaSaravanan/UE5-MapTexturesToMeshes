import unreal as ue
import os

EAL = ue.EditorAssetLibrary()
asset_tools = ue.AssetToolsHelpers.get_asset_tools()
asset_import_data = ue.AutomatedAssetImportData()

ingame_assets_path = '/Game/tool_output/Assets/'
ingame_textures_path = '/Game/tool_output/Textures/'
ingame_materials_path = '/Game/tool_output/Materials/'


def get_assets(folder_path):
    assets_list = []
    for asset in os.listdir(folder_path):
        assets_list.append(os.path.join(folder_path, asset).replace("\\", "/"))

    return assets_list


def import_assets():
    """
    Import assets into project.
    """
    # list of files to import
    common_path = r'C:\Your\Tool\Input'
    common_path = common_path.replace("\\", "/")

    # set assetImportData attributes
    asset_import_data.replace_existing = True

    # Import assets
    fbx_list = get_assets(os.path.join(common_path, "Assets").replace("\\", "/"))
    asset_import_data.filenames = fbx_list
    asset_import_data.destination_path = ingame_assets_path
    asset_tools.import_assets_automated(asset_import_data)

    textures_paths = get_assets(os.path.join(common_path, 'Textures').replace("\\", "/"))
    for textures_path in textures_paths:
        textures_list = get_assets(textures_path)
        asset_import_data.filenames = textures_list
        asset_name = os.path.basename(textures_path)

        # Import textures
        textures_ingame_destination_path = ingame_textures_path + asset_name
        asset_import_data.destination_path = textures_ingame_destination_path
        asset_tools.import_assets_automated(asset_import_data)

        # Create a material
        material_name = 'm_' + asset_name
        material_package_path = ingame_materials_path
        material_factory = ue.MaterialFactoryNew()
        material = asset_tools.create_asset(material_name, material_package_path,
                                            ue.Material, material_factory)

        for texture_path in EAL.list_assets(textures_ingame_destination_path):
            texture_path = texture_path.split('.')[0]
            texture = EAL.load_asset(texture_path)

            # Create a Texture Sample node
            texture_sample = ue.MaterialEditingLibrary.create_material_expression(material,
                                                                        ue.MaterialExpressionTextureSample)

            # Set the base color texture in the Texture Sample node
            texture_sample.set_editor_property("texture", texture)

            # Connect the Texture Sample node to the base color input
            material_properties = {
                "albedo": ue.MaterialProperty.MP_BASE_COLOR,
                "normal": ue.MaterialProperty.MP_NORMAL,
                "occlusion": ue.MaterialProperty.MP_AMBIENT_OCCLUSION,
                "spec": ue.MaterialProperty.MP_SPECULAR,
                "rough": ue.MaterialProperty.MP_ROUGHNESS
            }

            # do split(test_rock_)[1] later, did it.
            material_property = texture.get_name().split('_')[-2]
            try:
                ue_material_property_object = material_properties[material_property]
            except:
                continue

            ue.MaterialEditingLibrary.connect_material_property(texture_sample, 'RGB', ue_material_property_object)

        fbx_path = ingame_assets_path + 'sm_' + asset_name
        fbx_object = EAL.load_asset(fbx_path)

        for static_material in fbx_object.static_materials:
            # get the index of the current static material for later
            material_index = fbx_object.static_materials.index(static_material)
            fbx_object.set_material(material_index, material)


import_assets()
