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
        MainWindow.resize(1423, 715)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.layout_grid_center = QtWidgets.QGridLayout(self.centralwidget)
        self.layout_grid_center.setObjectName("layout_grid_center")
        self.layout_leftside = QtWidgets.QVBoxLayout()
        self.layout_leftside.setObjectName("layout_leftside")
        self.button_delete_pos = QtWidgets.QPushButton(self.centralwidget)
        self.button_delete_pos.setObjectName("button_delete_pos")
        self.layout_leftside.addWidget(self.button_delete_pos)
        self.list_pos = QtWidgets.QListWidget(self.centralwidget)
        self.list_pos.setAcceptDrops(True)
        self.list_pos.setDragEnabled(True)
        self.list_pos.setDragDropOverwriteMode(False)
        self.list_pos.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.list_pos.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.list_pos.setAlternatingRowColors(True)
        self.list_pos.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.list_pos.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.list_pos.setViewMode(QtWidgets.QListView.ListMode)
        self.list_pos.setObjectName("list_pos")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../.designer/backup/media/waypoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.list_pos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../.designer/backup/media/clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.list_pos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_pos.addItem(item)
        self.layout_leftside.addWidget(self.list_pos)
        self.layout_delay = QtWidgets.QHBoxLayout()
        self.layout_delay.setObjectName("layout_delay")
        self.spinbox_delay_length = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinbox_delay_length.setMaximum(999999999.0)
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
        self.spacer_shear_api.setPixmap(QtGui.QPixmap("../../../../../../.designer/backup/media/shear.jpeg"))
        self.spacer_shear_api.setObjectName("spacer_shear_api")
        self.layout_grid_center.addWidget(self.spacer_shear_api, 0, 2, 1, 1)
        self.layout_rightside = QtWidgets.QVBoxLayout()
        self.layout_rightside.setObjectName("layout_rightside")
        self.layout_sia_logo_axis_settings = QtWidgets.QHBoxLayout()
        self.layout_sia_logo_axis_settings.setContentsMargins(-1, -1, -1, 20)
        self.layout_sia_logo_axis_settings.setObjectName("layout_sia_logo_axis_settings")
        self.layout_axis_settings = QtWidgets.QVBoxLayout()
        self.layout_axis_settings.setObjectName("layout_axis_settings")
        self.label_axis_settings = QtWidgets.QLabel(self.centralwidget)
        self.label_axis_settings.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_axis_settings.setFont(font)
        self.label_axis_settings.setObjectName("label_axis_settings")
        self.layout_axis_settings.addWidget(self.label_axis_settings)
        self.layou_buttonConnect = QtWidgets.QHBoxLayout()
        self.layou_buttonConnect.setObjectName("layou_buttonConnect")
        self.pushButton_connectX = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_connectX.setObjectName("pushButton_connectX")
        self.layou_buttonConnect.addWidget(self.pushButton_connectX)
        self.pushButton_connectY = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_connectY.setObjectName("pushButton_connectY")
        self.layou_buttonConnect.addWidget(self.pushButton_connectY)
        self.layout_axis_settings.addLayout(self.layou_buttonConnect)
        self.layout_comboBox = QtWidgets.QHBoxLayout()
        self.layout_comboBox.setObjectName("layout_comboBox")
        self.comboBox_x = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_x.setEditable(True)
        self.comboBox_x.setCurrentText("")
        self.comboBox_x.setObjectName("comboBox_x")
        self.layout_comboBox.addWidget(self.comboBox_x)
        self.comboBox_y = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_y.setEditable(True)
        self.comboBox_y.setObjectName("comboBox_y")
        self.layout_comboBox.addWidget(self.comboBox_y)
        self.layout_axis_settings.addLayout(self.layout_comboBox)
        self.layout_axis_settings_checkboxes = QtWidgets.QHBoxLayout()
        self.layout_axis_settings_checkboxes.setContentsMargins(-1, -1, -1, 0)
        self.layout_axis_settings_checkboxes.setObjectName("layout_axis_settings_checkboxes")
        self.check_switchxy = QtWidgets.QCheckBox(self.centralwidget)
        self.check_switchxy.setObjectName("check_switchxy")
        self.layout_axis_settings_checkboxes.addWidget(self.check_switchxy)
        self.check_reverse_y = QtWidgets.QCheckBox(self.centralwidget)
        self.check_reverse_y.setMinimumSize(QtCore.QSize(0, 0))
        self.check_reverse_y.setObjectName("check_reverse_y")
        self.layout_axis_settings_checkboxes.addWidget(self.check_reverse_y)
        self.check_reverse_x = QtWidgets.QCheckBox(self.centralwidget)
        self.check_reverse_x.setObjectName("check_reverse_x")
        self.layout_axis_settings_checkboxes.addWidget(self.check_reverse_x)
        self.layout_axis_settings.addLayout(self.layout_axis_settings_checkboxes)
        self.layout_sia_logo_axis_settings.addLayout(self.layout_axis_settings)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_sia = QtWidgets.QLabel(self.centralwidget)
        self.label_sia.setText("")
        self.label_sia.setPixmap(QtGui.QPixmap("../../../../../../.designer/backup/media/SIA.png"))
        self.label_sia.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sia.setObjectName("label_sia")
        self.verticalLayout.addWidget(self.label_sia)
        self.layout_sia_logo_axis_settings.addLayout(self.verticalLayout)
        self.layout_rightside.addLayout(self.layout_sia_logo_axis_settings)
        self.layout_movement_types = QtWidgets.QGridLayout()
        self.layout_movement_types.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.layout_movement_types.setContentsMargins(-1, -1, -1, 0)
        self.layout_movement_types.setObjectName("layout_movement_types")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_now = QtWidgets.QLabel(self.centralwidget)
        self.label_now.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_now.setFont(font)
        self.label_now.setObjectName("label_now")
        self.gridLayout.addWidget(self.label_now, 0, 0, 1, 1)
        self.label_next = QtWidgets.QLabel(self.centralwidget)
        self.label_next.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_next.setFont(font)
        self.label_next.setObjectName("label_next")
        self.gridLayout.addWidget(self.label_next, 0, 1, 1, 1)
        self.next = QtWidgets.QLabel(self.centralwidget)
        self.next.setMaximumSize(QtCore.QSize(16777215, 30))
        self.next.setObjectName("next")
        self.gridLayout.addWidget(self.next, 1, 1, 1, 1)
        self.now = QtWidgets.QLabel(self.centralwidget)
        self.now.setMaximumSize(QtCore.QSize(16777215, 30))
        self.now.setObjectName("now")
        self.gridLayout.addWidget(self.now, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(300, 0))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.label_measurement = QtWidgets.QLabel(self.centralwidget)
        self.label_measurement.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_measurement.setFont(font)
        self.label_measurement.setObjectName("label_measurement")
        self.verticalLayout_2.addWidget(self.label_measurement)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.number_cycles = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.number_cycles.setFont(font)
        self.number_cycles.setObjectName("number_cycles")
        self.horizontalLayout_3.addWidget(self.number_cycles)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.layout_movement_types.addLayout(self.verticalLayout_2, 4, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_step_size = QtWidgets.QLabel(self.centralwidget)
        self.label_step_size.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_step_size.setFont(font)
        self.label_step_size.setObjectName("label_step_size")
        self.verticalLayout_4.addWidget(self.label_step_size)
        self.step_slider = QtWidgets.QSlider(self.centralwidget)
        self.step_slider.setOrientation(QtCore.Qt.Horizontal)
        self.step_slider.setObjectName("step_slider")
        self.verticalLayout_4.addWidget(self.step_slider)
        self.step_textbox = QtWidgets.QSpinBox(self.centralwidget)
        self.step_textbox.setObjectName("step_textbox")
        self.verticalLayout_4.addWidget(self.step_textbox)
        self.layout_step_sizes = QtWidgets.QHBoxLayout()
        self.layout_step_sizes.setContentsMargins(-1, -1, -1, 20)
        self.layout_step_sizes.setObjectName("layout_step_sizes")
        self.button_smallest = QtWidgets.QPushButton(self.centralwidget)
        self.button_smallest.setObjectName("button_smallest")
        self.layout_step_sizes.addWidget(self.button_smallest)
        self.button_small = QtWidgets.QPushButton(self.centralwidget)
        self.button_small.setObjectName("button_small")
        self.layout_step_sizes.addWidget(self.button_small)
        self.button_medium = QtWidgets.QPushButton(self.centralwidget)
        self.button_medium.setObjectName("button_medium")
        self.layout_step_sizes.addWidget(self.button_medium)
        self.button_big = QtWidgets.QPushButton(self.centralwidget)
        self.button_big.setObjectName("button_big")
        self.layout_step_sizes.addWidget(self.button_big)
        self.verticalLayout_4.addLayout(self.layout_step_sizes)
        self.layout_movement_types.addLayout(self.verticalLayout_4, 4, 0, 1, 1)
        self.layout_rightside.addLayout(self.layout_movement_types)
        self.layout_arrowkeys = QtWidgets.QGridLayout()
        self.layout_arrowkeys.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.layout_arrowkeys.setObjectName("layout_arrowkeys")
        self.button_move_right = QtWidgets.QPushButton(self.centralwidget)
        self.button_move_right.setMinimumSize(QtCore.QSize(88, 60))
        self.button_move_right.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../.designer/backup/media/arrow_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_move_right.setIcon(icon2)
        self.button_move_right.setIconSize(QtCore.QSize(40, 40))
        self.button_move_right.setFlat(True)
        self.button_move_right.setObjectName("button_move_right")
        self.layout_arrowkeys.addWidget(self.button_move_right, 2, 2, 1, 1)
        self.button_move_left = QtWidgets.QPushButton(self.centralwidget)
        self.button_move_left.setMinimumSize(QtCore.QSize(88, 60))
        self.button_move_left.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../../../.designer/backup/media/arrow_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_move_left.setIcon(icon3)
        self.button_move_left.setIconSize(QtCore.QSize(40, 40))
        self.button_move_left.setFlat(True)
        self.button_move_left.setObjectName("button_move_left")
        self.layout_arrowkeys.addWidget(self.button_move_left, 2, 0, 1, 1)
        self.button_move_down = QtWidgets.QPushButton(self.centralwidget)
        self.button_move_down.setMinimumSize(QtCore.QSize(88, 60))
        self.button_move_down.setWhatsThis("")
        self.button_move_down.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../../../../.designer/backup/media/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_move_down.setIcon(icon4)
        self.button_move_down.setIconSize(QtCore.QSize(40, 40))
        self.button_move_down.setFlat(True)
        self.button_move_down.setObjectName("button_move_down")
        self.layout_arrowkeys.addWidget(self.button_move_down, 3, 1, 1, 1)
        self.button_move_up = QtWidgets.QPushButton(self.centralwidget)
        self.button_move_up.setMinimumSize(QtCore.QSize(88, 60))
        self.button_move_up.setTabletTracking(False)
        self.button_move_up.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../../../../../.designer/backup/media/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_move_up.setIcon(icon5)
        self.button_move_up.setIconSize(QtCore.QSize(40, 40))
        self.button_move_up.setCheckable(False)
        self.button_move_up.setFlat(True)
        self.button_move_up.setObjectName("button_move_up")
        self.layout_arrowkeys.addWidget(self.button_move_up, 1, 1, 1, 1)
        self.button_save_pos = QtWidgets.QPushButton(self.centralwidget)
        self.button_save_pos.setTabletTracking(False)
        self.button_save_pos.setToolTip("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../../../../../.designer/backup/media/enter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_save_pos.setIcon(icon6)
        self.button_save_pos.setIconSize(QtCore.QSize(40, 40))
        self.button_save_pos.setFlat(False)
        self.button_save_pos.setObjectName("button_save_pos")
        self.layout_arrowkeys.addWidget(self.button_save_pos, 2, 1, 1, 1)
        self.layout_rightside.addLayout(self.layout_arrowkeys)
        self.layout_grid_center.addLayout(self.layout_rightside, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1423, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
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
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close)
        self.step_slider.valueChanged['int'].connect(self.step_textbox.setValue)
        self.step_textbox.valueChanged['int'].connect(self.step_slider.setValue)
        self.button_delete_pos.clicked.connect(self.list_pos.clearSelection)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIA - Shear Interferometer Automation"))
        self.button_delete_pos.setStatusTip(_translate("MainWindow", "Shortcut: del"))
        self.button_delete_pos.setText(_translate("MainWindow", "Delete Selected"))
        self.button_delete_pos.setShortcut(_translate("MainWindow", "Del"))
        __sortingEnabled = self.list_pos.isSortingEnabled()
        self.list_pos.setSortingEnabled(False)
        item = self.list_pos.item(0)
        item.setText(_translate("MainWindow", "Pos1"))
        item = self.list_pos.item(1)
        item.setText(_translate("MainWindow", "Delay (360s)"))
        item = self.list_pos.item(2)
        item.setText(_translate("MainWindow", "Pos2"))
        self.list_pos.setSortingEnabled(__sortingEnabled)
        self.label_delay.setText(_translate("MainWindow", "Seconds"))
        self.button_add_delay.setStatusTip(_translate("MainWindow", "Shortcut: D"))
        self.button_add_delay.setText(_translate("MainWindow", "Add Delay"))
        self.button_add_delay.setShortcut(_translate("MainWindow", "D"))
        self.label_repetitions.setText(_translate("MainWindow", "Repetitions"))
        self.button_start.setStatusTip(_translate("MainWindow", "Shortcut: Space"))
        self.button_start.setText(_translate("MainWindow", "Start"))
        self.button_start.setShortcut(_translate("MainWindow", "Space"))
        self.label_axis_settings.setText(_translate("MainWindow", "Axis Settings"))
        self.pushButton_connectX.setText(_translate("MainWindow", "Connect X"))
        self.pushButton_connectY.setText(_translate("MainWindow", "Connect Y"))
        self.comboBox_x.setStatusTip(_translate("MainWindow", "Select Port of X Axis"))
        self.comboBox_y.setStatusTip(_translate("MainWindow", "Select Port of Y Axis"))
        self.check_switchxy.setText(_translate("MainWindow", "Switch X Y"))
        self.check_reverse_y.setText(_translate("MainWindow", "Reverse Y"))
        self.check_reverse_x.setText(_translate("MainWindow", "Reverse X"))
        self.label_now.setText(_translate("MainWindow", "Present Step"))
        self.label_next.setText(_translate("MainWindow", "Next Step"))
        self.next.setText(_translate("MainWindow", "TextLabel"))
        self.now.setText(_translate("MainWindow", "TextLabel"))
        self.label_measurement.setText(_translate("MainWindow", "Overall Progress"))
        self.label.setText(_translate("MainWindow", "Cycle"))
        self.number_cycles.setText(_translate("MainWindow", "0 of 12"))
        self.label_step_size.setText(_translate("MainWindow", "Step Size"))
        self.button_smallest.setText(_translate("MainWindow", "smallest"))
        self.button_small.setText(_translate("MainWindow", "small"))
        self.button_medium.setText(_translate("MainWindow", "medium"))
        self.button_big.setText(_translate("MainWindow", "big"))
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
