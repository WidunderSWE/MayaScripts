import maya.cmds as cmds

'''
Creates a plane with joints along it for easier placement
INSTRUCTIONS
  Specify amount of joints and size of plane, run script and move group into position, into a hand/finger for example
'''
#Specify amount of Joints

joints = range(0, 4)
jointList = []
for amount in joints:
    jointList.append(cmds.joint())
    cmds.move(1, 0, 0, localSpace=True)

cmds.select(jointList[0])
cmds.move(-1.5, 0, 0)
    
plane = cmds.polyPlane(name='fingerPlane')
cmds.scale(3, 3, 3)

planeGrp = cmds.group(name='fingerPlaneGRP')
cmds.move(-1.5, 0, 0, 'fingerPlaneGRP.rotatePivot')

cmds.parent(jointList[0], planeGrp)
cmds.select(planeGrp)





