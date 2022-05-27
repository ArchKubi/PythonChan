import PySimpleGUI as sg

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

layout = [
    [sg.Button("test")]

        ]

window = sg.Window("Gnuchan Calculator", layout)
while True:
    event, Value = window.read()
    if event == sg.WINDOW_CLOSED:
        break



