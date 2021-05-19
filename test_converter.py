from generated_layout import *

from text_converter import backend

import sys


class StringConverter(Ui_MainWindow):

    def __init__(self, window):
        self.setupUi(window)
        # direct the signal to a method of our app class
        self.pushButton.clicked.connect(self.button_item_name)
        self.pushButton_2.clicked.connect(self.button_all)

    def button_item_name(self):
        # takes the input from the text box
        user_input = self.plainTextEdit_1.toPlainText()
        user_input_modify = user_input.replace(", ", "|").replace(",", "|").replace('\n', '|').replace("  ", "|").replace(" ", "|")

        attribute_string = "AttributesContain["
        item_name_string = "item_name"

        end_syntax = attribute_string + item_name_string + ":" + user_input_modify + "]"

        print(end_syntax)

    def button_all(self):
        user_input = self.plainTextEdit_1.toPlainText()
        user_input_modify = user_input.replace(", ", "|").replace(",", "|").replace('\n', '|').replace("  ", "|").replace(" ", "|")

        attribute_string = "AttributesContain["
        item_name_string = "item_name"
        bullet_point_string = "bullet_point"
        product_description_string = "product_description"

        end_syntax = attribute_string + item_name_string + "|" + bullet_point_string + "|" + product_description_string + ":" + user_input_modify + "]"

        print(end_syntax)


# creates an application
app = QtWidgets.QApplication(sys.argv)
# creates a window
MainWindow = QtWidgets.QMainWindow()

# creates an instance of our class
ui = StringConverter(MainWindow)


# show window
MainWindow.show()
# run app
app.exec_()
