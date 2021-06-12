import bpy, random

class ColouredCube():
    def __init__(self, x, y, z, cubesize, colour):
        bpy.ops.mesh.primitive_cube_add(size=cubesize, enter_editmode=False, location=(x, y, z))
        print("Number of objects:", len(bpy.data.objects))
        
        self.colours = ["Red", "Green", "Blue", "Black", "White", "Red_T", "Green_T", "Blue_T", "Black_T", "White_T"]
        self.colour_map = {"Red":(1,0,0,1),"Green":(0,1,0,1),"Blue":(0,0,1,1), "Black": (0,0,0,1), "White": (1,1,1,1),\
                           "Red_T":(1,0,0,0.5),"Green_T":(0,1,0,0.5),"Blue_T":(0,0,1,0.5), "Black_T": (0,0,0,0.3), "White_T": (1,1,1,0.5)}
        
        self.material = bpy.data.materials.new("R"+"_"+str(x)+"_"+str(y)+"_"+str(z))
        self.material.diffuse_color = self.colour_map[colour]

        self.cube = bpy.data.objects[-1]
        self.cube.data.materials.append(self.material)
    
    def set_colour(self, colour):
        self.material.diffuse_color = self.colour_map[colour]
    
    def set_location(self, x, y, z):
        self.cube.location = (x, y, z)
    
def clear_all_objects():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)


def create_2D_square(height):
    square_list = []
    for x in range(0, height):
        row = []
        for y in range(0, height):
            temp = ColouredCube(x,y,0,0.5,"Black_T")
            row.append(temp)
        square_list.append(row)
    return square_list

clear_all_objects()
height = 10
cubes = create_2D_square(height)

# Task 1
# Write a function to colour perimeter of the 2D square Red
def paint_perimeter(cubes, ori_x, ori_y, height, colour):
    pass

#Task 1
paint_perimeter(cubes, 0, 0, height, "Red")

# Task 2
# Write a recursive function to colour each pareimeter inwards starting 
# with Red, Green and Black and then repeat the order till center of the big sqaure
def onion(cubes, ori_x, ori_y, height, colour_index, colours):
    pass

onion(cubes, 0, 0, height, 0, ["Red","Green","Black"])

# Task 3
# Write a function to color all the cubes with Red and Blue such a way that no adjacent colour is the same
def checkered(cubes, ori_x, ori_y, height):
    pass
checkered(cubes, 0, 0, height)

# Task 4
# read the pattern file displays it in the big square, take note of the orientation
def display_pattern(cubes, patterns_file):
    pass          

display_pattern(cubes, "D:\\1-School\\H2Computing\\1-RV tutorials\\02 Practicals\\T6 lab10 - Blender Scripting\\heart_pattern.txt")

# Task 5 - animation (given as reference)   
def change_colour(cubes, colours):
    bpy.context.scene.frame_end = 200
    frame_num = 0 
    #bpy.context.scene.frame_set(frame_num)

    for x in range(0, len(cubes)):
        for y in range(0, len(cubes)):
            cubes[x][y].set_colour(colours[random.randint(0,2)])
            cubes[x][y].material.keyframe_insert("diffuse_color",frame=frame_num)
            #cubes[x][y][z][0].keyframe_insert(data_path = "location", index = -1)
            
    frame_num += 20 

    for phase in [1,2,3,4,5,6,7,8,9,10]:
        bpy.context.scene.frame_set(frame_num)    
        print(frame_num)
        for x in range(0, len(cubes)):
            for y in range(0, len(cubes)):
                # Assign it to object
                cubes[x][y].set_colour(colours[random.randint(0,2)])
                cubes[x][y].material.keyframe_insert("diffuse_color",frame=frame_num)
        frame_num += 20

change_colour(cubes, ["Red", "Green", "Blue", "Black", "White"])

# Task 6 - animation rotation
def change_direction(cubes, patterns_file):
    pass

#change_direction(cubes, "D:\\1-School\\H2Computing\\1-RV tutorials\\02 Practicals\\T6 lab10 - Blender Scripting\\heart_pattern.txt")
