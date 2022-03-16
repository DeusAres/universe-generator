import PySimpleGUI as sg
import generateSquares as gs
from funPIL import df
import json
from pathlib import Path
import os
import save

os.chdir(Path(__file__).parents[0])

s = 20, 1
s2 = 5, 1
names = ['nSquares', 'minSize', 'maxSize', 'minDistance', 'W', 'H']

sg.LOOK_AND_FEEL_TABLE["DarkPoker"] = {
    "BACKGROUND": "#252525",
    "TEXT": "#FFFFFF",
    "INPUT": "#af0404",
    "TEXT_INPUT": "#FFFFFF",
    "SCROLL": "#af0404",
    "BUTTON": ("#FFFFFF", "#252525"),
    "BORDER": 1,
    "SLIDER_DEPTH": 0,
    "PROGRESS_DEPTH": 0,
    "COLOR_LIST": ["#252525", "#414141", "#af0404", "#ff0000"],
    "PROGRESS": ("# D1826B", "# CC8019"),
}
sg.theme("DarkPoker")

layout = [
    [
        sg.Column([
            [sg.Image(key='prev')],
            [sg.Push(),sg.Button('Generate'),sg.Push()]
        ]),
        sg.Column([
            [sg.Text('Population', s), sg.Input(key='nSquares', s=s2)],
            [sg.Text('Minimal size', s), sg.Input(key='minSize', s=s2)],
            [sg.Text('Maximum size', s), sg.Input(key='maxSize', s=s2)],
            [sg.Text('Distance between', s), sg.Input(key='minDistance', s=s2)],
            [sg.Text('Width of canvas', s), sg.Input(key='W', s=s2)], 
            [sg.Text('Height of canvas', s), sg.Input(key='H', s=s2)],
            [sg.Push(), sg.Button('Save')]
        ])
    ]
]

window = sg.Window("Universe generator", layout, finalize=True)

with open('numbers.json', 'r') as f:
    numbers = json.load(f)

[window[each].Update(str(numbers[each])) for each in numbers.keys()]

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Quit":
        break

    if event == 'Generate':
        numbers = {}
        for each in names:
            numbers[each] = int(values[each]) 

        with open('numbers.json', 'w') as f:
            json.dump(numbers, f)
        
        img = gs.main(*numbers.values())
        if not img:
            sg.Popup("Hey chief. It took to much to generate the universe. Try lowering some settings")
        else:
            window['prev'].Update(data=df.image_to_data(df.resizeToFit(img, 500)[0]))

    if event == 'Save':
        try:
            save.main(img)
        except:
            pass

window.close()