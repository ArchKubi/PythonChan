import PySimpleGUI as sg

sz = (7,1)

column1 = [ [sg.ReadButton('UPDATE\nTEXT', size=sz)],
            [sg.ReadButton('LOAD-\nTEXT', size=sz)],
            [sg.ReadButton('SAVE-VOC', size=sz)],
            [sg.ReadButton('CLEAR\nTEXT', size=sz)]
            ]

column2 = [[sg.ReadButton('Click here')]]

col_layout = [
                [sg.InputText(focus=True, key='word')],
                [sg.Column(column2)]
             ]

layout = [
            [sg.Text("Study Text Box")],
            [sg.Multiline(size=(50,10), font='Tahoma 13', key='-STLINE-', autoscroll=True), sg.Column(column1), sg.VerticalSeparator(pad=None), sg.Column(col_layout)]
         ]
        

window = sg.Window("TbLLT Program", layout, resizable=True, finalize=True)

while True:
    event, values=window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'SAVE-VOC':
        with open('someText(saved).txt', 'w+') as file:
            savedText1 = file.write(values['-STLINE-'])
        file.close()
    if event == 'Click here':
        window['-STLINE-'].update(values['word'])
window.close()