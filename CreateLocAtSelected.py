import maya.cmds as cmds

#Select object and run script to create a Locator at the same location/orientation
#This entire script will parentConstraint the Locator to selected object and bake the animation on the locator
#Remove the parts you don't want to make versions of this script

selected = cmds.ls(sl=True)[0]
hasNameSpace = selected.find(':')

if hasNameSpace == -1:
    selected = cmds.ls(sl=True)[0]
    selectedFullName = cmds.ls(sl=True)[0]
else:
    selected = cmds.ls(sl=True)[0].split(':')[1]
    selectedFullName = cmds.ls(sl=True)[0]
#print selected

#selected = cmds.ls(sl=True)[0]
#selectedName = cmds.ls(sl=True)[0].split(':')[1]

translation = cmds.xform(query=True, absolute=True, worldSpace=True, translation=True)
rotation = cmds.xform(query=True, absolute=True, worldSpace=True, rotation=True)
rot_order = cmds.getAttr('.rotateOrder')

#Create Locator and copy and set rotation order and xform
newLoc = cmds.spaceLocator(name=selected+'_loc')
cmds.setAttr('.rotateOrder', rot_order)
cmds.xform(worldSpace=True, absolute=True, rotation=rotation)
cmds.xform(worldSpace=True, absolute=True, translation=translation)
cmds.xform(scale=(15,15,15))

#PARENT LOCATOR TO SELECTED

#parent constraint Loc to selection
cmds.select(newLoc)
cmds.parentConstraint(selectedFullName, newLoc)


#BAKE ANIMATION TO LOCATOR AND REMOVE CONSTRAINT

timeEnd = cmds.playbackOptions(query=True, animationEndTime=True)
timeStart = cmds.playbackOptions(query=True, animationStartTime=True)


cmds.bakeResults(newLoc, simulation=True, time=(timeStart, timeEnd))
cmds.select(newLoc, r=True)
cmds.DeleteConstraints()
