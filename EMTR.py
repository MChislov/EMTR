import keyboard  # Using module keyboard
import handle_the_text

global trigger
trigger = False

keyboard.add_hotkey('ctrl+c,ctrl+x', handle_the_text.change_clipboard, args=['cas'])
keyboard.add_hotkey('ctrl+c,ctrl+q', handle_the_text.change_clipboard, args=['name'])
# keyboard.add_hotkey('ctrl+alt+x', handle_the_text.exit_app)