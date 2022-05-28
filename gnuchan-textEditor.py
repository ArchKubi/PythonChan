from importlib.resources import path
from optparse import Values
from unittest.mock import patch
import PySimpleGUI as sg
from pathlib import Path

#sg.popup(full_text)

def border(elem):
    return sg.Frame('', [[elem]], background_color='#0b011c')

sg.set_options(font="Sans 20")
sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {
                                        'BACKGROUND': '#240046',
                                        'TEXT': '#9d4edd',
                                        'INPUT': '#18012e',
                                        'TEXT_INPUT': '#9d4edd',
                                        'SCROLL': '#5a189a',
                                        'BUTTON': ('#c77dff',  '#3c096c'),
                                        'PROGRESS': ('#c77dff', '#3c096c'),
                                        "MENU":("#19032e"),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, 
                                            }
sg.theme("MyCreatedTheme")

# menu_layout = [
#     ["File",["Open","Save","---","Exit"]],
#     ["Tools",["Word Count"]],
# ]

layout = [
    [sg.Text("Welcome to GnuChan Text Editor", background_color="#19032e", expand_x=True,justification="center")],
    [border(sg.Image(filename="/home/archkubi/git/PythonChan/image/logo.png", expand_x=True, expand_y=True, background_color="#19032e")),
    sg.Text("""---------------------------------------------------------------------------------------------------------
this is just test text



---------------------------------------------------------------------------------------------------------""",
background_color="#18012e", expand_x=True,expand_y=True)],
    [sg.Button("My Website", expand_x=True),sg.Button("My itch.io", expand_x=True),sg.Button("Open", expand_x=True),sg.Button("Save", expand_x=True),sg.Button("Exit", expand_x=True)],
    {sg.Text("untitled", key="-DOCNAME-")},
    [sg.Multiline(size=(80,15), key="-TEXTBOX-")]

        ]
window = sg.Window("Gnuchan Text Editor", layout)
while True:
    event, values = window.Read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Open":
       file_path =  sg.popup_get_file("Open", no_window=True)
       if file_path:
           file = Path(file_path)
           window["-TEXTBOX-"].update(file.read_text())
           window["-DOCNAME-"].update(file_path.split("/")[-1])

    if event == "Save":
        file_path = sg.popup_get_file("Save", save_as=True, no_window=True)
        file = Path(file_path)
        file.write_text(values["-TEXTBOX-"])
        window["-DOCNAME-"].update(file_path.split("/")[-1])
    if event == "Exit":
        break



