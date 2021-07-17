import maya.cmds as cmds
import maya.mel as mel

#Project Weights to Last Selected

lastSelected = cmds.ls(sl=True, type='transform', tl=True)[0]
cmds.select(lastSelected, tgl=True)

sel = cmds.ls(sl=True, type='transform')

for each in sel:
    cmds.copySkinWeights(lastSelected, each, noMirror=True, surfaceAssociation='closestPoint', influenceAssociation=['closestJoint', 'oneToOne', 'oneToOne'], normalize=True)
