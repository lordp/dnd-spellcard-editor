# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dndapp.ui'
#
# Created: Mon Sep 26 16:55:18 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 570)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.group_classes = QtGui.QGroupBox(self.centralwidget)
        self.group_classes.setGeometry(QtCore.QRect(10, 70, 291, 111))
        self.group_classes.setObjectName("group_classes")
        self.class_bard = QtGui.QCheckBox(self.group_classes)
        self.class_bard.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.class_bard.setObjectName("class_bard")
        self.class_cleric = QtGui.QCheckBox(self.group_classes)
        self.class_cleric.setGeometry(QtCore.QRect(20, 40, 70, 17))
        self.class_cleric.setObjectName("class_cleric")
        self.class_druid = QtGui.QCheckBox(self.group_classes)
        self.class_druid.setGeometry(QtCore.QRect(20, 60, 70, 17))
        self.class_druid.setObjectName("class_druid")
        self.class_fighter = QtGui.QCheckBox(self.group_classes)
        self.class_fighter.setGeometry(QtCore.QRect(20, 80, 70, 17))
        self.class_fighter.setObjectName("class_fighter")
        self.class_paladin = QtGui.QCheckBox(self.group_classes)
        self.class_paladin.setGeometry(QtCore.QRect(120, 20, 70, 17))
        self.class_paladin.setObjectName("class_paladin")
        self.class_ranger = QtGui.QCheckBox(self.group_classes)
        self.class_ranger.setGeometry(QtCore.QRect(120, 40, 70, 17))
        self.class_ranger.setObjectName("class_ranger")
        self.class_sorcerer = QtGui.QCheckBox(self.group_classes)
        self.class_sorcerer.setGeometry(QtCore.QRect(120, 80, 70, 17))
        self.class_sorcerer.setObjectName("class_sorcerer")
        self.class_wizard = QtGui.QCheckBox(self.group_classes)
        self.class_wizard.setGeometry(QtCore.QRect(220, 20, 70, 17))
        self.class_wizard.setObjectName("class_wizard")
        self.class_warlock = QtGui.QCheckBox(self.group_classes)
        self.class_warlock.setGeometry(QtCore.QRect(220, 40, 70, 17))
        self.class_warlock.setObjectName("class_warlock")
        self.class_rogue = QtGui.QCheckBox(self.group_classes)
        self.class_rogue.setGeometry(QtCore.QRect(120, 60, 70, 17))
        self.class_rogue.setObjectName("class_rogue")
        self.label_spell_name = QtGui.QLabel(self.centralwidget)
        self.label_spell_name.setGeometry(QtCore.QRect(10, 40, 60, 20))
        self.label_spell_name.setObjectName("label_spell_name")
        self.spell_name = QtGui.QLineEdit(self.centralwidget)
        self.spell_name.setGeometry(QtCore.QRect(80, 40, 221, 20))
        self.spell_name.setObjectName("spell_name")
        self.label_spell_level = QtGui.QLabel(self.centralwidget)
        self.label_spell_level.setGeometry(QtCore.QRect(10, 190, 71, 20))
        self.label_spell_level.setObjectName("label_spell_level")
        self.spell_school = QtGui.QComboBox(self.centralwidget)
        self.spell_school.setGeometry(QtCore.QRect(128, 190, 111, 20))
        self.spell_school.setObjectName("spell_school")
        self.spell_school.addItem("")
        self.spell_school.addItem("")
        self.spell_school.addItem("")
        self.spell_school.addItem("")
        self.spell_school.addItem("")
        self.spell_school.addItem("")
        self.spell_school.addItem("")
        self.spell_school.addItem("")
        self.spell_level = QtGui.QLineEdit(self.centralwidget)
        self.spell_level.setGeometry(QtCore.QRect(80, 190, 41, 20))
        self.spell_level.setObjectName("spell_level")
        self.spell_ritual = QtGui.QCheckBox(self.centralwidget)
        self.spell_ritual.setGeometry(QtCore.QRect(249, 190, 51, 20))
        self.spell_ritual.setObjectName("spell_ritual")
        self.spell_casting_time = QtGui.QLineEdit(self.centralwidget)
        self.spell_casting_time.setGeometry(QtCore.QRect(80, 220, 221, 20))
        self.spell_casting_time.setObjectName("spell_casting_time")
        self.label_casting_time = QtGui.QLabel(self.centralwidget)
        self.label_casting_time.setGeometry(QtCore.QRect(10, 220, 61, 20))
        self.label_casting_time.setObjectName("label_casting_time")
        self.label_duration = QtGui.QLabel(self.centralwidget)
        self.label_duration.setGeometry(QtCore.QRect(10, 250, 61, 20))
        self.label_duration.setObjectName("label_duration")
        self.spell_duration = QtGui.QLineEdit(self.centralwidget)
        self.spell_duration.setGeometry(QtCore.QRect(80, 250, 221, 20))
        self.spell_duration.setObjectName("spell_duration")
        self.spell_range = QtGui.QLineEdit(self.centralwidget)
        self.spell_range.setGeometry(QtCore.QRect(80, 280, 221, 20))
        self.spell_range.setObjectName("spell_range")
        self.label_range = QtGui.QLabel(self.centralwidget)
        self.label_range.setGeometry(QtCore.QRect(10, 280, 61, 20))
        self.label_range.setObjectName("label_range")
        self.group_components = QtGui.QGroupBox(self.centralwidget)
        self.group_components.setGeometry(QtCore.QRect(10, 310, 291, 151))
        self.group_components.setObjectName("group_components")
        self.component_somatic = QtGui.QCheckBox(self.group_components)
        self.component_somatic.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.component_somatic.setObjectName("component_somatic")
        self.component_verbal = QtGui.QCheckBox(self.group_components)
        self.component_verbal.setGeometry(QtCore.QRect(210, 20, 70, 17))
        self.component_verbal.setObjectName("component_verbal")
        self.component_material = QtGui.QCheckBox(self.group_components)
        self.component_material.setGeometry(QtCore.QRect(110, 20, 70, 17))
        self.component_material.setObjectName("component_material")
        self.text_materials = QtGui.QPlainTextEdit(self.group_components)
        self.text_materials.setGeometry(QtCore.QRect(10, 70, 271, 71))
        self.text_materials.setObjectName("text_materials")
        self.label_materials = QtGui.QLabel(self.group_components)
        self.label_materials.setGeometry(QtCore.QRect(10, 50, 271, 20))
        self.label_materials.setAlignment(QtCore.Qt.AlignCenter)
        self.label_materials.setObjectName("label_materials")
        self.label_source = QtGui.QLabel(self.centralwidget)
        self.label_source.setGeometry(QtCore.QRect(10, 470, 47, 20))
        self.label_source.setObjectName("label_source")
        self.label_page = QtGui.QLabel(self.centralwidget)
        self.label_page.setGeometry(QtCore.QRect(190, 470, 47, 20))
        self.label_page.setObjectName("label_page")
        self.source = QtGui.QComboBox(self.centralwidget)
        self.source.setGeometry(QtCore.QRect(50, 470, 131, 20))
        self.source.setObjectName("source")
        self.source.addItem("")
        self.source.addItem("")
        self.source_page = QtGui.QLineEdit(self.centralwidget)
        self.source_page.setGeometry(QtCore.QRect(220, 470, 81, 20))
        self.source_page.setObjectName("source_page")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(320, 40, 3, 450))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.spell_text = QtGui.QPlainTextEdit(self.centralwidget)
        self.spell_text.setGeometry(QtCore.QRect(340, 69, 291, 400))
        self.spell_text.setObjectName("spell_text")
        self.spell_text_length = QtGui.QLabel(self.centralwidget)
        self.spell_text_length.setGeometry(QtCore.QRect(556, 470, 71, 20))
        self.spell_text_length.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spell_text_length.setObjectName("spell_text_length")
        self.button_save = QtGui.QPushButton(self.centralwidget)
        self.button_save.setGeometry(QtCore.QRect(560, 500, 75, 30))
        self.button_save.setObjectName("button_save")
        self.button_reset = QtGui.QPushButton(self.centralwidget)
        self.button_reset.setGeometry(QtCore.QRect(480, 500, 75, 30))
        self.button_reset.setObjectName("button_reset")
        self.label_spell_text = QtGui.QLabel(self.centralwidget)
        self.label_spell_text.setGeometry(QtCore.QRect(340, 40, 47, 20))
        self.label_spell_text.setObjectName("label_spell_text")
        self.spell_list = QtGui.QComboBox(self.centralwidget)
        self.spell_list.setGeometry(QtCore.QRect(10, 10, 630, 20))
        self.spell_list.setObjectName("spell_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Spells = QtGui.QAction(MainWindow)
        self.actionLoad_Spells.setObjectName("actionLoad_Spells")
        self.actionSave_Spells = QtGui.QAction(MainWindow)
        self.actionSave_Spells.setObjectName("actionSave_Spells")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionLoad_Spells)
        self.menuFile.addAction(self.actionSave_Spells)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "D&D Spell Card Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.group_classes.setTitle(QtGui.QApplication.translate("MainWindow", "Classes", None, QtGui.QApplication.UnicodeUTF8))
        self.class_bard.setText(QtGui.QApplication.translate("MainWindow", "Bard", None, QtGui.QApplication.UnicodeUTF8))
        self.class_cleric.setText(QtGui.QApplication.translate("MainWindow", "Cleric", None, QtGui.QApplication.UnicodeUTF8))
        self.class_druid.setText(QtGui.QApplication.translate("MainWindow", "Druid", None, QtGui.QApplication.UnicodeUTF8))
        self.class_fighter.setText(QtGui.QApplication.translate("MainWindow", "Fighter", None, QtGui.QApplication.UnicodeUTF8))
        self.class_paladin.setText(QtGui.QApplication.translate("MainWindow", "Paladin", None, QtGui.QApplication.UnicodeUTF8))
        self.class_ranger.setText(QtGui.QApplication.translate("MainWindow", "Ranger", None, QtGui.QApplication.UnicodeUTF8))
        self.class_sorcerer.setText(QtGui.QApplication.translate("MainWindow", "Sorcerer", None, QtGui.QApplication.UnicodeUTF8))
        self.class_wizard.setText(QtGui.QApplication.translate("MainWindow", "Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.class_warlock.setText(QtGui.QApplication.translate("MainWindow", "Warlock", None, QtGui.QApplication.UnicodeUTF8))
        self.class_rogue.setText(QtGui.QApplication.translate("MainWindow", "Rogue", None, QtGui.QApplication.UnicodeUTF8))
        self.label_spell_name.setText(QtGui.QApplication.translate("MainWindow", "Spell Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_spell_level.setText(QtGui.QApplication.translate("MainWindow", "Level / School", None, QtGui.QApplication.UnicodeUTF8))
        self.spell_school.setItemText(0, QtGui.QApplication.translate("MainWindow", "Abjuration", None, QtGui.QApplication.UnicodeUTF8))
        self.spell_school.setItemText(1, QtGui.QApplication.translate("MainWindow", "Conjuration", None, QtGui.QApplication.UnicodeUTF8))
        self.spell_school.setItemText(2, QtGui.QApplication.translate("MainWindow", "Divination", None, QtGui.QApplication.UnicodeUTF8))
        self.spell_school.setItemText(3, QtGui.QApplication.translate("MainWindow", "Enchantment", None, QtGui.QApplication.UnicodeUTF8))
        self.spell_school.setItemText(4, QtGui.QApplication.translate("MainWindow", "Evocation", None, QtGui.QApplication.UnicodeUTF8))
        self.spell_school.setItemText(5, QtGui.QApplication.translate("MainWindow", "lllusion", None, QtGui.QApplication.UnicodeUTF8))
        self.spell_school.setItemText(6, QtGui.QApplication.translate("MainWindow", "Necromancy", None, QtGui.QApplication.UnicodeUTF8))
        self.spell_school.setItemText(7, QtGui.QApplication.translate("MainWindow", "Transmutation", None, QtGui.QApplication.UnicodeUTF8))
        self.spell_ritual.setText(QtGui.QApplication.translate("MainWindow", "Ritual", None, QtGui.QApplication.UnicodeUTF8))
        self.label_casting_time.setText(QtGui.QApplication.translate("MainWindow", "Casting Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_duration.setText(QtGui.QApplication.translate("MainWindow", "Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_range.setText(QtGui.QApplication.translate("MainWindow", "Range", None, QtGui.QApplication.UnicodeUTF8))
        self.group_components.setTitle(QtGui.QApplication.translate("MainWindow", "Components", None, QtGui.QApplication.UnicodeUTF8))
        self.component_somatic.setText(QtGui.QApplication.translate("MainWindow", "Somatic", None, QtGui.QApplication.UnicodeUTF8))
        self.component_verbal.setText(QtGui.QApplication.translate("MainWindow", "Verbal", None, QtGui.QApplication.UnicodeUTF8))
        self.component_material.setText(QtGui.QApplication.translate("MainWindow", "Material", None, QtGui.QApplication.UnicodeUTF8))
        self.label_materials.setText(QtGui.QApplication.translate("MainWindow", "Materials", None, QtGui.QApplication.UnicodeUTF8))
        self.label_source.setText(QtGui.QApplication.translate("MainWindow", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.label_page.setText(QtGui.QApplication.translate("MainWindow", "Page", None, QtGui.QApplication.UnicodeUTF8))
        self.source.setItemText(0, QtGui.QApplication.translate("MainWindow", "Player\'s Handbook", None, QtGui.QApplication.UnicodeUTF8))
        self.source.setItemText(1, QtGui.QApplication.translate("MainWindow", "Elemental Evil", None, QtGui.QApplication.UnicodeUTF8))
        self.spell_text_length.setText(QtGui.QApplication.translate("MainWindow", "0 / 600", None, QtGui.QApplication.UnicodeUTF8))
        self.button_save.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.button_reset.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_spell_text.setText(QtGui.QApplication.translate("MainWindow", "Spell Text", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Spells.setText(QtGui.QApplication.translate("MainWindow", "Load Spells", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Spells.setText(QtGui.QApplication.translate("MainWindow", "Save Spells", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
