import maya.cmds as cmds

#Select objects and run script to change overrideColor

sel = cmds.ls(sl=True, type='transform')

for each in sel:
    cmds.select(each, replace=True)
    
    cmds.setAttr((each + '.overrideEnabled'), 1)
    
    #6 = Blue, 14 = Red, 17 = Yellow
    cmds.setAttr((each + '.overrideColor'), 17)
