#  -------------------------------------------------------------------------
#  pyCGNS - Python package for CFD General Notation System - 
#  See license.txt file in the root directory of this Python module source  
#  -------------------------------------------------------------------------
#
from __future__ import unicode_literals
from builtins import (str, bytes, range, dict)

from qtpy.QtCore import Qt
from qtpy.QtWidgets import *

RAISEVIEW = '@@RAISEVIEW@@'
CLOSEVIEW = '@@CLOSEVIEW@@'
INFO = '@@INFOVIEW@@'

KEYMAPPING = {
    RAISEVIEW: Qt.Key_Space,
    CLOSEVIEW: Qt.Key_Delete,
    INFO: Qt.Key_Enter,
}


# -----------------------------------------------------------------
class Q7ControlTableWidget(QTableWidget):
    def mousePressEvent(self, event):
        self.lastPos = event.globalPos()
        self.lastButton = event.button()
        QTableWidget.mousePressEvent(self, event)

    def keyPressEvent(self, event):
        # kmod = event.modifiers()
        kval = event.key()
        if kval == KEYMAPPING[RAISEVIEW]:
            self.control.raiseView()
            return
        if kval == KEYMAPPING[CLOSEVIEW]:
            self.control.closeView()
            return
        if kval == KEYMAPPING[INFO]:
            self.control.info()
            return
        QTableWidget.keyPressEvent(self, event)

# -----------------------------------------------------------------
