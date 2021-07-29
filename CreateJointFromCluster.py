import maya.cmds as cmds
'''
Joint from Selected Component Center

Instructions:
    Select objects or components and run tool to create a joint at the projected center
'''

cluster = cmds.cluster()[1]
cmds.select(clear=True)
jnt = cmds.joint()
cmds.delete(cmds.pointConstraint(cluster, jnt))
cmds.delete(cluster)
