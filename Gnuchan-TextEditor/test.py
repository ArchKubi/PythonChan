import sys
import re
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg




def autocomplete_popup_show(text_list ):
    autocomplete_popup_layout = [[sg.Listbox(values=text_list,
                                             size=(15,len(text_list)),
                                             change_submits=True,
                                             bind_return_key=True,
                                             auto_size_text=True,
                                             key='_FLOATING_LISTBOX_', enable_events=True)]]

    autocomplete_popup = sg.Window("Borderless Window",
                                   default_element_size=(12, 1),
                                   text_justification='c',
                                   auto_size_text=False,
                                   auto_size_buttons=False,
                                   no_titlebar=True,
                                   grab_anywhere=True,
                                   return_keyboard_events=True,
                                   keep_on_top=True,
                                   background_color='black',
                                   location=(1320,622),
                                   default_button_element_size=(12, 1))

    window = autocomplete_popup.Layout(autocomplete_popup_layout).Finalize()
    return window



def predict_text(input, lista):
    pattern = re.compile('.*' + input + '.*')
    return [w for w in lista if re.match(pattern, w)]

# print(predict_text('1', ['123']))
choices = ['ABC' + str(i) for i in range(30)]
# print(predict_text('1', values))
# print(values)
layout = [  [sg.Text('Your typed chars appear here:')],
            [sg.In(key='_INPUT_', size=(5,1)),sg.Text('', key='_OUTPUT_')],
            [sg.Listbox(choices,  size=(10,15), key='_COMBO_')],
            [sg.Button('Show'), sg.Button('Exit')],
         ]

window = sg.Window('Window Title', return_keyboard_events=True).Layout(layout)


sel_item = 0
while True:             # Event Loop
    event, values = window.Read(timeout=100)
    if event is None or event == 'Exit':
        break
    if event != sg.TIMEOUT_KEY:
        in_val = values['_INPUT_']
        prediction_list = predict_text(str(in_val), choices)
        if prediction_list:
            try:
                fwindow.Close()
            except: pass
            fwindow = autocomplete_popup_show(prediction_list)
            list_elem = fwindow.Element('_FLOATING_LISTBOX_')

            window.Element('_OUTPUT_').Update(prediction_list[0])

        if event == '_COMBO_':
            sg.Popup('Chose', values['_COMBO_'])
        if event == 'Down:40':
            sel_item = sel_item + (sel_item<len(prediction_list))
            list_elem.Update(set_to_index=sel_item)
        elif event == 'Up:38':
            sel_item = sel_item - (sel_item>0)
            list_elem.Update(set_to_index=sel_item)
        if event == '\r' or event == 'Show':
            if len(values['_COMBO_']) == 0:
                chosen = values['_INPUT_']
            else:
                chosen = values['_COMBO_']
            sg.Popup('Chose', chosen)
    try:
        ev2, vals2 = fwindow.Read(timeout=100)
        if ev2 != sg.TIMEOUT_KEY:
            fwindow.Close()
            sg.Popup('Chose from window', vals2['_FLOATING_LISTBOX_'])
    except: pass
window.Close()