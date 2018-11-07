#!/usr/bin/env python

from farmware_tools import device, get_config_value

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

safeZ = -200
plantLocation = [[0, 0], [0, 38], [0, 76], [0, 114], [0, 152], [0, 190], [0, 229], [0, 267], [0, 305], [0, 343], [0, 381], [0, 419], [0, 457], [32, 0], [32, 38], [32, 76], [32, 114], [32, 152], [32, 190], [32, 229], [32, 267], [32, 305], [32, 343], [32, 381], [32, 419], [32, 457], [64, 0], [64, 38], [64, 76], [64, 114], [64, 152], [64, 190], [64, 229], [64, 267], [64, 305], [64, 343], [64, 381], [64, 419], [64, 457], [95, 0], [95, 38], [95, 76], [95, 114], [95, 152], [95, 190], [95, 229], [95, 267], [95, 305], [95, 343], [95, 381], [95, 419], [95, 457], [127, 0], [127, 38], [127, 76], [127, 114], [127, 152], [127, 190], [127, 229], [127, 267], [127, 305], [127, 343], [127, 381], [127, 419], [127, 457], [159, 0], [159, 38], [159, 76], [159, 114], [159, 152], [159, 190], [159, 229], [159, 267], [159, 305], [159, 343], [159, 381], [159, 419], [159, 457], [190, 0], [190, 38], [190, 76], [190, 114], [190, 152], [190, 190], [190, 229], [190, 267], [190, 305], [190, 343], [190, 381], [190, 419], [190, 457], [222, 0], [222, 38], [222, 76], [222, 114], [222, 152], [222, 190], [222, 229], [222, 267], [222, 305], [222, 343], [222, 381], [222, 419], [222, 457]]
seedToolX = 1330
seedToolY = 136
seedToolZ = -325
            
toolExtractX = 1240
            
seedTrayX = 1340
seedTrayY = 0

pos_x = get_config_value('Seeding Path', 'start_x')
pos_y = get_config_value('Seeding Path', 'start_y')
pos_z = get_config_value('Seeding Path', 'start_z')

##Starting from [0,0,0]

moveAbs(seedToolX, seedToolY, safeZ)
moveAbs(seedToolX, seedToolY, seedToolZ)
moveAbs(toolExtractX, seedToolY, seedToolZ)
moveAbs(toolExtractX, seedToolY, safeZ)
            
for i in range(len(plantLocation)):
    moveAbs(seedTrayX, seedTrayY, safeZ)
    moveAbs(seedTrayX, seedTrayY, safeZ-10)
    moveAbs(seedTrayX, seedTrayY, safeZ)
    moveAbs(plantLocation[i][0]+pos_x, plantLocation[i][1]+pos_y, safeZ)
    moveAbs(plantLocation[i][0]+pos_x, plantLocation[i][1]+pos_y, safeZ-10)
    moveAbs(plantLocation[i][0]+pos_x, plantLocation[i][1]+pos_y, safeZ)
    
moveAbs(toolExtractX, seedToolY, seedToolZ)
moveAbs(seedToolX, seedToolY, seedToolZ)
moveAbs(seedToolX, seedToolY, safeZ)

#insert moveAbs(home)

device.log('success!!', 'success', ['toast'])

if __name__ == '__main__':
    farmware_name = 'move_to_safe'
