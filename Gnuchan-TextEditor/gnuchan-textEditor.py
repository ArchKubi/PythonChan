import PySimpleGUI as sg
from pathlib import Path
import pathlib,  pickle, requests, subprocess, sys, os
import a0_Clang,a1_PythonLang,a2_Html,a3_GdSCript,welcome



####################################################################################
#sg.popup(full_text)

def border(elem):
    return sg.Frame('', [[elem]], background_color='#0b011c')

font_size = 20
font_size_code = 11
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
#### starting screen
Default = [
    [
    sg.Text("Welcome to GnuChan Text Editor", background_color="#19032e", expand_x=True,justification="center",font=font),
    sg.Button("My Website", expand_x=True,font=font,border_width=0),
    sg.Button("My itch.io", expand_x=True,font=font,border_width=0),
    sg.Button("Exit", expand_x=True,font=font,border_width=0),
    ],

    [border(sg.Image(expand_x=True, expand_y=True, background_color="#19032e")),
     sg.Text(welcome, expand_x=True,font=font) 
    ], 

    [sg.Multiline(cheat,background_color="#18012e",expand_x=True,key="-CHEAT-",size=(900,900),font=font_bSizeFo,no_scrollbar=True,border_width=0)]
        ]
####################################################################################




####################################################################################
#### Text editor

Full_TextEditor = [
    [sg.Text("Open File",font=font,key="OpenText")],

    [sg.Button("Open Text", expand_x=True,font=font,border_width=0),
    sg.Button("Save Text", expand_x=True,font=font,border_width=0),
    sg.Button("Save As Text", expand_x=True,font=font,border_width=0)],

    [sg.Multiline('', size=(60, 20), key='TextFile',expand_y=True,expand_x=True,enable_events=True,font=font_code,background_color="#18012e",border_width=0)],
]
####################################################################################




####################################################################################
#### code editor 

Full_Script = [
    [sg.Text("Open File Tab1",font=font,key="OpenScript",border_width=0)],
    [
    sg.Button("Open Tab1", expand_x=True,font=font,border_width=0),
    sg.Button("Save Tab1",expand_x=True,font=font,border_width=0),
    sg.Button("Save As Tab1",expand_x=True,font=font,border_width=0)
    ],
    [
    sg.Multiline(size=(5,200), justification='r', key='-ScriptNum1-', no_scrollbar=True, write_only=True, disabled=True,  p=0,font=font_code,background_color="#18012e",border_width=0),
    sg.Multiline(size=(200,200), key='ScriptFile', p=0,expand_y=True,expand_x=True,font=font_code,background_color="#18012e",border_width=0)
    ],
]  
####################################################################################




####################################################################################
#### code editor 2

Full_Script2 = [
    [sg.Text("Open File Tab2",font=font,key="OpenScript2")],
    [sg.Button("Open Tab2", expand_x=True,font=font,border_width=0),
    sg.Button("Save Tab2",expand_x=True,font=font,border_width=0),
    sg.Button("Save As Tab2",expand_x=True,font=font,border_width=0)],
    [
    sg.Multiline(size=(5,200), justification='r', key='-ScriptNum2-', no_scrollbar=True, write_only=True, disabled=True,  p=0,font=font_code,background_color="#18012e",border_width=0),
    sg.Multiline(size=(200,200), key='ScriptFile2', p=0,expand_y=True,expand_x=True,font=font_code,background_color="#18012e",border_width=0)
    ],
]
####################################################################################



####################################################################################
Full_Script3 = [
    [sg.Text("Open File Tab3",font=font,key="OpenScript3")],
    [sg.Button("Open Tab3", expand_x=True,font=font,border_width=0),
    sg.Button("Save Tab3",expand_x=True,font=font,border_width=0),
    sg.Button("Save As Tab3",expand_x=True,font=font,border_width=0)],
    [
    sg.Multiline(size=(5,200), justification='r', key='-ScriptNum3-', no_scrollbar=True, write_only=True, disabled=True,  p=0,font=font_code,background_color="#18012e",border_width=0),
    sg.Multiline(size=(200,200), key='ScriptFile3', p=0,expand_y=True,expand_x=True,font=font_code,background_color="#18012e",border_width=0)
    ],
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
    [sg.Button("Run Script", expand_x=True,font=font,border_width=0)],
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
    [sg.Input(key='_IN_',font=font,background_color="#18012e",expand_x=True),
    sg.Button('Run',font=font,border_width=0)],
    [sg.Output(size=(60,15),font=font_code,expand_x=True,expand_y=True,background_color="#18012e")],
                ]
####################################################################################




