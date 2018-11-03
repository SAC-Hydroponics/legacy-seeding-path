#!/usr/bin/env python
"""Seeding Path Farmware"""
#Import libraries
from farmware_tools import device, get_config_value, app #sacFarmBot

start_arm_x = device.get_current_position('x')
start_arm_y = device.get_current_position('y')
start_arm_z = device.get_current_position('z')

safeZ = -200

device.log('starting!', 'success', ['toast'])
'''
legacy = get_config_value('Legacy Seeding Path', 'legacy')#User inputs 0 for false and 1 for true.
# Load inputs from Farmware page widget specified in manifest file
pos_x = get_config_value('Legacy Seeding Path', 'start_x')#Starting X position of Pathway
pos_y = get_config_value('Legacy Seeding Path', 'start_y')#Starting Y position of Pathway
pos_z = get_config_value('Legacy Seeding Path', 'start_z')
plantLength = get_config_value('Legacy Seeding Path', 'plant_l') #Distance between one center of a plant to another X dimention
plantWidth = get_config_value('Legacy Seeding Path', 'plant_w') #Distance between one center of a plant to another Y dimention
#currently a scaler, make it a list later, the next two inputs
plantCountLong = get_config_value('Legacy Seeding Path', 'cellX') #How many plants are in a column
plantCountWide = get_config_value('Legacy Seeding Path', 'cellY') #How many plans are in a row

#Seed tool location
seedToolX = 1330
seedToolY = 136
seedToolZ = -325

#Seed tray location
seedTrayX = 1340
seedTrayY = 0
seedTrayZ = -260

toolExtractX = 1240

# Define plant location lists
plant_pos_x, plant_pos_y, plant_pos_z = [], [], pos_z #XY dimention of plant in array using 40mm and 30 mm with a z being the planting z height sequence values

def move_toSeed_plant(x, y, z):
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
'''

if __name__ == '__main__':
    farmware_name = 'move_to_safe'
