# -*- coding:utf-8 -*-
from urllib import request
import PySimpleGUI as sg
import requests

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

sg.theme("MyCreatedTheme")

layout = [
        [sg.Text("Welcome to GnuChan Calculator", expand_x=True,justification="center")],
        [border(sg.Image(size=(500,500), data=response.raw.read(), expand_x=True, expand_y=True, background_color="#19032e"))],
        
        
        ]

tab_group = [
    [
            sg.TabGroup
        (
            [[
            sg.Tab("Default", layout),
            sg.Button("Exit", expand_x=True),
            ]],

            tab_location="center",
            title_color="#9d4edd",
            tab_background_color="#370666",
            selected_title_color="#c77dff",
            selected_background_color="#240046",
            key='Status'
        ),
    ]
]

layout = [[sg.Text('GnuChan', size=(30, 1), key='Status')]]
window = sg.Window('Title', layout, resizable=True, finalize=True)
window.bind('<Configure>', "Configure")
status = window['Status']

while True:

    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Configure':
        if window.TKroot.state() == 'zoomed':
            status.update(value='Window zoomed and maximized !')
        else:
            status.update(value='Window normal')


