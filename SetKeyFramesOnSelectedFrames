import maya.cmds as cmds
import maya.mel as mel

'''
Set Keyframes on a selected objects on selected frames in timeline
INSTRUCTIONS
- Select object and select a keyrange in timeline
- Run Script
'''

aTimeSlider = mel.eval('$tmpVar=$gPlayBackSlider')
timeRange = cmds.timeControl(aTimeSlider, q=True, rangeArray=True)
firstFrame = int(timeRange[0])
lastFrame = int(timeRange[1])

chosenFrames = range(firstFrame, lastFrame)

for index, element in enumerate(chosenFrames):
    cmds.setKeyframe(time=element, insert=True)
