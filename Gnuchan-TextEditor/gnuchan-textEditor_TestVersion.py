import PySimpleGUI as sg
from pathlib import Path
import pathlib,  pickle, requests, subprocess, sys, os
import a0_Clang,a1_PythonLang,a2_Html,a3_GdSCript,welcome



####################################################################################
#sg.popup(full_text)

def border(elem):
    return sg.Frame('', [[elem]], background_color='#0b011c')

font_size = 20
font_size_code = 13
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
-----------------------------------------
don\'t use like this:
while True:
    print("fBom")
-----------------------------------------
not working editor freezes
input() nope not working

range works normal

C : #include <stdio.h>
    int main(){
            
        printf("Hello F... World BRUH")   
        return 0;
    }

"""

python = a1_PythonLang.txt
cLang  = a0_Clang.Ctxt
htmlLang = a2_Html.htmTxt
welcome = welcome.welcomeTXT
gdScriptLang = a3_GdSCript
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

pythonFile = False
cFile = False
gdscriptFile = False
htmlFile = False

pro_url = ""

if pythonFile == True:
    "https://raw.githubusercontent.com/ArchKubi/PythonChan/main/Gnuchan-TextEditor/complete_lang/pythonFile.txt"
elif cFile == True:
    "https://raw.githubusercontent.com/ArchKubi/PythonChan/main/Gnuchan-TextEditor/complete_lang/cFile.txt"
elif gdscriptFile == True:
    "https://raw.githubusercontent.com/ArchKubi/PythonChan/main/Gnuchan-TextEditor/complete_lang/htmlFile.txt"
elif htmlFile == True:
    "https://github.com/ArchKubi/PythonChan/blob/main/Gnuchan-TextEditor/complete_lang/gdscriptFile.txt"

dictionary_file = 'dictionary.pickle'
if not pathlib.Path(dictionary_file).is_file():
    # Load dictionary from web if file not found
    try:
        url = pro_url
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

width = max(map(len, dictionary_file))


Full_TextEditor = [
    [sg.Text("Open File",font=font,key="OpenScript")],
    [sg.Button("Open", expand_x=True,font=font),sg.Button("Save",expand_x=True,font=font),sg.Button("Save As",expand_x=True,font=font)],
    [sg.Multiline("",size=(2, 6),expand_x=True,expand_y=True,background_color="#18012e",font=font_code,no_scrollbar=True),
     sg.Multiline('', size=(100, 20), key='ScriptFile',expand_y=True,expand_x=True,font=font_code,no_scrollbar=True,background_color="#18012e"),
     sg.Listbox([], size=(7, 6), expand_y=True,expand_x=True,enable_events=True, key='ScriptList',font=font,background_color="#18012e",no_scrollbar=True)
     
     ],
]
####################################################################################

####################################################################################
#### Text editor

Full_TextEditor2 = [
    [sg.Text("Open File",font=font,key="OpenText")],
    [sg.Button("Open Text", expand_x=True,font=font),sg.Button("Save Text", expand_x=True,font=font),sg.Button("Save As Text", expand_x=True,font=font)],
    [sg.Multiline('', size=(60, 20), key='TextFile',expand_y=True,expand_x=True,enable_events=True,font=font_code,background_color="#18012e")],
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
#### Text editor

Full_GDScript = [
    [sg.Text("Open GDScript",font=font,key="OpenGDScript")],
    [sg.Button("Open GDScript", expand_x=True,font=font),sg.Button("Save GDScript", expand_x=True,font=font),sg.Button("Save As GDScript", expand_x=True,font=font)],
    [sg.Multiline('', size=(100, 20), key='GDScript',expand_y=True,expand_x=True,font=font_code,no_scrollbar=True,background_color="#18012e",),
    sg.Listbox([], size=(7, 6), expand_y=True,expand_x=True,enable_events=True, key='GDScriptList',font=font,background_color="#18012e",no_scrollbar=True)

    ]

]
####################################################################################




####################################################################################
tab_group = [
    [
            sg.TabGroup
        (
            [[
            sg.Tab("Default", Default),
            sg.Tab("Terminal",GnuChan_Terminal),
            sg.Tab("Text",Full_TextEditor2),
            sg.Tab("Code",Full_TextEditor),
            sg.Tab("Python Run",pythonCodeRunner),
            sg.Tab("GDScript", Full_GDScript),
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


ScriptFile = window['ScriptFile']
widget = ScriptFile.widget
ScriptFile.bind('<Key>', "+Key")
ScriptList = window['ScriptList']

text,text2 = window['ScriptFile'].Widget , window['TextFile'].Widget
text.configure(undo=True)
text.bind('<Control-Shift-Key-Z>', lambda event, text=text:redo(event, text))

text2.configure(undo=True)
text2.bind('<Control-Shift-Key-Z>', lambda event, text=text:redo(event, text))

gdscriptX_ = window["GDScript"].Widget
gdscriptX_.configure(undo=True)
gdscriptX_.bind('<Control-Shift-Key-Z>', lambda event, text=text:redo(event, text))




tab = sg.Text.char_width_in_pixels(font_code)*3
widget.configure(tabs=(tab,)) 

lapse_amount = 0
script_open = False
txt_open = False
GDScript_open = False
####################################################################################



####################################################################################
while True:
    event, values = window.Read()
    if event == sg.WIN_CLOSED:
        break

## AutoComplete Not Finish

    elif event == 'ScriptFile+Key':
        entry = widget.get("insert-1c wordstart", "insert")
        if entry:
            words = [word for word in dictionary if word.startswith(entry)]
        else:
            words = []
        ScriptList.update(words)

    elif event == 'ScriptList':
        items = values[event]
        if not items:
            continue
        widget.delete("insert-1c wordstart", "insert")
        widget.insert("insert", items[0])
        ScriptList.update([])
        ScriptFile.set_focus()



    elif event == 'ScriptFile+Key':
        entry = widget.get("insert-1c wordstart", "insert")
        if entry:
            words = [word for word in dictionary if word.startswith(entry)]
        else:
            words = []
        ScriptList.update(words)

    elif event == 'ScriptList':
        items = values[event]
        if not items:
            continue
        widget.delete("insert-1c wordstart", "insert")
        widget.insert("insert", items[0])
        ScriptList.update([])
        ScriptFile.set_focus()




## Script Edit

    if event == "Open":
        file_path_Script =  sg.popup_get_file("Open", no_window=True)
        if file_path_Script:
            file = Path(file_path_Script)
            window["ScriptFile"].update(file.read_text())
            script_open = True
            window["OpenScript"].update(file)
            


        if ".py" in file_path_Script:
            window["-CHEAT-"].update(python)
            pythonFile = True

        elif ".c" in file_path_Script:
            window["-CHEAT-"].update(cLang)
            cFile = True
        elif ".html" in file_path_Script:
            window["-CHEAT-"].update(htmlLang)
            htmlFile = True
        elif ".gd" in file_path_Script:
            window["-CHEAT-"].update(gdScriptLang)
            gdscriptFile = True


    if event == "Save As":
        file_path_Script = sg.popup_get_file("Save", save_as=True, no_window=True)
        if file_path_Script:
            file = Path(file_path_Script)
            file.write_text(values["ScriptFile"])
            script_open = True
            window["OpenScript"].update(file)
    if event == "Save" and script_open == True:
        if file_path_Script:
            file = Path(file_path_Script)
            file.write_text(values["ScriptFile"])
        else:
            pass

## Text Edit

    if event == "Open Text":
        file_path_Text =  sg.popup_get_file("Open Text", no_window=True)
        if file_path_Text:
            fileText = Path(file_path_Text)
            window["TextFile"].update(fileText.read_text())
            txt_open = True
            window["OpenText"].update(fileText)
            

    if event == "Save Text" and txt_open == True:
        if file_path_Text:
            fileText = Path(file_path_Text)
            fileText.write_text(values["TextFile"])
        else:
            pass


    if event == "Save As Text":
        file_path_Text = sg.popup_get_file("Save As Text", save_as=True, no_window=True)
        if file_path_Text:
            fileText = Path(file_path_Text)
            fileText.write_text(values["TextFile"])
            txt_open = True
            window["OpenText"].update(fileText)


## Text Edit

    if event == "Open GDScript":
        file_path_GDScript =  sg.popup_get_file("Open GDScript", no_window=True)
        if file_path_GDScript:
            file_GDscript = Path(file_path_GDScript)
            window["GDScript"].update(file_GDscript.read_text())
            GDScript_open = True
            window["OpenGDScript"].update(file_GDscript)

    if event == "Save GDScript" and GDScript_open == True:
        if file_path_GDScript:
            file_GDscript = Path(file_path_GDScript)
            file_GDscript.write_text(values["GDScript"])
            
        else:
            pass

    if event == "Save As GDScript":
        file_path_GDScript = sg.popup_get_file("Save As GDScript", save_as=True, no_window=True)
        if file_path_GDScript:
            file_GDscript = Path(file_path_GDScript)
            file_GDscript.write_text(values["GDScript"])
            GDScript_open = True
            window["OpenGDScript"].update(file_GDscript)




## Extra


    if event == 'Run Script' and script_open == True:
        runScript()

    if event == "_IN_" + "_Enter":
        runCommand(cmd=values['_IN_'], window=window)
        window["_IN_"].update("")


    if event == "Exit":
        break
####################################################################################