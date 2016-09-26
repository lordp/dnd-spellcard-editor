import sys
from PySide import QtGui
import json

import dndui


class DNDApp(QtGui.QMainWindow, dndui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(DNDApp, self).__init__(parent)
        self.setupUi(self)

        self.spell_filename = ''

        self.spell_text.textChanged.connect(self.spell_text_content_changed)
        self.spell_list.currentIndexChanged.connect(self.display_spell)
        self.button_reset.clicked.connect(self.display_spell)

        self.actionLoad_Spells.triggered.connect(self.load_spells)
        self.actionSave_Spells.triggered.connect(self.save_spells)
        self.button_save.clicked.connect(self.update_spell)
        self.actionQuit.triggered.connect(self.close)

        self.spells = {}
        self.components = {
            "S": "somatic",
            "V": "verbal",
            "M": "material"
        }

    def spell_text_content_changed(self):
        length = len(self.spell_text.toPlainText())
        self.spell_text_length.setText('{0} of 600'.format(length))

    def load_spells(self):
        dialog = QtGui.QFileDialog(self)
        dialog.setNameFilter("JSON Files (*.json)")
        dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
        dialog.setDirectory('.')
        if dialog.exec_():
            self.spell_filename = dialog.selectedFiles()[0]
            with open(self.spell_filename) as json_data:
                self.spells = json.load(json_data)

            spell_names = sorted(list(self.spells.keys()))
            self.spell_list.addItems(spell_names)

            self.statusbar.showMessage('{0} spells loaded'.format(len(self.spells)), 2000)
        else:
            self.statusbar.showMessage('Failed to load spell list', 2000)

    def save_spells(self):
        if self.spell_filename is None:
            self.spell_filename = 'spells.json'

        with open(self.spell_filename, 'w') as fp:
            json.dump(self.spells, fp)

        self.statusbar.showMessage('{0} spells saved'.format(len(self.spells)), 2000)

    def update_spell(self):
        spell_name = self.spell_name.text()
        if spell_name in self.spells:
            selected = self.spells[spell_name]
        else:
            selected = {}
            self.spells[spell_name] = selected

        selected['classes'] = []
        for spell_class in self.group_classes.findChildren(QtGui.QCheckBox):
            if spell_class.isChecked():
                selected['classes'].append(spell_class.text())

        selected['level'] = int(self.spell_level.text())
        selected['school'] = self.spell_school.currentText()
        selected['ritual'] = str(self.spell_ritual.isChecked())

        selected['time'] = self.spell_casting_time.text()
        selected['duration'] = self.spell_duration.text()
        selected['range'] = self.spell_range.text()

        selected['components'] = []
        for spell_component in self.group_components.findChildren(QtGui.QCheckBox):
            if spell_component.isChecked():
                selected['components'].append(spell_component.text()[0])

        selected['material'] = self.text_materials.toPlainText()

        selected['source'] = self.source.currentText()
        selected['source_page'] = self.source_page.text()

        selected['text'] = self.spell_text.toPlainText()

        self.statusbar.showMessage('Spell updated', 2000)

    def display_spell(self):
        spell_name = self.spell_list.currentText()
        selected = self.spells[spell_name]

        self.spell_name.setText(spell_name)

        for spell_class in self.group_classes.findChildren(QtGui.QCheckBox):
            spell_class.setChecked(False)
        for spell_class in selected['classes']:
            class_checkbox = self.group_classes.findChild(QtGui.QCheckBox, 'class_{0}'.format(spell_class.lower()))
            if class_checkbox:
                class_checkbox.setChecked(True)

        self.spell_level.setText(str(selected['level']))
        spell_school = self.spell_school.findText(selected['school'])
        self.spell_school.setCurrentIndex(spell_school)
        self.spell_ritual.setChecked(bool(selected['ritual']))

        self.spell_casting_time.setText(selected['time'])
        self.spell_duration.setText(selected['duration'])
        self.spell_range.setText(selected['range'])

        for spell_component in self.group_components.findChildren(QtGui.QCheckBox):
            spell_component.setChecked(False)
        for spell_component in selected['components']:
            component_checkbox = self.group_components.findChild(QtGui.QCheckBox, 'component_{0}'.format(
                self.components[spell_component]
            ))
            if component_checkbox:
                component_checkbox.setChecked(True)

        self.text_materials.setPlainText(selected['material'])

        source = self.source.findText(selected['source'])
        self.source.setCurrentIndex(source)
        self.source_page.setText(str(selected['source_page']))

        self.spell_text.setPlainText(selected['text'])


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = DNDApp()
    window.show()
    app.exec_()
