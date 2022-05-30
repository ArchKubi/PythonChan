import PySimpleGUI as sg
import webbrowser, requests
from time import time

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


url = "https://i.ibb.co/jZzSq6Q/logo.png"
response = requests.get(url, stream=True)
response.raw.decode_content = True


def create_window():
    sg.theme("MyCreatedTheme")
    layout = [
            [sg.Text("Welcome to GnuChan Timer", background_color="#19032e", expand_x=True,justification="center")],
            [border(sg.Image(size=(350,350), data=response.raw.read(), expand_x=True, expand_y=True, background_color="#19032e"))],
            [sg.Text("0", key="-TIME-",background_color="#5a189a",expand_x=True),sg.VSeparator(),sg.Text("|GnuChan Help You|")],
            [sg.Button("Close"),sg.Button("Start", key = "-STARTSTOP-",expand_x=True),sg.Button("Lap", key="-LAP-", visible=False)],
            [sg.Button("My Website", expand_x=True), sg.Button("My itch.io", expand_x=True)],
            [sg.Button("Reset APP",expand_x=True)],
            [sg.Column([[]], key="-LAPS-",justification="center")]
            ]

        

    return sg.Window(
        "StopWatch",
        layout,        
    )
window = create_window()

lapse_amount = 0
start_time = 1
active = False

while True:
    event, Value = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, "Close"):
        break

    if event == "-STARTSTOP-":
        if active:
            active = False
            window["-STARTSTOP-"].update("Reset")
            window["-LAP-"].update(visible = False)
        else:
            start_time = time()
            active = True
            window["-STARTSTOP-"].update("Stop")
            window["-LAP-"].update(visible = True)
 
    if active:
        elapsed_time = round(time() - start_time,1)
        window["-TIME-"].update(elapsed_time)
    if event == "-LAP-":
        window.extend_layout(window["-LAPS-"], [[sg.Text(lapse_amount),sg.VSeparator(),sg.Text(elapsed_time)]])
        lapse_amount += 1
    if event == "Reset APP":
        window.close()
        window = create_window()
        active = False
        start_time = 0
        lapse_amount = 1
    if event == "My Website":
        webbrowser.open("https://archkubi.github.io/")
    if event == "My itch.io":
        webbrowser.open("https://archkubi.itch.io/")

window.close()


