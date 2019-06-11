import bpy
from random import uniform
import random
import math
import pprint
import os
import glob

'''
# Clear the screen

bpy.ops.object.select_all(action='TOGGLE')
bpy.ops.object.select_all(action='TOGGLE')
bpy.ops.object.delete(use_global=False)

'''


bpy.context.scene.unit_settings.system = 'METRIC'


#bpy.context.space_data.viewport_shade = 'TEXTURED'
cameraz = 0.8
cameray = 0.008
camerax = 0.012
lampz = 0.8
totalPots = 1

for folderName in range(1,10):
    # Deselect all
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_all(action='SELECT')

    # Select the object
    for i in bpy.data.objects:
        print(i)
    bpy.data.objects['Camera_M'].select_set(state=False)

    bpy.ops.object.delete()

    '''
    # adding a K|LENS

    context = bpy.context
    #bpy.ops.group.create(name="myGroup")
    # bpy.data.cameras = []
    bpy.ops.object.camera_add(view_align=True, enter_editmode=True, location=(0, 0, cameraz), rotation=( 0 , 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    camera = context.object
    bpy.data.cameras[-1].lens= 80
    camera.name = "Camera_M"
    #bpy.ops.object
    '''
    '''

    # Add all 9 cameras

    bpy.ops.object.camera_add(view_align=True, enter_editmode=True, location=(0.012, 0, cameraz), rotation=( 0 , 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    camera = context.object
    bpy.data.cameras[-1].lens= 80
    camera.name = "Camera_R"
    #bpy.data.objects[-1].name= "Camera_R"
    bpy.ops.object.camera_add(view_align=True, enter_editmode=True, location=(-0.012, 0, cameraz), rotation=( 0 , 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    camera = context.object
    bpy.data.cameras[-1].lens= 80
    camera.name = "Camera_L"
    bpy.ops.object.camera_add(view_align=True, enter_editmode=True, location=(0, 0.008, cameraz), rotation=( 0 , 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    camera = context.object
    bpy.data.cameras[-1].lens= 80
    camera.name = "Camera_T"
    bpy.ops.object.camera_add(view_align=True, enter_editmode=True, location=(0, -0.008, cameraz), rotation=( 0 , 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    camera = context.object
    bpy.data.cameras[-1].lens= 80
    camera.name = "Camera_B"
    bpy.ops.object.camera_add(view_align=True, enter_editmode=True, location=(-0.012, -0.008, cameraz), rotation=( 0 , 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    camera = context.object
    bpy.data.cameras[-1].lens= 80
    camera.name = "Camera_BL"
    bpy.ops.object.camera_add(view_align=True, enter_editmode=True, location=(0.012, -0.008, cameraz), rotation=( 0 , 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    camera = context.object
    bpy.data.cameras[-1].lens= 80
    camera.name = "Camera_BR"
    bpy.ops.object.camera_add(view_align=True, enter_editmode=True, location=(-0.012, 0.008, cameraz), rotation=( 0 , 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    camera = context.object
    bpy.data.cameras[-1].lens= 80
    camera.name = "Camera_TL"
    bpy.ops.object.camera_add(view_align=True, enter_editmode=True, location=(0.012, 0.008, cameraz), rotation=( 0 , 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    camera = context.object
    bpy.data.cameras[-1].lens= 80
    camera.name = "Camera_TR"
    '''

    # Generating the scene
    context = bpy.context

    #bpy.ops.object.lamp_add(type='POINT', view_align=False, location=(0, 0, 10), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bagroundImagesPath = r"/Users/patel/Downloads/baground images/"
    bagimages = os.listdir(bagroundImagesPath)
    print(bagimages)
    mymodels = glob.glob(r"/Users/patel/Downloads/sizecorrected/smallobjects/*/*.glb")
    print(mymodels)

    #print(0+"0")

    for i in range(totalPots):
        file_loc = random.choice(mymodels)
        bpy.ops.import_scene.gltf(filepath=file_loc , filter_glob="*.glb;*.gltf", loglevel=0, import_pack_images=True, import_shading='NORMALS')
        #print(bpy.context.active_object)
        #print(max(bpy.context.active_object.dimensions[0],bpy.context.active_object.dimensions[1],bpy.context.active_object.dimensions[2]))
        #while(max(bpy.context.active_object.dimensions[0],bpy.context.active_object.dimensions[1],bpy.context.active_object.dimensions[2])>0.5):
        #    bpy.ops.transform.resize(value=(0.5, 0.5, 0.5), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        #while(max(bpy.context.active_object.dimensions[0],bpy.context.active_object.dimensions[1],bpy.context.active_object.dimensions[2])<0.05):
        #    bpy.ops.transform.resize(value=(2, 2, 2), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        
            
        #bpy.ops.transform.resize(value=(0.1, 0.1, 0.1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)


        scale_variable = uniform(0.05, 0.1)
        bpy.ops.transform.resize(value=(scale_variable, scale_variable, scale_variable), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        #bpy.ops.transform.resize(value=(scale_variable, scale_variable, scale_variable), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        ztranslation = uniform(-0.5,-5)
        xtranslation_max = (math.tan(0.392639/2)*ztranslation)
        ytranslation_max = (math.tan(0.392639/2/(2483/1637))*ztranslation)
        bpy.ops.transform.translate(value=(uniform(-xtranslation_max, xtranslation_max), uniform(-ytranslation_max, ytranslation_max), ztranslation), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)

        #bpy.ops.transform.translate(value=(uniform(-xtranslation_max, xtranslation_max), uniform(-ytranslation_max, ytranslation_max), ztranslation), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
        #bpy.ops.transform.translate(value=(0, 0, -9.54925), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
        bpy.ops.transform.rotate(value=0.51285, orient_axis='Z', orient_type='VIEW', orient_matrix=((-1, 0, -0), (0, 1.34359e-07, -1), (-0, 1, 1.34359e-07)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False)

        bpy.ops.transform.rotate(value=uniform(-1.547014, 1.547014), orient_axis='Z', orient_type='VIEW', orient_matrix=((-1, 0, -0),(0, 0, -1), (-0, 1, 0)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.rotate(value=1.54 + uniform(-0.1,0.1), orient_axis='X', orient_type='VIEW', orient_matrix=((-1, 0, -0), (0, 0, -1), (-0, 1, 0)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.rotate(value=uniform(-1.547014, 1.547014), orient_axis='Y', orient_type='VIEW', orient_matrix=((-1, 0, -0), (0, 0, -1), (-0, 1, 0)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1)
        

    #    else:
    #        ztranslation = uniform(-1,-15.5)
    #        bpy.ops.transform.translate(value=(uniform(-1.6, 1.6), uniform(-1, 1), uniform(-5,-10.5)), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
    #        #bpy.ops.transform.translate(value=(0, 0, -9.54925), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
    #        bpy.ops.transform.rotate(value=1.54 + uniform(-0.1,0.1), axis=(-1, -0, -0), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    #        bpy.ops.transform.rotate(value=uniform(-1.547014, 1.547014), axis=(-0, -0, -1), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    #        bpy.ops.transform.rotate(value=uniform(-1.547014, 1.547014), axis=(-0, -1, -0), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.object.light_add(type='POINT', radius=uniform(1,5), location=(uniform(5,-5), uniform(5,-5), 0))

    bpy.ops.object.light_add(type='SUN', location=(uniform(2.5,2.5), uniform(2.5,-2.5), 0))
    bpy.ops.object.light_add(type='SUN', location=(uniform(2.5,2.5), uniform(2.5,-2.5), 0))

    bpy.context.scene.cursor.location = (0.0, 0.0, -30)
    bpy.ops.import_image.to_plane(files=[{"name":random.choice(bagimages), "name":random.choice(bagimages)}], directory=bagroundImagesPath)
    imageplane = context.object
    print(imageplane)
    imageplane.name = "Image"
    bpy.ops.transform.resize(value=(10, 10, 10), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.context.object.rotation_euler[0] = uniform(-0.216421,0.216421)
    bpy.context.object.rotation_euler[1] = uniform(-0.155334,0.155334)

    frameAnz= 18
    scene = bpy.context.scene
    scene.frame_start = 2
    scene.frame_end = 18

    print(bpy.context.scene.node_tree)

    directory = "/Users/patel/Downloads/data/large_displacement_small_objects/"+str(folderName)+"/"

    try:
        os.makedirs(directory)
    except FileExistsError:
        # directory already exists
        pass


    bpy.context.scene.node_tree.nodes["File Output.002"].base_path = directory
    bpy.context.scene.node_tree.nodes["File Output.001"].base_path = directory
    bpy.context.scene.node_tree.nodes["File Output"].base_path = directory

    bpy.ops.render.render(animation=True)

'''
### Reset the scene for next take

# Deselect all
bpy.ops.object.select_all(action='DESELECT')

# Select the object
bpy.data.objects['sun'].select = True

bpy.data.objects['Image'].select = True

for i in range(totalPots):
    bpy.data.objects['pot'+str(i+1)].select = True

bpy.ops.object.delete()
'''

'''
Camera Animation


frameAnz= 18
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 3



cameraPositions = [(0,0,0),(0.012,0,0),(0,0,0),(-0.012,0,0),(0,0,0),(0,0.008,0),(0,0,0),(0,-0.008,0),(0,0,0),(0.012,0.008,0),(0,0,0),(-0.012,0.008,0),(0,0,0),(0.012,-0.008,0),(0,0,0),(-0.012,-0.008,0),(0,0,0)]

print(len(cameraPositions))

for actFrame in range(1,frameAnz):
    ob = scene.objects["Camera_M"]
    ob.location.x, ob.location.y, ob.location.z = cameraPositions[actFrame-1]
    print(ob.location.x)
    ob.keyframe_insert(data_path= 'location', index= -1, frame= actFrame)
'''

'''
#bpy.ops.mesh.primitive_cone_add(radius1=0.5, radius2=0, depth=1, view_align=False, enter_editmode=False, location=(0, 0, -3.5), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

#saveCameraImagesAndDepth()

#bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')
#bpy.context.object.location[0] = 0.012
'''
