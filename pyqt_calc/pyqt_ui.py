import sys

from PyQt5 import QtWidgets, uic


class Calculator:
    """ methods required in claculator app."""

    def __init__(self, equation_box):
        self.equation_box = equation_box

    def calculate(self):
        """ calcualte the result of the equation """
        eq_result = eval(self.equation_box.text())
        self.equation_box.setText(str(eq_result))


class Ui(QtWidgets.QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("calculator.ui", self)
        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = Ui()
    calculater = Calculator(window.equation_box)

    window.equal.clicked.connect(calculater.calculate)

    app.exec_()


if __name__ == "__main__":
    main()