from pynput import mouse, keyboard
import logging
import time



lgr = logging.getLogger('Mouse')
lgr_kb = logging.getLogger('Keyboard')
lgr.setLevel(logging.DEBUG) # log all escalated at and above DEBUG
# add a file handler
fh = logging.FileHandler('game_play_3.csv')
fh.setLevel(logging.DEBUG) # ensure all messages are logged to file

# create a formatter and set the formatter for the handler.
frmt = logging.Formatter('%(asctime)s,%(message)s')
fh.setFormatter(frmt)

# add the Handler to the logger
lgr.addHandler(fh)
lgr_kb.addHandler(fh)






def on_move(x, y):
	lgr.info(f'Moved: {x}_{y}')

def on_click(x, y, button, pressed):
	lgr.info(f"Click {x}_{y}")

def on_scroll(x, y, dx, dy):
	lgr.info(f"Scroll {'down' if dy < 0 else 'up'} at {x}_{y}")

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()


def on_press(key):
	lgr.info(f"Pressed key {key}")
    

listener_2 = keyboard.Listener(
	on_press=on_press)
listener_2.start()


while True:
	continue		
