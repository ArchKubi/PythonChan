from cgitb import html
from cmath import exp
from importlib.resources import path
from optparse import Values
from platform import python_branch
from unittest.mock import patch
import PySimpleGUI as sg
from pathlib import Path
import pathlib,  pickle, requests
import python_book, C_Book, htmlBook, welcome
import subprocess, sys, os, readline



####################################################################################
#sg.popup(full_text)

def border(elem):
    return sg.Frame('', [[elem]], background_color='#0b011c')

font_size = 20
font_size_code = 15

font = ('Courier New', font_size)
font_code = ('Courier New', font_size_code)

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
####################################################################################


####################################################################################
cheat = """
this is language example place open file from text editor

Python : Print("Hello F... World BRUH")

C : #include <stdio.h>
    int main(){
            
        printf("Hello F... World BRUH")   
        return 0;
    }

"""

python = python_book.txt
cLang  = C_Book.Ctxt
htmlLang = htmlBook.htmTxt
welcome = welcome.welcomeTXT
####################################################################################

####################################################################################
url = "https://i.ibb.co/jZzSq6Q/logo.png"
response = requests.get(url, stream=True)
response.raw.decode_content = True
####################################################################################


####################################################################################
Default = [

    [sg.Text("Welcome to GnuChan Text Editor", background_color="#19032e", expand_x=True,justification="center",font=font),
     sg.Button("My Website", expand_x=True,font=font),
     sg.Button("My itch.io", expand_x=True,font=font)

    ],

    [border(sg.Image(data=response.raw.read(), expand_x=True, expand_y=True, background_color="#19032e")),
     sg.Text(welcome, expand_x=True,font=font)
    
    ], 

    [sg.Multiline(cheat,background_color="#18012e",expand_x=True,key="-CHEAT-",size=(900,900),font=font)]

        ]
####################################################################################


####################################################################################
### code editor 
dictionary_file = 'dictionary.pickle'
if not pathlib.Path(dictionary_file).is_file():
    # Load dictionary from web if file not found
    try:
        url = "https://raw.githubusercontent.com/ArchKubi/PythonChan/main/Gnuchan-TextEditor/python.txt"
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


Full_TextEditor = [
    [sg.Text("Welcome to GnuChan Text Editor", background_color="#19032e", expand_x=True,justification="center",font=font)],
    [sg.Button("Open", expand_x=True,font=font),sg.Button("Save",expand_x=True,font=font)],
    [sg.Multiline('', size=(3, 6), expand_y=True,font=font,background_color="#18012e"),
     sg.Multiline('', size=(102, 20), key='MULTILINE',expand_y=True,expand_x=True,font=font_size_code,no_scrollbar=True,background_color="#18012e"),
     sg.Listbox([], size=(15, 6), expand_y=True,expand_x=True,enable_events=True, key='LISTBOX',font=font,background_color="#18012e")
     
     ],
]
####################################################################################

####################################################################################
### Text editor

Full_TextEditor2 = [
    [sg.Text("Welcome to GnuChan Text Editor", background_color="#19032e", expand_x=True,justification="center",font=font)],
    [sg.Button("Open_Text", expand_x=True,font=font),sg.Button("Save_Text", expand_x=True,font=font)],
    [sg.Multiline('', size=(60, 20), key='MULTILINE2',expand_y=True,expand_x=True,enable_events=True,font=font_code,background_color="#18012e")],
]
####################################################################################


####################################################################################
### not work
pythonCodeRunner = [
    [sg.Text("Run Your Python Script", background_color="#19032e", expand_x=True,justification="center",font=font)],
    [sg.Button("Run Script", expand_x=True,font=font)],
    [sg.Multiline(expand_x=True,expand_y=True, key="-TEXTBOX-",size=(900,900),background_color="#18012e")],
]
####################################################################################



####################################################################################
#### Terminal
def runCommand(cmd, timeout=None, window=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.Refresh() if window else None   
    retval = p.wait(timeout)
    return (retval, output)                     


home = os.getcwd()
GnuChan_Terminal = [
    [sg.Text('This is GnuChan Terminal ---> ',font=font),sg.Text(home, font=font)],
    [sg.Input(key='_IN_',font=font,background_color="#18012e",expand_x=True),sg.Button('Run',font=font)],
    [sg.Output(size=(60,15),font=font_code,expand_x=True,expand_y=True,background_color="#18012e")],
                ]
####################################################################################


####################################################################################
tab_group = [
    [
            sg.TabGroup
        (
            [[
            sg.Tab("Default", Default),
            sg.Tab("Text",Full_TextEditor2),
            sg.Tab("Code Editor",Full_TextEditor),
            sg.Tab("Python Code Runner",pythonCodeRunner),
            sg.Tab("GnuChan Terminal",GnuChan_Terminal),
            sg.Button("Exit", expand_x=True,font=font),
            ]],

            tab_location="center",
            title_color="#9d4edd",
            tab_background_color="#370666",
            selected_title_color="#c77dff",
            selected_background_color="#240046",
            font=font
        ),
    ]
]
####################################################################################



####################################################################################
window = sg.Window("Gnuchan Text Editor", tab_group, size=(1200,800),finalize=True, return_keyboard_events=True)
window['_IN_'].bind("<Return>","_Enter")
multiline = window['MULTILINE']
widget = multiline.widget
multiline.bind('<Key>', "+Key")
listbox = window['LISTBOX']
tab = sg.Text.char_width_in_pixels(font_code)*1      # 4 spaces for a Tab
widget.configure(tabs=(tab,)) 
####################################################################################


####################################################################################
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
        elif ".html" in file_path:
            window["-CHEAT-"].update(htmlLang)

    if event == "Save":
        file_path = sg.popup_get_file("Save", save_as=True, no_window=True)
        if file_path:
            file = Path(file_path)
            file.write_text(values["MULTILINE"])

    if event == "Open_Text":
        file_path =  sg.popup_get_file("Open", no_window=True)
        if file_path:
            file = Path(file_path)
            window["MULTILINE2"].update(file.read_text())

    if event == "Save_Text":
        file_path = sg.popup_get_file("Save", save_as=True, no_window=True)
        if file_path:
            file = Path(file_path)
            file.write_text(values["MULTILINE2"])

    if event == 'Run':
        runCommand(cmd=values['_IN_'], window=window)
        window["_IN_"].update("")

    if event == "_IN_" + "_Enter":
        runCommand(cmd=values['_IN_'], window=window)
        window["_IN_"].update("")

    if event == "Exit":
        break
####################################################################################