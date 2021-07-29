import maya.cmds as cmds
'''
Transfer rotation to joint orient values
'''

sel_jnts = cmds.ls(sl=True, type='joint')

for each_jnt in sel_jnts:
    cmds.delete(each_jnt, constraints=True)
    
    rx = cmds.getAttr(each_jnt+'.rotateX')
    ry = cmds.getAttr(each_jnt+'.rotateY')
    rz = cmds.getAttr(each_jnt+'.rotateZ')
    
    cmds.setAttr(each_jnt+'.jointOrientX', rx)
    cmds.setAttr(each_jnt+'.jointOrientY', ry)
    cmds.setAttr(each_jnt+'.jointOrientZ', rz)
    
    cmds.setAttr(each_jnt+'.rotateX', 0)
    cmds.setAttr(each_jnt+'.rotateY', 0)
    cmds.setAttr(each_jnt+'.rotateZ', 0)
