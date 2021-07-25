import maya.cmds as cmds
import maya.OpenMayaUI as mui
from PySide2 import QtWidgets
import shiboken2

'''
GraphEditor with a transparency slider
'''

if cmds.window("GEW", exists=True): cmds.deleteUI("GEW", window=True) 
cmds.window( "GEW", title="Graph Editor +" )
cmds.paneLayout( configuration='single' )
cmds.scriptedPanel( type='graphEditor' )
cmds.columnLayout (adj=1)
cmds.floatSlider(min=0.1, max=1.0, v=1.0, dc=lambda x:ref(x))
cmds.showWindow("GEW")
GEQ = shiboken2.wrapInstance(long(mui.MQtUtil.findWindow( "GEW" )), QtWidgets.QWidget)
def ref(value): GEQ.setWindowOpacity(value)
GEQ.setWindowOpacity(1.0)
