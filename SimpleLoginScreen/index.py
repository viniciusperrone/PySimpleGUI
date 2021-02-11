from PySimpleGUI import PySimpleGUI as sg

sg.theme('BlueMono')

layout = [
  [sg.Text('User'), sg.Input(key='user')],
  [sg.Text('Password'), sg.Input(key='password', password_char='*')],
  [sg.Checkbox('Save Login?')],
  [sg.Button('Enter')]
]

window = sg.Window('Login Screen', layout)

while True: 
  events, values = window.read()
  if events == sg.WINDOW_CLOSED: 
    break
  if events == 'Enter':
    if values['user'] == 'vinicius' and values['password'] == '123456':
      print('Ok')
    else: 
      print('Failed!')
