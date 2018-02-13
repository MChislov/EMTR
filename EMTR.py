import keyboard  # Using module keyboard
import main_window
import handle_the_text



def exit_app():
	exit()

keyboard.add_hotkey('ctrl+c,ctrl+x', handle_the_text.change_clipboard, args=['cas'])
keyboard.add_hotkey('ctrl+c,ctrl+q', handle_the_text.change_clipboard, args=['name'])
keyboard.add_hotkey('ctrl+alt,x', exit_app)

while True:
	pass