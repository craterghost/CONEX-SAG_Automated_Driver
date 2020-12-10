# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1734, 702)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.layout_grid_center = QtWidgets.QGridLayout(self.centralwidget)
        self.layout_grid_center.setObjectName("layout_grid_center")
        self.layout_leftside = QtWidgets.QVBoxLayout()
        self.layout_leftside.setObjectName("layout_leftside")
        self.list_pos = QtWidgets.QListWidget(self.centralwidget)
        self.list_pos.setObjectName("list_pos")
        item = QtWidgets.QListWidgetItem()
        self.list_pos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_pos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_pos.addItem(item)
        self.layout_leftside.addWidget(self.list_pos)
        self.button_delete_pos = QtWidgets.QPushButton(self.centralwidget)
        self.button_delete_pos.setObjectName("button_delete_pos")
        self.layout_leftside.addWidget(self.button_delete_pos)
        self.layout_delay = QtWidgets.QHBoxLayout()
        self.layout_delay.setObjectName("layout_delay")
        self.spinbox_delay_length = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinbox_delay_length.setObjectName("spinbox_delay_length")
        self.layout_delay.addWidget(self.spinbox_delay_length)
        self.label_delay = QtWidgets.QLabel(self.centralwidget)
        self.label_delay.setObjectName("label_delay")
        self.layout_delay.addWidget(self.label_delay)
        self.button_add_delay = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_delay.setToolTip("")
        self.button_add_delay.setObjectName("button_add_delay")
        self.layout_delay.addWidget(self.button_add_delay)
        self.layout_leftside.addLayout(self.layout_delay)
        self.layout_line_repetitions = QtWidgets.QHBoxLayout()
        self.layout_line_repetitions.setObjectName("layout_line_repetitions")
        self.spinbox_rep_count = QtWidgets.QSpinBox(self.centralwidget)
        self.spinbox_rep_count.setObjectName("spinbox_rep_count")
        self.layout_line_repetitions.addWidget(self.spinbox_rep_count)
        self.label_repetitions = QtWidgets.QLabel(self.centralwidget)
        self.label_repetitions.setObjectName("label_repetitions")
        self.layout_line_repetitions.addWidget(self.label_repetitions)
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setObjectName("button_start")
        self.layout_line_repetitions.addWidget(self.button_start)
        self.layout_leftside.addLayout(self.layout_line_repetitions)
        self.layout_grid_center.addLayout(self.layout_leftside, 0, 0, 1, 1)
        self.spacer_shear_api = QtWidgets.QLabel(self.centralwidget)
        self.spacer_shear_api.setText("")
        self.spacer_shear_api.setPixmap(QtGui.QPixmap("media/shear.jpeg"))
        self.spacer_shear_api.setObjectName("spacer_shear_api")
        self.layout_grid_center.addWidget(self.spacer_shear_api, 0, 2, 1, 1)
        self.layout_rightside = QtWidgets.QVBoxLayout()
        self.layout_rightside.setObjectName("layout_rightside")
        self.hor_1 = QtWidgets.QHBoxLayout()
        self.hor_1.setContentsMargins(-1, -1, -1, 50)
        self.hor_1.setObjectName("hor_1")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_axis_settings = QtWidgets.QLabel(self.centralwidget)
        self.label_axis_settings.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_axis_settings.setObjectName("label_axis_settings")
        self.verticalLayout.addWidget(self.label_axis_settings)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.check_switchxy = QtWidgets.QCheckBox(self.centralwidget)
        self.check_switchxy.setObjectName("check_switchxy")
        self.horizontalLayout.addWidget(self.check_switchxy)
        self.check_reverse_y = QtWidgets.QCheckBox(self.centralwidget)
        self.check_reverse_y.setMinimumSize(QtCore.QSize(0, 0))
        self.check_reverse_y.setObjectName("check_reverse_y")
        self.horizontalLayout.addWidget(self.check_reverse_y)
        self.check_reverse_x = QtWidgets.QCheckBox(self.centralwidget)
        self.check_reverse_x.setObjectName("check_reverse_x")
        self.horizontalLayout.addWidget(self.check_reverse_x)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.hor_1.addLayout(self.verticalLayout)
        self.label_sia = QtWidgets.QLabel(self.centralwidget)
        self.label_sia.setText("")
        self.label_sia.setPixmap(QtGui.QPixmap("media/SIA.png"))
        self.label_sia.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sia.setObjectName("label_sia")
        self.hor_1.addWidget(self.label_sia)
        self.layout_rightside.addLayout(self.hor_1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(-1, -1, -1, 50)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_smallest = QtWidgets.QPushButton(self.centralwidget)
        self.button_smallest.setObjectName("button_smallest")
        self.horizontalLayout_5.addWidget(self.button_smallest)
        self.button_small = QtWidgets.QPushButton(self.centralwidget)
        self.button_small.setObjectName("button_small")
        self.horizontalLayout_5.addWidget(self.button_small)
        self.button_medium = QtWidgets.QPushButton(self.centralwidget)
        self.button_medium.setObjectName("button_medium")
        self.horizontalLayout_5.addWidget(self.button_medium)
        self.button_big = QtWidgets.QPushButton(self.centralwidget)
        self.button_big.setObjectName("button_big")
        self.horizontalLayout_5.addWidget(self.button_big)
        self.gridLayout.addLayout(self.horizontalLayout_5, 8, 1, 1, 1)
        self.label_moving_speed = QtWidgets.QLabel(self.centralwidget)
        self.label_moving_speed.setMaximumSize(QtCore.QSize(16777215, 44))
        self.label_moving_speed.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_moving_speed.setAutoFillBackground(False)
        self.label_moving_speed.setObjectName("label_moving_speed")
        self.gridLayout.addWidget(self.label_moving_speed, 3, 0, 1, 1)
        self.layout_column_speed__ui_buttons = QtWidgets.QHBoxLayout()
        self.layout_column_speed__ui_buttons.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_column_speed__ui_buttons.setContentsMargins(-1, -1, -1, 0)
        self.layout_column_speed__ui_buttons.setObjectName("layout_column_speed__ui_buttons")
        self.button_speed_slowest = QtWidgets.QPushButton(self.centralwidget)
        self.button_speed_slowest.setObjectName("button_speed_slowest")
        self.layout_column_speed__ui_buttons.addWidget(self.button_speed_slowest)
        self.button_speed_slow = QtWidgets.QPushButton(self.centralwidget)
        self.button_speed_slow.setObjectName("button_speed_slow")
        self.layout_column_speed__ui_buttons.addWidget(self.button_speed_slow)
        self.button_speed_fast = QtWidgets.QPushButton(self.centralwidget)
        self.button_speed_fast.setObjectName("button_speed_fast")
        self.layout_column_speed__ui_buttons.addWidget(self.button_speed_fast)
        self.button_speed_fastest = QtWidgets.QPushButton(self.centralwidget)
        self.button_speed_fastest.setObjectName("button_speed_fastest")
        self.layout_column_speed__ui_buttons.addWidget(self.button_speed_fastest)
        self.gridLayout.addLayout(self.layout_column_speed__ui_buttons, 8, 0, 1, 1)
        self.step_slider = QtWidgets.QSlider(self.centralwidget)
        self.step_slider.setOrientation(QtCore.Qt.Horizontal)
        self.step_slider.setObjectName("step_slider")
        self.gridLayout.addWidget(self.step_slider, 6, 1, 1, 1)
        self.step_textbox = QtWidgets.QSpinBox(self.centralwidget)
        self.step_textbox.setObjectName("step_textbox")
        self.gridLayout.addWidget(self.step_textbox, 4, 1, 1, 1)
        self.xor_move_fluently = QtWidgets.QRadioButton(self.centralwidget)
        self.xor_move_fluently.setObjectName("xor_move_fluently")
        self.gridLayout.addWidget(self.xor_move_fluently, 2, 0, 1, 1)
        self.speed_slider = QtWidgets.QSlider(self.centralwidget)
        self.speed_slider.setMinimum(50)
        self.speed_slider.setMaximum(10000)
        self.speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider.setObjectName("speed_slider")
        self.gridLayout.addWidget(self.speed_slider, 6, 0, 1, 1)
        self.label_step_size = QtWidgets.QLabel(self.centralwidget)
        self.label_step_size.setObjectName("label_step_size")
        self.gridLayout.addWidget(self.label_step_size, 3, 1, 1, 1)
        self.speed_textbox = QtWidgets.QSpinBox(self.centralwidget)
        self.speed_textbox.setMinimum(50)
        self.speed_textbox.setMaximum(10000)
        self.speed_textbox.setObjectName("speed_textbox")
        self.gridLayout.addWidget(self.speed_textbox, 4, 0, 1, 1)
        self.xor_move_steps = QtWidgets.QRadioButton(self.centralwidget)
        self.xor_move_steps.setObjectName("xor_move_steps")
        self.gridLayout.addWidget(self.xor_move_steps, 2, 1, 1, 1)
        self.layout_rightside.addLayout(self.gridLayout)
        self.layout_grid_position = QtWidgets.QGridLayout()
        self.layout_grid_position.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.layout_grid_position.setObjectName("layout_grid_position")
        self.button_move_right = QtWidgets.QPushButton(self.centralwidget)
        self.button_move_right.setMinimumSize(QtCore.QSize(0, 60))
        self.button_move_right.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/arrow_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_move_right.setIcon(icon)
        self.button_move_right.setFlat(True)
        self.button_move_right.setObjectName("button_move_right")
        self.layout_grid_position.addWidget(self.button_move_right, 2, 2, 1, 1)
        self.button_move_left = QtWidgets.QPushButton(self.centralwidget)
        self.button_move_left.setMinimumSize(QtCore.QSize(0, 60))
        self.button_move_left.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("media/arrow_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_move_left.setIcon(icon1)
        self.button_move_left.setFlat(True)
        self.button_move_left.setObjectName("button_move_left")
        self.layout_grid_position.addWidget(self.button_move_left, 2, 0, 1, 1)
        self.button_move_down = QtWidgets.QPushButton(self.centralwidget)
        self.button_move_down.setMinimumSize(QtCore.QSize(0, 60))
        self.button_move_down.setWhatsThis("")
        self.button_move_down.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("media/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_move_down.setIcon(icon2)
        self.button_move_down.setFlat(True)
        self.button_move_down.setObjectName("button_move_down")
        self.layout_grid_position.addWidget(self.button_move_down, 3, 1, 1, 1)
        self.button_move_up = QtWidgets.QPushButton(self.centralwidget)
        self.button_move_up.setMinimumSize(QtCore.QSize(0, 60))
        self.button_move_up.setTabletTracking(False)
        self.button_move_up.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("media/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_move_up.setIcon(icon3)
        self.button_move_up.setCheckable(False)
        self.button_move_up.setFlat(True)
        self.button_move_up.setObjectName("button_move_up")
        self.layout_grid_position.addWidget(self.button_move_up, 1, 1, 1, 1)
        self.button_save_pos = QtWidgets.QPushButton(self.centralwidget)
        self.button_save_pos.setTabletTracking(False)
        self.button_save_pos.setToolTip("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("media/enter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_save_pos.setIcon(icon4)
        self.button_save_pos.setFlat(False)
        self.button_save_pos.setObjectName("button_save_pos")
        self.layout_grid_position.addWidget(self.button_save_pos, 2, 1, 1, 1)
        self.layout_rightside.addLayout(self.layout_grid_position)
        self.layout_grid_center.addLayout(self.layout_rightside, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1734, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuConnect = QtWidgets.QMenu(self.menubar)
        self.menuConnect.setObjectName("menuConnect")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionConnect_X = QtWidgets.QAction(MainWindow)
        self.actionConnect_X.setWhatsThis("")
        self.actionConnect_X.setObjectName("actionConnect_X")
        self.actionConnect_Y = QtWidgets.QAction(MainWindow)
        self.actionConnect_Y.setObjectName("actionConnect_Y")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuConnect.addSeparator()
        self.menuConnect.addAction(self.actionConnect_X)
        self.menuConnect.addAction(self.actionConnect_Y)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConnect.menuAction())

        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close)
        self.speed_slider.valueChanged['int'].connect(self.speed_textbox.setValue)
        self.speed_textbox.valueChanged['int'].connect(self.speed_slider.setValue)
        self.step_slider.valueChanged['int'].connect(self.step_textbox.setValue)
        self.step_textbox.valueChanged['int'].connect(self.step_slider.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIA - Shear Interferometer Automation"))
        __sortingEnabled = self.list_pos.isSortingEnabled()
        self.list_pos.setSortingEnabled(False)
        item = self.list_pos.item(0)
        item.setText(_translate("MainWindow", "Pos1"))
        item = self.list_pos.item(1)
        item.setText(_translate("MainWindow", "Delay (360s)"))
        item = self.list_pos.item(2)
        item.setText(_translate("MainWindow", "Pos2"))
        self.list_pos.setSortingEnabled(__sortingEnabled)
        self.button_delete_pos.setStatusTip(_translate("MainWindow", "Shortcut: del"))
        self.button_delete_pos.setText(_translate("MainWindow", "Delete Selected"))
        self.button_delete_pos.setShortcut(_translate("MainWindow", "Del"))
        self.label_delay.setText(_translate("MainWindow", "Seconds"))
        self.button_add_delay.setStatusTip(_translate("MainWindow", "Shortcut: D"))
        self.button_add_delay.setText(_translate("MainWindow", "Add Delay"))
        self.button_add_delay.setShortcut(_translate("MainWindow", "D"))
        self.label_repetitions.setText(_translate("MainWindow", "Repetitions"))
        self.button_start.setStatusTip(_translate("MainWindow", "Shortcut: Space"))
        self.button_start.setText(_translate("MainWindow", "Start"))
        self.button_start.setShortcut(_translate("MainWindow", "Space"))
        self.label_axis_settings.setText(_translate("MainWindow", "Axis Settings"))
        self.check_switchxy.setText(_translate("MainWindow", "Switch X Y"))
        self.check_reverse_y.setText(_translate("MainWindow", "Reverse Y"))
        self.check_reverse_x.setText(_translate("MainWindow", "Reverse X"))
        self.button_smallest.setText(_translate("MainWindow", "smallest"))
        self.button_small.setText(_translate("MainWindow", "small"))
        self.button_medium.setText(_translate("MainWindow", "medium"))
        self.button_big.setText(_translate("MainWindow", "big"))
        self.label_moving_speed.setText(_translate("MainWindow", "Moving Speed"))
        self.button_speed_slowest.setWhatsThis(_translate("MainWindow", "50hz "))
        self.button_speed_slowest.setText(_translate("MainWindow", "slowest"))
        self.button_speed_slow.setWhatsThis(_translate("MainWindow", "1kHz"))
        self.button_speed_slow.setText(_translate("MainWindow", "slow"))
        self.button_speed_fast.setWhatsThis(_translate("MainWindow", "5kHz"))
        self.button_speed_fast.setText(_translate("MainWindow", "fast"))
        self.button_speed_fastest.setWhatsThis(_translate("MainWindow", "10kHz"))
        self.button_speed_fastest.setText(_translate("MainWindow", "fastest"))
        self.xor_move_fluently.setText(_translate("MainWindow", "Move Fluently"))
        self.label_step_size.setText(_translate("MainWindow", "Step Size"))
        self.xor_move_steps.setText(_translate("MainWindow", "Move in Steps"))
        self.button_move_right.setShortcut(_translate("MainWindow", "Right"))
        self.button_move_left.setStatusTip(_translate("MainWindow", "Shortcut: Arrow Left"))
        self.button_move_left.setShortcut(_translate("MainWindow", "Left"))
        self.button_move_down.setStatusTip(_translate("MainWindow", "Shortcut: Arrow Down"))
        self.button_move_down.setShortcut(_translate("MainWindow", "Down"))
        self.button_move_up.setShortcut(_translate("MainWindow", "Up"))
        self.button_save_pos.setStatusTip(_translate("MainWindow", "Shortcut: Enter"))
        self.button_save_pos.setWhatsThis(_translate("MainWindow", "Save current position to list"))
        self.button_save_pos.setText(_translate("MainWindow", "Add Position"))
        self.button_save_pos.setShortcut(_translate("MainWindow", "Return"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuConnect.setTitle(_translate("MainWindow", "Connect"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save existing configuration"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create new configuration"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionConnect_X.setText(_translate("MainWindow", "Connect X"))
        self.actionConnect_Y.setText(_translate("MainWindow", "Connect Y"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
