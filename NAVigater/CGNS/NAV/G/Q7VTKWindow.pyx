# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CGNS/NAV/T/Q7VTKWindow.ui'
#
# Created: Fri Jun  1 11:38:59 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.9
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Q7VTKWindow(object):
    def setupUi(self, Q7VTKWindow):
        Q7VTKWindow.setObjectName("Q7VTKWindow")
        Q7VTKWindow.resize(803, 679)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Q7VTKWindow.sizePolicy().hasHeightForWidth())
        Q7VTKWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/cgSpy.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Q7VTKWindow.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Q7VTKWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cViews = QtGui.QComboBox(Q7VTKWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cViews.sizePolicy().hasHeightForWidth())
        self.cViews.setSizePolicy(sizePolicy)
        self.cViews.setEditable(True)
        self.cViews.setMaxCount(16)
        self.cViews.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.cViews.setObjectName("cViews")
        self.horizontalLayout.addWidget(self.cViews)
        self.bAddView = QtGui.QPushButton(Q7VTKWindow)
        self.bAddView.setMinimumSize(QtCore.QSize(25, 25))
        self.bAddView.setMaximumSize(QtCore.QSize(25, 25))
        self.bAddView.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/camera-add.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAddView.setIcon(icon1)
        self.bAddView.setObjectName("bAddView")
        self.horizontalLayout.addWidget(self.bAddView)
        self.bSaveView = QtGui.QPushButton(Q7VTKWindow)
        self.bSaveView.setMinimumSize(QtCore.QSize(25, 25))
        self.bSaveView.setMaximumSize(QtCore.QSize(25, 25))
        self.bSaveView.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons/camera-snap.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bSaveView.setIcon(icon2)
        self.bSaveView.setObjectName("bSaveView")
        self.horizontalLayout.addWidget(self.bSaveView)
        self.bRemoveView = QtGui.QPushButton(Q7VTKWindow)
        self.bRemoveView.setMinimumSize(QtCore.QSize(25, 25))
        self.bRemoveView.setMaximumSize(QtCore.QSize(25, 25))
        self.bRemoveView.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icons/camera-remove.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bRemoveView.setIcon(icon3)
        self.bRemoveView.setObjectName("bRemoveView")
        self.horizontalLayout.addWidget(self.bRemoveView)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.selectable = QtGui.QPushButton(Q7VTKWindow)
        self.selectable.setMinimumSize(QtCore.QSize(25, 25))
        self.selectable.setMaximumSize(QtCore.QSize(25, 25))
        self.selectable.setCursor(QtCore.Qt.OpenHandCursor)
        self.selectable.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/icons/move-actor.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectable.setIcon(icon4)
        self.selectable.setCheckable(True)
        self.selectable.setObjectName("selectable")
        self.horizontalLayout.addWidget(self.selectable)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ClippingRange = QtGui.QPushButton(Q7VTKWindow)
        self.ClippingRange.setMinimumSize(QtCore.QSize(25, 25))
        self.ClippingRange.setMaximumSize(QtCore.QSize(25, 25))
        self.ClippingRange.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/icons/value.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ClippingRange.setIcon(icon5)
        self.ClippingRange.setObjectName("ClippingRange")
        self.horizontalLayout.addWidget(self.ClippingRange)
        self.bResetCamera = QtGui.QPushButton(Q7VTKWindow)
        self.bResetCamera.setMinimumSize(QtCore.QSize(25, 25))
        self.bResetCamera.setMaximumSize(QtCore.QSize(25, 25))
        self.bResetCamera.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/icons/zoompoint.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bResetCamera.setIcon(icon6)
        self.bResetCamera.setObjectName("bResetCamera")
        self.horizontalLayout.addWidget(self.bResetCamera)
        self.cRotationAxis = QtGui.QComboBox(Q7VTKWindow)
        self.cRotationAxis.setObjectName("cRotationAxis")
        self.horizontalLayout.addWidget(self.cRotationAxis)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.bSaveVTK = QtGui.QPushButton(Q7VTKWindow)
        self.bSaveVTK.setMinimumSize(QtCore.QSize(25, 25))
        self.bSaveVTK.setMaximumSize(QtCore.QSize(25, 25))
        self.bSaveVTK.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/icons/save.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bSaveVTK.setIcon(icon7)
        self.bSaveVTK.setObjectName("bSaveVTK")
        self.horizontalLayout.addWidget(self.bSaveVTK)
        self.bScreenShot = QtGui.QPushButton(Q7VTKWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bScreenShot.sizePolicy().hasHeightForWidth())
        self.bScreenShot.setSizePolicy(sizePolicy)
        self.bScreenShot.setMinimumSize(QtCore.QSize(25, 25))
        self.bScreenShot.setMaximumSize(QtCore.QSize(25, 25))
        self.bScreenShot.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/icons/snapshot.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bScreenShot.setIcon(icon8)
        self.bScreenShot.setObjectName("bScreenShot")
        self.horizontalLayout.addWidget(self.bScreenShot)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(Q7VTKWindow)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bX = QtGui.QPushButton(Q7VTKWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bX.sizePolicy().hasHeightForWidth())
        self.bX.setSizePolicy(sizePolicy)
        self.bX.setMinimumSize(QtCore.QSize(25, 25))
        self.bX.setMaximumSize(QtCore.QSize(25, 25))
        self.bX.setObjectName("bX")
        self.horizontalLayout_3.addWidget(self.bX)
        self.bY = QtGui.QPushButton(Q7VTKWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bY.sizePolicy().hasHeightForWidth())
        self.bY.setSizePolicy(sizePolicy)
        self.bY.setMinimumSize(QtCore.QSize(25, 25))
        self.bY.setMaximumSize(QtCore.QSize(25, 25))
        self.bY.setObjectName("bY")
        self.horizontalLayout_3.addWidget(self.bY)
        self.bZ = QtGui.QPushButton(Q7VTKWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bZ.sizePolicy().hasHeightForWidth())
        self.bZ.setSizePolicy(sizePolicy)
        self.bZ.setMinimumSize(QtCore.QSize(25, 25))
        self.bZ.setMaximumSize(QtCore.QSize(25, 25))
        self.bZ.setObjectName("bZ")
        self.horizontalLayout_3.addWidget(self.bZ)
        self.cMirror = QtGui.QCheckBox(Q7VTKWindow)
        self.cMirror.setObjectName("cMirror")
        self.horizontalLayout_3.addWidget(self.cMirror)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.bSuffleColors = QtGui.QPushButton(Q7VTKWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bSuffleColors.sizePolicy().hasHeightForWidth())
        self.bSuffleColors.setSizePolicy(sizePolicy)
        self.bSuffleColors.setMinimumSize(QtCore.QSize(25, 25))
        self.bSuffleColors.setMaximumSize(QtCore.QSize(25, 25))
        self.bSuffleColors.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/icons/colors.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bSuffleColors.setIcon(icon9)
        self.bSuffleColors.setObjectName("bSuffleColors")
        self.horizontalLayout_3.addWidget(self.bSuffleColors)
        self.bBlackColor = QtGui.QPushButton(Q7VTKWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bBlackColor.sizePolicy().hasHeightForWidth())
        self.bBlackColor.setSizePolicy(sizePolicy)
        self.bBlackColor.setMinimumSize(QtCore.QSize(25, 25))
        self.bBlackColor.setMaximumSize(QtCore.QSize(25, 25))
        self.bBlackColor.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/icons/colors-bw.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bBlackColor.setIcon(icon10)
        self.bBlackColor.setObjectName("bBlackColor")
        self.horizontalLayout_3.addWidget(self.bBlackColor)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.bColorMapMin = QtGui.QPushButton(Q7VTKWindow)
        self.bColorMapMin.setMinimumSize(QtCore.QSize(25, 25))
        self.bColorMapMin.setMaximumSize(QtCore.QSize(25, 25))
        self.bColorMapMin.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/icons/colors-first.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bColorMapMin.setIcon(icon11)
        self.bColorMapMin.setObjectName("bColorMapMin")
        self.horizontalLayout_3.addWidget(self.bColorMapMin)
        self.bColorMapMax = QtGui.QPushButton(Q7VTKWindow)
        self.bColorMapMax.setMinimumSize(QtCore.QSize(25, 25))
        self.bColorMapMax.setMaximumSize(QtCore.QSize(25, 25))
        self.bColorMapMax.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/icons/colors-last.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bColorMapMax.setIcon(icon12)
        self.bColorMapMax.setObjectName("bColorMapMax")
        self.horizontalLayout_3.addWidget(self.bColorMapMax)
        self.cVariables = QtGui.QComboBox(Q7VTKWindow)
        self.cVariables.setObjectName("cVariables")
        self.horizontalLayout_3.addWidget(self.cVariables)
        self.cColorSpace = QtGui.QComboBox(Q7VTKWindow)
        self.cColorSpace.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cColorSpace.setObjectName("cColorSpace")
        self.horizontalLayout_3.addWidget(self.cColorSpace)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.bZoom = QtGui.QPushButton(Q7VTKWindow)
        self.bZoom.setMinimumSize(QtCore.QSize(25, 25))
        self.bZoom.setMaximumSize(QtCore.QSize(25, 25))
        self.bZoom.setCheckable(True)
        self.bZoom.setObjectName("bZoom")
        self.horizontalLayout_3.addWidget(self.bZoom)
        self.bLabeledMesh = QtGui.QPushButton(Q7VTKWindow)
        self.bLabeledMesh.setMinimumSize(QtCore.QSize(25, 25))
        self.bLabeledMesh.setMaximumSize(QtCore.QSize(25, 25))
        self.bLabeledMesh.setCheckable(True)
        self.bLabeledMesh.setObjectName("bLabeledMesh")
        self.horizontalLayout_3.addWidget(self.bLabeledMesh)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.display = QVTKRenderWindowInteractor(Q7VTKWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display.sizePolicy().hasHeightForWidth())
        self.display.setSizePolicy(sizePolicy)
        self.display.setObjectName("display")
        self.verticalLayout_2.addWidget(self.display)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bBackControl = QtGui.QPushButton(Q7VTKWindow)
        self.bBackControl.setMinimumSize(QtCore.QSize(25, 25))
        self.bBackControl.setMaximumSize(QtCore.QSize(25, 25))
        self.bBackControl.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/icons/top.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bBackControl.setIcon(icon13)
        self.bBackControl.setObjectName("bBackControl")
        self.horizontalLayout_2.addWidget(self.bBackControl)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.bUpdate = QtGui.QPushButton(Q7VTKWindow)
        self.bUpdate.setMinimumSize(QtCore.QSize(25, 25))
        self.bUpdate.setMaximumSize(QtCore.QSize(25, 25))
        self.bUpdate.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/images/icons/undo-last-modification.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bUpdate.setIcon(icon14)
        self.bUpdate.setObjectName("bUpdate")
        self.horizontalLayout_2.addWidget(self.bUpdate)
        self.cCurrentPath = QtGui.QComboBox(Q7VTKWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cCurrentPath.sizePolicy().hasHeightForWidth())
        self.cCurrentPath.setSizePolicy(sizePolicy)
        self.cCurrentPath.setEditable(True)
        self.cCurrentPath.setObjectName("cCurrentPath")
        self.horizontalLayout_2.addWidget(self.cCurrentPath)
        self.bReverse = QtGui.QPushButton(Q7VTKWindow)
        self.bReverse.setMinimumSize(QtCore.QSize(25, 25))
        self.bReverse.setMaximumSize(QtCore.QSize(25, 25))
        self.bReverse.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/icons/flag-revert.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bReverse.setIcon(icon15)
        self.bReverse.setObjectName("bReverse")
        self.horizontalLayout_2.addWidget(self.bReverse)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.sIndex1 = QtGui.QSpinBox(Q7VTKWindow)
        self.sIndex1.setObjectName("sIndex1")
        self.horizontalLayout_2.addWidget(self.sIndex1)
        self.sIndex2 = QtGui.QSpinBox(Q7VTKWindow)
        self.sIndex2.setObjectName("sIndex2")
        self.horizontalLayout_2.addWidget(self.sIndex2)
        self.sIndex3 = QtGui.QSpinBox(Q7VTKWindow)
        self.sIndex3.setObjectName("sIndex3")
        self.horizontalLayout_2.addWidget(self.sIndex3)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.bPrevious = QtGui.QPushButton(Q7VTKWindow)
        self.bPrevious.setMinimumSize(QtCore.QSize(25, 25))
        self.bPrevious.setMaximumSize(QtCore.QSize(25, 25))
        self.bPrevious.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/images/icons/control.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bPrevious.setIcon(icon16)
        self.bPrevious.setObjectName("bPrevious")
        self.horizontalLayout_2.addWidget(self.bPrevious)
        self.bReset = QtGui.QPushButton(Q7VTKWindow)
        self.bReset.setMinimumSize(QtCore.QSize(25, 25))
        self.bReset.setMaximumSize(QtCore.QSize(25, 25))
        self.bReset.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/images/icons/node-sids-leaf.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bReset.setIcon(icon17)
        self.bReset.setObjectName("bReset")
        self.horizontalLayout_2.addWidget(self.bReset)
        self.bNext = QtGui.QPushButton(Q7VTKWindow)
        self.bNext.setMinimumSize(QtCore.QSize(25, 25))
        self.bNext.setMaximumSize(QtCore.QSize(25, 25))
        self.bNext.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/images/icons/node-sids-closed.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bNext.setIcon(icon18)
        self.bNext.setObjectName("bNext")
        self.horizontalLayout_2.addWidget(self.bNext)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Q7VTKWindow)
        QtCore.QMetaObject.connectSlotsByName(Q7VTKWindow)

    def retranslateUi(self, Q7VTKWindow):
        Q7VTKWindow.setWindowTitle(QtGui.QApplication.translate("Q7VTKWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))
        Q7VTKWindow.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Show value", None, QtGui.QApplication.UnicodeUTF8))
        self.bAddView.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Add current view to view list", None, QtGui.QApplication.UnicodeUTF8))
        self.bSaveView.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Write view list into a file", None, QtGui.QApplication.UnicodeUTF8))
        self.bRemoveView.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Remove current view from view list", None, QtGui.QApplication.UnicodeUTF8))
        self.selectable.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Move legend", None, QtGui.QApplication.UnicodeUTF8))
        self.bResetCamera.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Zoom and center on selected", None, QtGui.QApplication.UnicodeUTF8))
        self.cRotationAxis.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Rotation axis", None, QtGui.QApplication.UnicodeUTF8))
        self.bSaveVTK.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Save VTK data into a file", None, QtGui.QApplication.UnicodeUTF8))
        self.bScreenShot.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Save view snapshot into a file", None, QtGui.QApplication.UnicodeUTF8))
        self.bX.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Show Y/Z plane", None, QtGui.QApplication.UnicodeUTF8))
        self.bX.setText(QtGui.QApplication.translate("Q7VTKWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.bY.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Show X/Z plane", None, QtGui.QApplication.UnicodeUTF8))
        self.bY.setText(QtGui.QApplication.translate("Q7VTKWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.bZ.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Show X/Y plane", None, QtGui.QApplication.UnicodeUTF8))
        self.bZ.setText(QtGui.QApplication.translate("Q7VTKWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.cMirror.setText(QtGui.QApplication.translate("Q7VTKWindow", "Mirror", None, QtGui.QApplication.UnicodeUTF8))
        self.bSuffleColors.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Change colors to random", None, QtGui.QApplication.UnicodeUTF8))
        self.bBlackColor.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Switch black/white colors", None, QtGui.QApplication.UnicodeUTF8))
        self.bZoom.setText(QtGui.QApplication.translate("Q7VTKWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.bLabeledMesh.setText(QtGui.QApplication.translate("Q7VTKWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.bBackControl.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Raise CGNS.NAV control window", None, QtGui.QApplication.UnicodeUTF8))
        self.bUpdate.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Update selected list from tree view", None, QtGui.QApplication.UnicodeUTF8))
        self.bReverse.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Switch seleted and  unselected actors", None, QtGui.QApplication.UnicodeUTF8))
        self.sIndex3.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Get/Set index for third dim", None, QtGui.QApplication.UnicodeUTF8))
        self.bPrevious.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Highlight previous selected item", None, QtGui.QApplication.UnicodeUTF8))
        self.bReset.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Clear selection list", None, QtGui.QApplication.UnicodeUTF8))
        self.bNext.setToolTip(QtGui.QApplication.translate("Q7VTKWindow", "Highlight next selected item", None, QtGui.QApplication.UnicodeUTF8))

from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import Res_rc
