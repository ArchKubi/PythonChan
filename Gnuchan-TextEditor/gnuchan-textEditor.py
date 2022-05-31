import PySimpleGUI as sg
from pathlib import Path
import pathlib,  pickle, requests, subprocess, sys, os
import python_book, C_Book, htmlBook, welcome





####################################################################################
#sg.popup(full_text)

def border(elem):
    return sg.Frame('', [[elem]], background_color='#0b011c')

font_size = 20
font_size_code = 15
font_bSize = 17
font_output = 25

font = ('Courier New', font_size)
font_code = ('Courier New', font_size_code)
font_bSizeFo = ('Courier New', font_bSize)
font_bOutput = ('Courier New', font_output)

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
don't use like this:
while True:
    print("fBom")
not working editor freezes
input() nope not working

range works normal

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
#### starting screen
Default = [

    [sg.Text("Welcome to GnuChan Text Editor", background_color="#19032e", expand_x=True,justification="center",font=font),
     sg.Button("My Website", expand_x=True,font=font),
     sg.Button("My itch.io", expand_x=True,font=font)

    ],

    [border(sg.Image(data=response.raw.read(), expand_x=True, expand_y=True, background_color="#19032e")),
     sg.Text(welcome, expand_x=True,font=font)
    
    ], 

    [sg.Multiline(cheat,background_color="#18012e",expand_x=True,key="-CHEAT-",size=(900,900),font=font_bSizeFo,no_scrollbar=True)]

        ]
####################################################################################


####################################################################################
#### code editor 
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
    [sg.Button("Open", expand_x=True,font=font),sg.Button("Save",expand_x=True,font=font),sg.Button("Save As",expand_x=True,font=font)],
    [sg.Multiline("",size=(5, 6),expand_x=True,expand_y=True,background_color="#18012e",font=font_code,no_scrollbar=True),
     sg.Multiline('', size=(85, 20), key='MULTILINE',expand_y=True,expand_x=True,font=font_code,no_scrollbar=True,background_color="#18012e"),
     sg.Listbox([], size=(7, 6), expand_y=True,expand_x=True,enable_events=True, key='LISTBOX',font=font,background_color="#18012e",no_scrollbar=True)
     
     ],
]
####################################################################################

####################################################################################
#### Text editor

Full_TextEditor2 = [
    [sg.Button("Open Text", expand_x=True,font=font),sg.Button("Save Text", expand_x=True,font=font),sg.Button("Save As Text", expand_x=True,font=font_code)],
    [sg.Multiline('', size=(60, 20), key='MULTILINE2',expand_y=True,expand_x=True,enable_events=True,font=font_code,background_color="#18012e")],
]
####################################################################################


####################################################################################
#### Run Python Script
def runScript():

    command = f'python {file}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,universal_newlines=True)
    outputResult, error = process.communicate()

    if "Error" in error:
        window["OutputX"].update(error)
    else:
        window["OutputX"].update(outputResult)



    
pythonCodeRunner = [
    [sg.Text("Run Your Python Script", background_color="#19032e", expand_x=True,justification="center",font=font)],
    [sg.Button("Run Script", expand_x=True,font=font)],
    [sg.Output(size=(60,15),font=font_bOutput,expand_x=True,expand_y=True,background_color="#18012e",key="OutputX")],
]
####################################################################################


####################################################################################
#### Terminal
def runCommand(cmd, timeout=None, window=None):
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.Refresh() if window else None   
    retval = p.wait(timeout)
    return (retval, output)                     


GnuChan_Terminal = [
    [sg.Text("'| GnuChan Terminal | This is  Not InterActive Terminal |'",font=font,expand_x=True,justification="center")],
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
            font=font,
            key="Status"
            
        ),
    ]
]
####################################################################################



####################################################################################
window = sg.Window("Gnuchan Text Editor",tab_group,finalize=True,return_keyboard_events=True,resizable=True)
window['_IN_'].bind("<Return>","_Enter")
window.bind('<Configure>', "Configure")
status = window['Status']


multiline = window['MULTILINE']
widget = multiline.widget
multiline.bind('<Key>', "+Key")
listbox = window['LISTBOX']

text = window['MULTILINE'].Widget
text.configure(undo=True)
text.bind('<Control-Shift-Key-Z>', lambda event, text=text:redo(event, text))



tab = sg.Text.char_width_in_pixels(font_code)*3
widget.configure(tabs=(tab,)) 

lapse_amount = 0
script_open = False
txt_open = False
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
            script_open = True

        if ".py" in file_path:
            window["-CHEAT-"].update(python)
        elif ".c" in file_path:
            window["-CHEAT-"].update(cLang)
        elif ".html" in file_path:
            window["-CHEAT-"].update(htmlLang)

    if event == "Save As":
        file_path = sg.popup_get_file("Save", save_as=True, no_window=True)
        if file_path:
            file = Path(file_path)
            file.write_text(values["MULTILINE"])
    if event == "Save" and script_open == True:
        if file_path:
            file = Path(file_path)
            file.write_text(values["MULTILINE"])
        else:
            pass

    if event == "Open Text":
        file_path =  sg.popup_get_file("Open", no_window=True)
        if file_path:
            file = Path(file_path)
            window["MULTILINE2"].update(file.read_text())
            txt_open = True

    if event == "Save Text" and txt_open == True:
        if file_path:
            file = Path(file_path)
            file.write_text(values["MULTILINE2"])
        else:
            pass


    if event == "Save As Text":
        file_path = sg.popup_get_file("Save", save_as=True, no_window=True)
        if file_path:
            file = Path(file_path)
            file.write_text(values["MULTILINE2"])

    if event == 'Run Script' and script_open == True:
        runScript()

    if event == "_IN_" + "_Enter":
        runCommand(cmd=values['_IN_'], window=window)
        window["_IN_"].update("")


    if event == "Exit":
        break
####################################################################################1