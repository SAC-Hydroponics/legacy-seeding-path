#!/usr/bin/env python
"""Seeding Path Farmware"""
#Import libraries
from farmware_tools import device, get_config_value, app, #sacFarmBot

'''
    Perhaps, the arm should move to a safe 'beginning' position,
    defined by the limit switches. It would also need to TRY to
    understand if it is in a precarious place and if movement in
    any direction will harm plants, the machine, or whatever.
    Perhaps, it could attempt to 'see' if it is in a precarious
    place by using the camera. Maybe little movements in each
    direction to start. Snap pic, attempt to find its location.
    It will also be GREAT practice to have the machine move to
    the safe location at the end of each program like you did
    in this one. We could use the limit switches to accomplish
    our safe position by going at slow speed until it's activated
    on all sides and then we have our, starting position = safe position.
'''

start_arm_x = device.get_current_position('x')
start_arm_y = device.get_current_position('y')
start_arm_z = device.get_current_position('z')

safeZ = -200
''' values for opencv
pos_x = 1013
pos_y = 24
pos_z = -400
'''

legacy = get_config_value('Seeding Path', 'Legacy Seeder')#User inputs 0 for false and 1 for true.
# Load inputs from Farmware page widget specified in manifest file
pos_x = get_config_value('Seeding Path', 'start_x')#Starting X position of Pathway
pos_y = get_config_value('Seeding Path', 'start_y')#Starting Y position of Pathway
pos_z = get_config_value('Seeding Path', 'start_z')
plantLength = get_config_value('Seeding Path', 'Plant-to-Plant Delta X\nFor current waffer use 40mm') #Distance between one center of a plant to another X dimention
plantWidth = get_config_value('Seeding Path', 'Plant-to-Plant Delta Y\nFor current waffer use 30mm') #Distance between one center of a plant to another Y dimention
#currently a scaler, make it a list later, the next two inputs
plantCountLong = get_config_value('Seeding Path', '# of Plants Long') #How many plants are in a column
plantCountWide = get_config_value('Seeding Path', '# of Plants Wide') #How many plans are in a row

seedToolX = 1330
seedTrayX = 1330#measure for actual value
seedToolY = 136
seedTrayY = 136#measure for actual value
seedToolZ = -325
seedTrayZ = -50#measure for actual value
toolExtractX = 1240

# Define plant location lists
plant_pos_x, plant_pos_y, plant_pos_z = [], [], -390 #XY dimention of plant in array using 40mm and 30 mm with a z being the planting z height sequence values
'''#After getting these values we should try and output it to a file to see how far off if at all the machine thinks it is, will it?
plant_pos_x_get, plant_pos_y_get, plant_pos_z_get = [], [], [] #XY dimention of plant in array using get_current_positio'''
'''#Computer vision location XYZ values in a list
plant_pos_x_cv, plant_pos_y_cv, plant_pos_z_cv = [], [], []'''
'''
moveAbs(toolExtractX, seedToolY, seedToolZ)
moveAbs(seedToolX,seedToolY,,safeZ)
'''
def move_toSeed_plant(x, y, z'''include vacume pump or hopper dispensation variable here?'''):
    moveAbs(x,y,z)
    moveAbs(x,y,z-5)
    #add the relese of the seed from the hopper and a wait function
    moveAbs(x,y,z+5)        

#Define functions
sense = 1#'sense' is my way of telling the program to go left or right. Sense = 1 Counts UP from ZERO
for i in range(plantCountLong): # for loop for every plant long
    plant_pos_x.append(plantWidth*i+pos_x) # place the plant position in an array
    if sense:
	for j in range(plantCountWide):
	    plant_pos_y.append(plantWidth*j+pos_y)
            if legacy:
                legacy_seed(plant_pos_x[i],plant_pos_y[j],plant_pos_z)
            else:
                move_toSeed_plant(plant_pos_x[i], plant_pos_y[j], plant_pos_z)
            #device.wait()
            #new_plant = app.add_plant(x = x,y = y)
	sense = 0
    else:
	for j in range(plantCountWide-1,-1,-1):
	    plant_pos_y.append(-1*plantWidth*j+pos_y)
            if legacy:
                legacy_seed(plant_pos_x[i],plant_pos_y[j],plant_pos_z)
            else:
                move_toSeed_plant(plant_pos_x[i], plant_pos_y[j], plant_pos_z)
            #device.wait(1000)
            #new_plant = app.add_plant(x = x,y = y)
        sense = 1

'''
Hopeful future use of move_relative(x,y,z,speed)
def moveRel(x, y, z, speed):
    #device.log('Moving to ' + str(x) + ', ' + str(y) + ', ' + str(z), 'success', ['toast'])
    device.move_relative(
        {
            'kind': 'coordinate',
            'args': {'x': x, 'y': y, 'z': z}
        },
        100,
        {
            'kind': 'coordinate',
            'args': {'x': 0, 'y': 0, 'z': 0}
        }
    )
'''

def grabSeeder():
    moveAbs(seedToolX, seedToolY, safeZ)
    moveAbs(seedToolX, seedToolY, seedToolZ)
    moveAbs(toolExtractX, seedToolY, seedToolZ)
def releaseSeeder():
    moveAbs(toolExtractX, seedToolY, seedToolZ)
    moveAbs(seedToolX, seedToolY, seedToolZ)
    moveAbs(seedToolX, seedToolY, safeZ)
def legacy_seed(x,y,z)
    moveAbs(x,y,safeZ)
    moveAbs(seedTrayX,y,safeZ)
    moveAbs(seedTrayX,seedTraY,safeZ)
    moveAbs(seedTrayX,seedTraY,safeZ-10'''this is only a demonstration value of -10''')
    #insert action that sucks seed up
    moveAbs(seedTrayX,seedTraY,safeZ)
    moveAbs(seedTrayX,y,safeZ)
    moveAbs(x,y,safeZ)
    moveAbs(x,y,z)
    moveAbs(x,y,z-5)
    moveAbs(x,y,z)

    
    

def moveAbs(x, y, z):
    device.log('Moving to ' + str(x) + ', ' + str(y) + ', ' + str(z), 'success', ['toast'])
    device.move_absolute(
        {
            'kind': 'coordinate',
            'args': {'x': x, 'y': y, 'z': z}
        },
        100,
        {
            'kind': 'coordinate',
            'args': {'x': 0, 'y': 0, 'z': 0}
        }
    )

device.log('success!!', 'success', ['toast'])

if __name__ == '__main__':
    farmware_name = 'move_to_safe'
