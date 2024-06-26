from PyQt5 import QtCore, QtGui, QtWidgets
from googletrans import Translator, LANGCODES, LANGUAGES
import os

translator = Translator()
language_codes = {
    "Nepali": "ne",
    "Indian": "hi",
    "English (UK)": "en",
    "English (US)": "en",
    "Spanish": "es",
    "Chinese (Simplified)": "zh-cn",
    "Chinese (Traditional)": "zh-tw",
    "Japanese": "ja",
}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(
            "#language_select { padding: 10px;}\n"
            "#filename_input {padding: 10px;}\n"
            "#status {\n"
            "    pading: 10px;\n"
            "}"
        )
        self.mainVerticleWidget = QtWidgets.QWidget(MainWindow)
        self.mainVerticleWidget.setObjectName("mainVerticleWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainVerticleWidget)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.inputHorizontalWidget = QtWidgets.QHBoxLayout()
        self.inputHorizontalWidget.setSpacing(2)
        self.inputHorizontalWidget.setObjectName("inputHorizontalWidget")

        self.filename_input = QtWidgets.QLineEdit(self.mainVerticleWidget)
        self.filename_input.setMinimumSize(QtCore.QSize(0, 40))
        self.filename_input.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.filename_input.setFont(font)
        self.filename_input.setObjectName("filename_input")
        self.inputHorizontalWidget.addWidget(self.filename_input)

        self.language_select = QtWidgets.QComboBox(self.mainVerticleWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.language_select.sizePolicy().hasHeightForWidth()
        )
        self.language_select.setSizePolicy(sizePolicy)
        self.language_select.setMinimumSize(QtCore.QSize(150, 40))
        self.language_select.setMaximumSize(QtCore.QSize(150, 40))
        self.language_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.language_select.setObjectName("language_select")
        self.language_select.addItem("")
        self.language_select.addItem("")
        self.language_select.addItem("")
        self.language_select.addItem("")
        self.language_select.addItem("")
        self.language_select.addItem("")
        self.language_select.addItem("")
        self.language_select.addItem("")
        self.inputHorizontalWidget.addWidget(self.language_select)

        self.translate_button = QtWidgets.QPushButton(self.mainVerticleWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.translate_button.sizePolicy().hasHeightForWidth()
        )
        self.translate_button.setSizePolicy(sizePolicy)
        self.translate_button.setMinimumSize(QtCore.QSize(95, 40))
        self.translate_button.setMaximumSize(QtCore.QSize(95, 40))
        self.translate_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.translate_button.setObjectName("translate_button")
        self.inputHorizontalWidget.addWidget(self.translate_button)
        self.translate_button.clicked.connect(self.handleTranslateBtn)

        self.verticalLayout.addLayout(self.inputHorizontalWidget)

        self.text_box_area = QtWidgets.QTextEdit(self.mainVerticleWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.text_box_area.setFont(font)
        self.text_box_area.setAutoFormatting(
            QtWidgets.QTextEdit.AutoFormattingFlag.AutoNone
        )
        self.text_box_area.setMarkdown("")
        self.text_box_area.setTabStopDistance(25.0)
        self.text_box_area.document().setDocumentMargin(10)
        self.text_box_area.textChanged.connect(self.keypressEvent)
        self.text_box_area.setObjectName("text_box_area")
        self.verticalLayout.addWidget(self.text_box_area)

        MainWindow.setCentralWidget(self.mainVerticleWidget)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def keypressEvent(self):
        if self.text_box_area.toPlainText():
            self.translate_button.setText("Translate")
        else:
            self.translate_button.setText("Open File")

    def handleTranslateBtn(self):
        button_text = self.translate_button.text()
        match button_text:
            case "Open File":
                options = QtWidgets.QFileDialog.Options()
                options |= QtWidgets.QFileDialog.ReadOnly
                filename, _ = QtWidgets.QFileDialog.getOpenFileName(
                    None,
                    "Choose File",
                    "",
                    "All Files (*);;Text Files(*.txt)",
                    options=options,
                )
                if filename:
                    with open(filename) as file:
                        self.text_box_area.setText(file.read())
                        self.filename_input.setText(filename)
            case "Translate":
                filename = self.filename_input.text()
                filename, _ = os.path.splitext(filename)
                
                dest = self.language_select.currentText()
                language_code = language_codes.get(dest)
                content = self.text_box_area.toPlainText()
                
                print(language_code)

                translation = str(translator.translate(content, src="auto", dest=language_code).text)
                print(translation)

                try:
                    with open(filename + "-translated.txt", "w") as file:
                        file.write(translation)
                except UnicodeEncodeError:
                    with open(filename + "-translated.txt", "wb") as file:
                        file.write(translation.encode())
                finally:
                    self.text_box_area.setText(translation)
            case _:
                print("Invalid Match")

    def addSelectLabels(self):
        _translate = QtCore.QCoreApplication.translate

        languages = [
            "Nepali",
            "Indian",
            "English (UK)",
            "English (US)",
            "Spanish",
            "Chinese (Simplified)",
            "Chinese (Traditional)",
            "Japanese",
        ]
        for index, language in enumerate(languages):
            self.language_select.setItemText(index, _translate("MainWindow", language))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translator"))
        self.filename_input.setPlaceholderText(_translate("MainWindow", "Filename"))
        self.language_select.setCurrentText(_translate("MainWindow", "Nepali"))
        self.language_select.setPlaceholderText(_translate("MainWindow", "Language"))
        self.addSelectLabels()
        self.translate_button.setText(_translate("MainWindow", "Open File"))
        self.text_box_area.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Verdana'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.text_box_area.setPlaceholderText(
            _translate("MainWindow", "Enter to text to Translate")
        )
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
