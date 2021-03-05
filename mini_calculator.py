import PySimpleGUI as sg

layout = [[sg.Text("Bitte gebe hier deine Rechnung ein")],
          [sg.Input(key='input')],
          [sg.Text(size=(40, 1), key='output')],
          [sg.Button('Ok'), sg.Button('Quit')]]

window = sg.Window('Rechner', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    try:
        window['output'].update(f'Ergebniss: {eval(values["input"])}')
    except:
        window['-output-'].update(f'Ergebniss: Error')
