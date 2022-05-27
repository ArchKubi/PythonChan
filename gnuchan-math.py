import imp
import PySimpleGUI as sg
import webbrowser

def border(elem):
    return sg.Frame('', [[elem]], background_color='#0b011c')

sg.set_options(font="Sans 20")
sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {
                                        'BACKGROUND': '#240046',
                                        'TEXT': '#9d4edd',
                                        'INPUT': '#339966',
                                        'TEXT_INPUT': '#9d4edd',
                                        'SCROLL': '#5a189a',
                                        'BUTTON': ('#c77dff',  '#3c096c'),
                                        'PROGRESS': ('#c77dff', '#3c096c'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, 
                                            }


sg.theme("MyCreatedTheme")


output_X = "Output"

layout = [
    [   
        [sg.Text("Welcome to GnuChan Calculator", background_color="#19032e", expand_x=True,justification="center")],
        [border(sg.Image(size=(500,500), filename="/home/archkubi/git/PythonChan/image/logo.png", expand_x=True, expand_y=True, background_color="#19032e"))],
        [sg.Text("GnuChan Math For You: "),sg.Text(output_X, justification="center", expand_x=True, key = "-TEXT-", background_color="#3d0275")],
        [sg.Button(4),sg.Button(5),sg.Button(6),sg.Button(7),sg.Button(8),sg.Button(9)],
        [sg.Button(0),sg.Button(1),sg.Button(2),sg.Button(3),sg.Button("."),sg.Button("My Website", expand_x=True)],
        [sg.Button("+"),sg.Button("-"),sg.Button("*"),sg.Button("/"),sg.Button("%"),sg.Button("My itch.io", expand_x=True),sg.Button("Close", expand_x=True)],
        [sg.Button("Clear", expand_x=True),sg.Button("Enter", expand_x=True)],
    ]
        ]

window = sg.Window("Gnuchan Calculator", layout)

current_Number = []
operationList = []

while True:
    event, Value = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event in ["0","1","2","3","4","5","6","7","8","9","."]:
        current_Number.append(event)
        num_string = "".join(current_Number)
        window["-TEXT-"].update(num_string)
    if event in ["+","-","/","*","%"]:
        operationList.append("".join(current_Number))
        current_Number = []
        operationList.append(event)
        window["-TEXT-"].update("")
    if event == "Enter":
        operationList.append("".join(current_Number))
        result = eval("".join(operationList))
        window["-TEXT-"].update(result)
        operationList = []
    if event == "Clear":
        current_Number = []
        operationList = []
        window["-TEXT-"].update("")
    if event == "My Website":
        webbrowser.open("https://archkubi.github.io/")
    if event == "My itch.io":
        webbrowser.open("https://archkubi.itch.io/")
    if event == "Close":
        break





window.close()