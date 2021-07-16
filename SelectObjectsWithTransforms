import maya.cmds as cmds

#Script to help with scene/object cleanup.
#INSTRUCTIONS:
#Select objects in a scene, run script.
#The script will select objects with local object transforms.

objects = cmds.ls(sl=True)
cmds.select(clear=True)

for each in objects:
    
    translate = list(cmds.getAttr(each+'.translate')[0])
    rotate = list(cmds.getAttr(each+'.rotate')[0])
    scale = list(cmds.getAttr(each+'.scale')[0])
    
    for attribute in translate or rotate:
        if attribute != 0.0:
            cmds.select(each, add=True)
            
    for value in scale:
        if value != 1.0:
            cmds.select(each, add=True)