####################################################################################
tab_Script = [
    [
            sg.TabGroup
        (
            [[
            sg.Tab(" Main ",Full_Script),
            sg.Tab(" Script1 ",Full_Script2),
            sg.Tab(" Script2 ",Full_Script3),
            sg.Tab(" Python Run ",pythonCodeRunner),
            ]],

            tab_location="center",
            title_color="#9d4edd",
            tab_background_color="#370666",
            selected_title_color="#c77dff",
            selected_background_color="#240046",
            font=font,
            key="Status",
            
        ),
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
            sg.Tab("Text",Full_TextEditor),
            sg.Tab("Script",tab_Script),
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
window = sg.Window("Gnuchan Text Editor",tab_group,finalize=True,return_keyboard_events=True,resizable=True,size=(1200,700))
window['_IN_'].bind("<Return>","_Enter")
window.bind('<Configure>', "Configure")
status = window['Status']

ScriptFile = window['ScriptFile']
widget = ScriptFile.widget


####################################################################################
text = window['TextFile'].Widget
text.configure(undo=True)
text.bind('<Control-Shift-Key-Z>', lambda event, text=text:redo(event, text))

script1 = window['ScriptFile'].Widget
script1.configure(undo=True)
script1.bind('<Control-Shift-Key-Z>', lambda event, text=text:redo(event, text))

script2 = window['ScriptFile2'].Widget
script2.configure(undo=True)
script2.bind('<Control-Shift-Key-Z>', lambda event, text=text:redo(event, text))

script3 = window['ScriptFile3'].Widget
script3.configure(undo=True)
script3.bind('<Control-Shift-Key-Z>', lambda event, text=text:redo(event, text))


window['-ScriptNum1-'].update('\n'.join([str(x) for x in range(1,51)]))
window['-ScriptNum2-'].update('\n'.join([str(x) for x in range(1,51)]))
window['-ScriptNum3-'].update('\n'.join([str(x) for x in range(1,51)]))


tab = sg.Text.char_width_in_pixels(font_code)*4
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

## Script Edit

    if event == "Open Tab1":
        file_path_Script =  sg.popup_get_file("Open", no_window=True)
        if file_path_Script:
            file = Path(file_path_Script)
            window["ScriptFile"].update(file.read_text())
            script_open = True
            window["OpenScript"].update(file)

        if ".py" in file_path_Script:
            window["-CHEAT-"].update(python)

        elif ".c" in file_path_Script:
            window["-CHEAT-"].update(cLang)
        elif ".html" in file_path_Script:
            window["-CHEAT-"].update(htmlLang)
        elif ".gd" in file_path_Script:
            window["-CHEAT-"].update(gdScriptLang)

    if event == "Save Tab1" and script_open == True:
        if file_path_Script:
            file = Path(file_path_Script)
            file.write_text(values["ScriptFile"])
        else:
            pass


    elif event == "Save Tab1" and script_open == False:
        window["ScriptFile"].update("Open File Bro")


    if event == "Save As Tab1":
        file_path_Script = sg.popup_get_file("Save Tab1", save_as=True, no_window=True)
        if file_path_Script:
            file = Path(file_path_Script)
            file.write_text(values["ScriptFile"])
            script_open = True
            window["OpenScript"].update(file)



## Script Edit

    if event == "Open Tab2":
        file_path_Script2 =  sg.popup_get_file("Open Tab2", no_window=True)
        if file_path_Script2 :
            file2 = Path(file_path_Script2 )
            window["ScriptFile2"].update(file2.read_text())
            script_open = True
            window["OpenScript2"].update(file2)

    if event == "Save Tab2" and script_open == True:
        if file_path_Script2 :
            file2 = Path(file_path_Script2 )
            file2.write_text(values["ScriptFile2"])
        else:
            pass

    if event == "Save Tab2" and script_open == False:
        window["ScriptFile2"].update("Open File Bro")

    if event == "Save As Tab2":
        file_path_Script2  = sg.popup_get_file("Save Tab2", save_as=True, no_window=True)
        if file_path_Script2 :
            file2 = Path(file_path_Script2 )
            file2.write_text(values["ScriptFile2"])
            script_open = True
            window["OpenScript2"].update(file2)


## Script Edit

    if event == "Open Tab3":
        file_path_Script3 =  sg.popup_get_file("Open Tab3", no_window=True)
        if file_path_Script3 :
            file3 = Path(file_path_Script3 )
            window["ScriptFile3"].update(file3.read_text())
            script_open = True
            window["OpenScript3"].update(file3)


    if event == "Save Tab3" and script_open == True:
        if file_path_Script3 :
            file3 = Path(file_path_Script3 )
            file3.write_text(values["ScriptFile3"])
        else:
            pass


    if event == "Save Tab3" and script_open == False:
        window["ScriptFile3"].update("Open File Bro")


    if event == "Save As Tab3":
        file_path_Script3  = sg.popup_get_file("Save Tab3", save_as=True, no_window=True)
        if file_path_Script3 :
            file3 = Path(file_path_Script3 )
            file3.write_text(values["ScriptFile3"])
            script_open = True
            window["OpenScript3"].update(file3)

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


    if event == "Save Text" and txt_open == False:
        window["TextFile"].update("Open File Bro")


    if event == "Save As Text":
        file_path_Text = sg.popup_get_file("Save As Text", save_as=True, no_window=True)
        if file_path_Text:
            fileText = Path(file_path_Text)
            fileText.write_text(values["TextFile"])
            txt_open = True
            window["OpenText"].update(fileText)


## Extra


    if event == 'Run Script' and script_open == True:
        runScript()

    if event == "_IN_" + "_Enter":
        runCommand(cmd=values['_IN_'], window=window)
        window["_IN_"].update("")

    if event == "Exit":
        break
####################################################################################
