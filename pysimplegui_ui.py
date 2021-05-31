# Build calculator application with pysimplegui
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import InputText

sg.theme("DarkAmber")  # Add a touch of color
# All the stuff inside your window.

equal_pressd = False


def clear_all(event):
    window["inputbox"].update(value="")


def clear_one(event):
    calcbox = window["inputbox"]
    box_val = calcbox.get()
    calcbox.update(value=box_val[:-1])


def on_number(event):
    global equal_pressd

    if equal_pressd:
        clear_all(event)
        equal_pressd = False

    calcbox = window["inputbox"]
    old_val = calcbox.get()
    calcbox.update(value=old_val + event)


def on_operator(event):
    global equal_pressd
    if window["inputbox"].get() == "":
        return
    equal_pressd = False
    calcbox = window["inputbox"]
    old_val = calcbox.get()
    calcbox.update(value=old_val + event)


def on_equal(event):
    global equal_pressd
    equal_pressd = True
    calcbox = window["inputbox"]
    equation = calcbox.get()
    try:
        calcbox.update(value=eval(equation))
    except ZeroDivisionError:
        calcbox.update(value="Zero Divison Error")
    except Exception as e:
        calcbox.update(value=e)


layout = [
    [sg.InputText(key="inputbox")],
    [sg.Button(item) for item in ["C", "CC", "%", "/"]],
    [sg.Button(item) for item in ["9", "8", "7", "*"]],
    [sg.Button(item) for item in ["6", "5", "4", "-"]],
    [sg.Button(item) for item in ["3", "2", "1", "+"]],
    [sg.Button(item) for item in ["0", ".", "="]],
]

# Create the Window
window = sg.Window("PySimpleGUI Calculator", layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event in [str(i) for i in range(9)]:
        on_number(event)
    if event in ["+", "-", "*", "/", "%"]:
        on_operator(event)
    if event == "=":
        on_equal(event)
    if event == "CC":
        clear_all(event)
    if event == "C":
        clear_one(event)
window.close()
