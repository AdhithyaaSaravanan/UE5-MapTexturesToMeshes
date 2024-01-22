# UE5 Tool for materials workflow

## Tool Summary

This tool is designed to streamline the process of texture mapping and 
material creation for a personal project in Unreal Engine 5. 
It automates the task of associating texture maps with meshes, 
creating and applying materials to the corresponding meshes. 
It works in correlation with the Houdini batch export tool.

## Note

This script was solely written for specific uses within a personal project.
The aim was to produce a quick script to automate a repetitive task. 
It is not ready to be integrated into other people's workflows, unless 
further changes are made in the code. In the future, I will add error checking
and testing to make it more reliable, and also potentially a UI to make it 
artist friendly. But the main logic is there :)

## Input

A sample input folder is provided in the repo to demonstrate an example. 
An underscore is assumed in the file names when string concatenation 
is specified in the below examples.

### Template Input Folder Tree
````
├───Assets
│       "sm" + asset_name + verion
└───Textures
    ├───asset_name + verion
    │       "t" + asset_name + albedo + verion
    │       "t" + asset_name + normal + verion
    │       "t" + asset_name + occlusion + verion
    │       "t" + asset_name + rough + verion
    │       "t" + asset_name + spec + verion
````

### Example Input Folder Tree
````
├───Assets
│       sm_test_rock_v001.fbx
└───Textures
    ├───test_rock_v001
    │       t_test_rock_albedo_v001.tga
    │       t_test_rock_normal_v001.tga
    │       t_test_rock_occlusion_v001.tga
    │       t_test_rock_rough_v001.tga
    │       t_test_rock_spec_v001.tga
    │       t_test_rock_v001.exr
    │       t_test_rock_v001.tga
````

## Output

The script generates 3 folders with the required files in the 
specified output directory inside the unreal project content browser.
The assets inside the "Assets" folder already have materials applied 
procedurally, so they're ready to be dragged and dropped onto the map.

### Example Folder Tree

````
├───Assets
│       sm_test_rock_v001.uasset
├───Materials
│       m_test_rock_v001.uasset
└───Textures
    ├───test_rock_v001
    │       t_test_rock_albedo_v001.uasset
    │       t_test_rock_normal_v001.uasset
    │       t_test_rock_occlusion_v001.uasset
    │       t_test_rock_rough_v001.uasset
    │       t_test_rock_spec_v001.uasset
    │       t_test_rock_v001.uasset
````