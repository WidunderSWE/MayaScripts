import maya.cmds as cmds

#Select to joints, parent and child
#Run script and choose how many joints you'd like to add in between
#Assumes Joints have X flowing along the chain

##############################################################################################
#UI

def ui():
    if cmds.window('segmentJoints', exists=True):
        cmds.deleteUI('segmentJoints')
        
    segmentJointsWin = cmds.window('segmentJoints', mxb=False)
    cmds.showWindow(segmentJointsWin)
    #cmds.windowPref( 'segmentJoints', remove=True)
    cmds.window('segmentJoints', e=True, height=140, width=135, s=False, tlb=True)
    cmds.rowColumnLayout()
      
    cmds.text(label='Segment Joints', height=20)
    cmds.text(label='----', height=10)
    
    cmds.text(label='Joint Amount:', height=20)
    cmds.intField('jointAmount',value=2, minValue=2, step=1)
    cmds.text(label='', height=5)

    cmds.button(label='Segment Joints', height=30, bgc=[0.4, 0.7, 0.7], command='segmentJoints()')
    
    cmds.text(label='', height=10)
    cmds.text(label='Markus Hammarstedt 2021', font='smallPlainLabelFont')
    cmds.text(label='www.gumroad.com/widunder', font='smallPlainLabelFont')
    cmds.text(label='www.twitter.com/widunder', font='smallPlainLabelFont')
    
ui()

###########################################################################################
#function

def segmentJoints():

    val = cmds.intField('jointAmount', query=True, value=True)
    selRoot = cmds.ls(sl=True, type='joint')[0]
    cmds.select(selRoot, hierarchy=True)
    chain = cmds.ls(sl=True)

#Get TranslateX and Radius Value of root joint
    if len(chain) > 1:
        selChild = cmds.listRelatives(selRoot, c=True)[0]
        tx = cmds.getAttr(selChild+'.translateX')
        radius = cmds.getAttr(selChild+'.radius')
        cmds.select(selRoot, r=True)
    
        #Create segmented Joints
        for i in range(1, val):
            jnt = cmds.joint(rad=radius)
            cmds.move(tx/val, 0, 0, ls=True)
        
        #Select last new joint created
        lastJnt = cmds.ls(sl=True, type='joint')
        cmds.parent(selChild, lastJnt)
    
    else:
        cmds.warning('Please select a bone with a child')
