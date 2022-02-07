import maya.cmds as cmds

selection = cmds.ls(sl=True)

root = selection[0]
hand = selection[1]
prop = selection[2]

#Get Rotation Orders From Controllers
root_rotOrder = cmds.getAttr('{0}.rotateOrder'.format(root))
hand_rotOrder = cmds.getAttr('{0}.rotateOrder'.format(hand))
prop_rotOrder = cmds.getAttr('{0}.rotateOrder'.format(prop))

#Create Locators and Set Rotation Orders
rootLoc = cmds.spaceLocator(name='prop_rootLoc')
cmds.setAttr('.localScale', 25, 25, 25)
cmds.setAttr('.rotateOrder', root_rotOrder)
cmds.setAttr('.overrideEnabled', 1)
cmds.setAttr('.overrideColor', 17)

handLoc = cmds.spaceLocator(name='prop_handLoc')
cmds.setAttr('.localScale', 25, 25, 25)
cmds.setAttr('.rotateOrder', hand_rotOrder)
cmds.setAttr('.overrideEnabled', 1)
cmds.setAttr('.overrideColor', 12)

handOffsetLoc = cmds.spaceLocator(name='prop_handOffsetLoc')
cmds.setAttr('.localScale', 25, 25, 25)
cmds.setAttr('.rotateOrder', hand_rotOrder)
cmds.setAttr('.overrideEnabled', 1)
cmds.setAttr('.overrideColor', 13)

propLoc = cmds.spaceLocator(name='prop_propLoc')
cmds.setAttr('.localScale', 25, 25, 25)
cmds.setAttr('.rotateOrder', prop_rotOrder)
cmds.setAttr('.overrideEnabled', 1)
cmds.setAttr('.overrideColor', 13)

#Parent Locator Hierarchy
cmds.select(rootLoc, handLoc, handOffsetLoc, propLoc)
locators = cmds.ls(sl=True)
for each in locators:
    cmds.select(each, replace=True)
    offset = cmds.group(name=each + '_offset')
    connect = cmds.group(name=each + '_connect')

cmds.parent('prop_handOffsetLoc_connect', 'prop_propLoc_connect', handLoc)
cmds.parent('prop_handLoc_connect', rootLoc)
cmds.parent('prop_rootLoc_connect', root)

rootGrp = 'prop_rootLoc_connect'
handGrp = 'prop_handLoc_connect'
handOffsetGrp = 'prop_handOffsetLoc_connect'
propGrp = 'prop_propLoc_connect'


#Snap Locators to each Controller
cmds.delete(cmds.parentConstraint(root, rootGrp, maintainOffset=False))
cmds.delete(cmds.parentConstraint(hand, handGrp, maintainOffset=False))
cmds.delete(cmds.parentConstraint(hand, handOffsetGrp, maintainOffset=False))
cmds.delete(cmds.parentConstraint(prop, propGrp, maintainOffset=False))

#Create Constraints to Locators
cmds.parentConstraint(handOffsetLoc, hand, maintainOffset=False)
cmds.parentConstraint(propLoc, prop, maintainOffset=False)

