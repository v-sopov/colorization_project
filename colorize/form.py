# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)
        self.horizontalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 10, 10, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.raw_folder_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.raw_folder_input.setFont(font)
        self.raw_folder_input.setText("")
        self.raw_folder_input.setObjectName("raw_folder_input")
        self.horizontalLayout_2.addWidget(self.raw_folder_input)
        self.raw_folder_dialog_button = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.raw_folder_dialog_button.setObjectName("raw_folder_dialog_button")
        self.horizontalLayout_2.addWidget(self.raw_folder_dialog_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.prev_image_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.prev_image_button.setObjectName("prev_image_button")
        self.horizontalLayout_8.addWidget(self.prev_image_button)
        self.current_image_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.current_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_image_label.setObjectName("current_image_label")
        self.horizontalLayout_8.addWidget(self.current_image_label)
        self.next_image_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.next_image_button.setObjectName("next_image_button")
        self.horizontalLayout_8.addWidget(self.next_image_button)
        self.horizontalLayout_8.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.colorpicker_mode_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorpicker_mode_button.sizePolicy().hasHeightForWidth())
        self.colorpicker_mode_button.setSizePolicy(sizePolicy)
        self.colorpicker_mode_button.setObjectName("colorpicker_mode_button")
        self.gridLayout.addWidget(self.colorpicker_mode_button, 0, 1, 1, 1)
        self.brush_mode_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brush_mode_button.sizePolicy().hasHeightForWidth())
        self.brush_mode_button.setSizePolicy(sizePolicy)
        self.brush_mode_button.setObjectName("brush_mode_button")
        self.gridLayout.addWidget(self.brush_mode_button, 0, 0, 1, 1)
        self.tip_mode_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tip_mode_button.sizePolicy().hasHeightForWidth())
        self.tip_mode_button.setSizePolicy(sizePolicy)
        self.tip_mode_button.setCheckable(False)
        self.tip_mode_button.setFlat(False)
        self.tip_mode_button.setObjectName("tip_mode_button")
        self.gridLayout.addWidget(self.tip_mode_button, 0, 2, 1, 1)
        self.fill_mode_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fill_mode_button.sizePolicy().hasHeightForWidth())
        self.fill_mode_button.setSizePolicy(sizePolicy)
        self.fill_mode_button.setObjectName("fill_mode_button")
        self.gridLayout.addWidget(self.fill_mode_button, 1, 1, 1, 1)
        self.eraser_mode_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eraser_mode_button.sizePolicy().hasHeightForWidth())
        self.eraser_mode_button.setSizePolicy(sizePolicy)
        self.eraser_mode_button.setObjectName("eraser_mode_button")
        self.gridLayout.addWidget(self.eraser_mode_button, 1, 0, 1, 1)
        self.select_mode_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.select_mode_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_mode_button.sizePolicy().hasHeightForWidth())
        self.select_mode_button.setSizePolicy(sizePolicy)
        self.select_mode_button.setText("")
        self.select_mode_button.setFlat(False)
        self.select_mode_button.setObjectName("select_mode_button")
        self.gridLayout.addWidget(self.select_mode_button, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.palette = Palette(self.horizontalLayoutWidget)
        self.palette.setMinimumSize(QtCore.QSize(50, 50))
        self.palette.setObjectName("palette")
        self.verticalLayout.addWidget(self.palette)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.brush_opacity_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brush_opacity_input.sizePolicy().hasHeightForWidth())
        self.brush_opacity_input.setSizePolicy(sizePolicy)
        self.brush_opacity_input.setMinimumSize(QtCore.QSize(25, 0))
        self.brush_opacity_input.setObjectName("brush_opacity_input")
        self.gridLayout_2.addWidget(self.brush_opacity_input, 1, 2, 1, 1)
        self.brush_size_slider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.brush_size_slider.setMinimum(1)
        self.brush_size_slider.setMaximum(50)
        self.brush_size_slider.setProperty("value", 10)
        self.brush_size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brush_size_slider.setObjectName("brush_size_slider")
        self.gridLayout_2.addWidget(self.brush_size_slider, 0, 1, 1, 1)
        self.brush_opacity_slider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.brush_opacity_slider.setMaximum(100)
        self.brush_opacity_slider.setProperty("value", 100)
        self.brush_opacity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brush_opacity_slider.setObjectName("brush_opacity_slider")
        self.gridLayout_2.addWidget(self.brush_opacity_slider, 1, 1, 1, 1)
        self.brush_hardness_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brush_hardness_input.sizePolicy().hasHeightForWidth())
        self.brush_hardness_input.setSizePolicy(sizePolicy)
        self.brush_hardness_input.setMinimumSize(QtCore.QSize(25, 0))
        self.brush_hardness_input.setObjectName("brush_hardness_input")
        self.gridLayout_2.addWidget(self.brush_hardness_input, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.brush_hardness_slider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.brush_hardness_slider.setMinimum(1)
        self.brush_hardness_slider.setMaximum(100)
        self.brush_hardness_slider.setProperty("value", 90)
        self.brush_hardness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brush_hardness_slider.setObjectName("brush_hardness_slider")
        self.gridLayout_2.addWidget(self.brush_hardness_slider, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.brush_size_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brush_size_input.sizePolicy().hasHeightForWidth())
        self.brush_size_input.setSizePolicy(sizePolicy)
        self.brush_size_input.setMinimumSize(QtCore.QSize(25, 0))
        self.brush_size_input.setObjectName("brush_size_input")
        self.gridLayout_2.addWidget(self.brush_size_input, 0, 2, 1, 1)
        self.gridLayout_2.setColumnMinimumWidth(1, 100)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.colorization_progress_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.colorization_progress_label.setText("")
        self.colorization_progress_label.setAlignment(QtCore.Qt.AlignCenter)
        self.colorization_progress_label.setObjectName("colorization_progress_label")
        self.verticalLayout.addWidget(self.colorization_progress_label)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.image_size_slider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.image_size_slider.setMinimum(3)
        self.image_size_slider.setMaximum(24)
        self.image_size_slider.setSingleStep(1)
        self.image_size_slider.setPageStep(1)
        self.image_size_slider.setProperty("value", 9)
        self.image_size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.image_size_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.image_size_slider.setTickInterval(1)
        self.image_size_slider.setObjectName("image_size_slider")
        self.horizontalLayout_3.addWidget(self.image_size_slider)
        self.image_size_value = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image_size_value.setObjectName("image_size_value")
        self.horizontalLayout_3.addWidget(self.image_size_value)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.save_folder_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.save_folder_input.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.save_folder_input.setFont(font)
        self.save_folder_input.setText("")
        self.save_folder_input.setObjectName("save_folder_input")
        self.horizontalLayout_7.addWidget(self.save_folder_input)
        self.save_folder_dialog_button = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.save_folder_dialog_button.setObjectName("save_folder_dialog_button")
        self.horizontalLayout_7.addWidget(self.save_folder_dialog_button)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.save_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.save_button.setFlat(False)
        self.save_button.setObjectName("save_button")
        self.verticalLayout.addWidget(self.save_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.raw_image = Canvas(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.raw_image.sizePolicy().hasHeightForWidth())
        self.raw_image.setSizePolicy(sizePolicy)
        self.raw_image.setMinimumSize(QtCore.QSize(100, 100))
        self.raw_image.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_image.setObjectName("raw_image")
        self.horizontalLayout.addWidget(self.raw_image)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.colorize_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorize_button.sizePolicy().hasHeightForWidth())
        self.colorize_button.setSizePolicy(sizePolicy)
        self.colorize_button.setMinimumSize(QtCore.QSize(40, 0))
        self.colorize_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.colorize_button.setIconSize(QtCore.QSize(16, 16))
        self.colorize_button.setObjectName("colorize_button")
        self.verticalLayout_3.addWidget(self.colorize_button)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.colorized_image = Canvas(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.colorized_image.sizePolicy().hasHeightForWidth())
        self.colorized_image.setSizePolicy(sizePolicy)
        self.colorized_image.setMinimumSize(QtCore.QSize(100, 100))
        self.colorized_image.setAlignment(QtCore.Qt.AlignCenter)
        self.colorized_image.setObjectName("colorized_image")
        self.horizontalLayout.addWidget(self.colorized_image)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 7)
        self.horizontalLayout.setStretch(3, 7)
        MainWindow.setCentralWidget(self.horizontalLayoutWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Folder"))
        self.raw_folder_dialog_button.setText(_translate("MainWindow", "..."))
        self.prev_image_button.setText(_translate("MainWindow", "<"))
        self.current_image_label.setText(_translate("MainWindow", "SELECT FOLDER"))
        self.next_image_button.setText(_translate("MainWindow", ">"))
        self.colorpicker_mode_button.setText(_translate("MainWindow", "CP"))
        self.brush_mode_button.setText(_translate("MainWindow", "Br"))
        self.tip_mode_button.setText(_translate("MainWindow", "Tip"))
        self.fill_mode_button.setText(_translate("MainWindow", "Fill"))
        self.eraser_mode_button.setText(_translate("MainWindow", "Eras"))
        self.brush_opacity_input.setText(_translate("MainWindow", "100"))
        self.brush_hardness_input.setText(_translate("MainWindow", "90"))
        self.label_6.setText(_translate("MainWindow", "Hardness"))
        self.label_5.setText(_translate("MainWindow", "Opacity"))
        self.label_4.setText(_translate("MainWindow", "Size"))
        self.brush_size_input.setText(_translate("MainWindow", "10"))
        self.label.setText(_translate("MainWindow", "Image Size"))
        self.image_size_value.setText(_translate("MainWindow", "1536"))
        self.save_folder_dialog_button.setText(_translate("MainWindow", "..."))
        self.save_button.setText(_translate("MainWindow", "SAVE"))
        self.raw_image.setText(_translate("MainWindow", "raw_image"))
        self.colorize_button.setText(_translate("MainWindow", "->"))
        self.colorized_image.setText(_translate("MainWindow", "colorized_image"))
from canvas import Canvas
from palette import Palette
