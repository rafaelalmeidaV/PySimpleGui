import PySimpleGUI as sg
import threading
import time
import pygame

sg.theme('Topanga')

def start_pomodoro():
    global paused
    duration = 25 * 60  # 25 minutos em segundos
    
    while duration and not paused:
        minutes, seconds = divmod(duration, 60)
        time_format = '{:02d}:{:02d}'.format(minutes, seconds)
        window['-OUTPUT-'].update(time_format)
        duration -= 1
        time.sleep(1)    
    
    if not paused:        
        pygame.mixer.music.load('Pomodoro/sound/Cell-phone-ring-sound.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
    
    
    

def run_pomodoro():
    threading.Thread(target=start_pomodoro).start()

def pause_pomodoro():  
    global paused
    paused = True

def resume_pomodoro():  
    global paused
    paused = False
    run_pomodoro()

src_Image = r'Pomodoro\img\pomodoro.png'


layout = [ 
    
    [sg.Image(src_Image)],
    [sg.Text(size=(20, 1))],
    [sg.Column([
        [sg.Text('Pomodoro', font=('Helvetica', 26), justification='center')],
        [sg.Text('00:00', key='-OUTPUT-', font=('Helvetica', 48), justification='center')],
        [sg.Button('Iniciar', size=(10, 2)), sg.Button('Pausar', size=(10, 2)), sg.Button('Retomar', size=(10, 2))]
    ], element_justification='center')], 
    [sg.Text(size=(20, 1))],
    
]

window = sg.Window('Pomodoro', layout)

pygame.mixer.init()

paused = False

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == 'Iniciar':        
        run_pomodoro()
        window.refresh()

    if event == 'Pausar':
        pause_pomodoro()
        window.refresh()
    
    if event == 'Retomar':
        resume_pomodoro()
        window.refresh()

        
window.close()