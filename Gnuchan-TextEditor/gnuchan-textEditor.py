from cmath import exp
from importlib.resources import path
from optparse import Values
from unittest.mock import patch
import PySimpleGUI as sg
from pathlib import Path
import pathlib,  pickle, requests


#sg.popup(full_text)

def border(elem):
    return sg.Frame('', [[elem]], background_color='#0b011c')

sg.set_options(font="Sans 20")
sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {
                                        'BACKGROUND': '#240046',
                                        'TEXT': '#9d4edd',
                                        'INPUT': '#5a189a',
                                        'TEXT_INPUT': '#9d4edd',
                                        'SCROLL': '#5a189a',
                                        'BUTTON': ('#c77dff',  '#3c096c'),
                                        'PROGRESS': ('#c77dff', '#3c096c'),
                                        "MENU":("#c77dff"),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, 
                                            }
sg.theme("MyCreatedTheme")

cheat = """
burası kodlar için hile bölgesidir görmek için bir dosya aç







"""

python = """ python """
cLang  = """ c Lang """
welcome = """
---------------------------------------------------------------------------------------------------






---------------------------------------------------------------------------------------------------
"""



dictionary_file = 'dictionary.pickle'



if not pathlib.Path(dictionary_file).is_file():
    # Load dictionary from web if file not found
    try:
        url = "https://github.com/ArchKubi/PythonChan/blob/main/Gnuchan-TextEditor/python.txt"
        response = requests.get(url, allow_redirects=True)
        text = response.content.decode()
        dictionary = [word for word in text.splitlines() if word.isalpha()]
        # Save dictionary to file
        with open(dictionary_file, 'wb') as f:
            pickle.dump(dictionary, f)
    except:
        words = None
else:
    # Load dictionary from file
    with open(dictionary_file, 'rb') as f:
        dictionary = pickle.load(f)

width = max(map(len, dictionary))

Default = [

    [
    sg.Text("Welcome to GnuChan Text Editor", background_color="#19032e", expand_x=True,justification="center"),
    sg.Button("My Website", expand_x=True),
    sg.Button("My itch.io", expand_x=True)
    ],
##################################
    [
    border(sg.Image(filename="/home/archkubi/git/PythonChan/image/logo.png", expand_x=True, expand_y=True, background_color="#19032e")),
    sg.Text(welcome, expand_x=True)
    ], 
##################################
    [sg.Multiline(cheat,background_color="#18012e",expand_x=True,key="-CHEAT-",size=(900,900))]

        ]

Full_TextEditor = [
    [sg.Text("Welcome to GnuChan Text Editor", background_color="#19032e", expand_x=True,justification="center")],
    [sg.Button("Open", expand_x=True),sg.Button("Save", expand_x=True)],
    #[sg.Multiline(expand_x=True,expand_y=True, key="-TEXTBOX-",size=(900,900),background_color="#18012e")],
    
    [sg.Multiline('', size=(60, 20), key='MULTILINE'),
     sg.Listbox([], size=(width, 10), expand_y=True,expand_x=True, enable_events=True, key='LISTBOX')],


]

tab_group = [
    [
            sg.TabGroup
        (
            [[
            sg.Tab("Default", Default),
            sg.Tab("Text Editor",Full_TextEditor),
            sg.Button("Exit", expand_x=True),
            ]],

            tab_location="center",
            title_color="#9d4edd",
            tab_background_color="#5a189a",
            selected_title_color="#c77dff",
            selected_background_color="#240046"
        ),
    ]

]


window = sg.Window("Gnuchan Text Editor", tab_group, size=(1200,800),finalize=True, return_keyboard_events=True)
multiline = window['MULTILINE']
widget = multiline.widget
multiline.bind('<Key>', "+Key")
listbox = window['LISTBOX']



while True:
    event, values = window.Read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'MULTILINE+Key':
        entry = widget.get("insert-1c wordstart", "insert")
        if entry:
            words = [word for word in dictionary if word.startswith(entry)]
        else:
            words = []
        listbox.update(words)
    elif event == 'LISTBOX':
        items = values[event]
        if not items:
            continue
        widget.delete("insert-1c wordstart", "insert")
        widget.insert("insert", items[0])
        listbox.update([])
        multiline.set_focus()


    if event == "Open":
        file_path =  sg.popup_get_file("Open", no_window=True)
        if file_path:
            file = Path(file_path)
            window["MULTILINE"].update(file.read_text())

        if ".py" in file_path:
            window["-CHEAT-"].update(python)
        elif ".c" in file_path:
            window["-CHEAT-"].update(cLang)

    if event == "Save":
        file_path = sg.popup_get_file("Save", save_as=True, no_window=True)
        if file_path:
            file = Path(file_path)
            file.write_text(values["MULTILINE"])
        

    if event == "Exit":
        break



