import maya.cmds as cmds

#Grouping Tool Simple
#Select nodes you desire to group
#Run script, it will group the selection under two groups with the names "offset" and "connect

sel = cmds.ls(sl=True, type='transform')

for each in sel:
    cmds.select(each, replace=True)
    offset = cmds.group(name=each + '_offset')
    connect = cmds.group(name=each + '_connect')
