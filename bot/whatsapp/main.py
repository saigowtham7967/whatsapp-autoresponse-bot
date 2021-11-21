import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Button, Controller
from time import sleep

pt.FAILSAFE = True
mouse = Controller()


# Nav to any image
def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=.7)

    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pt.moveTo(position, duration=.5)
        pt.moveRel(off_x, off_y, duration=.2)
        pt.click(clicks=clicks, interval=.1)


def get_message():
    nav_to_image('images/paperclip.jpg', 0, off_y=-80)
    mouse.click(Button.left, 3)
    pt.rightClick()

    copy = nav_to_image('images/copy.jpg', 1)
    sleep(.5)
    return pc.paste() if copy != 0 else 0


def send_message(msg):
    nav_to_image('images/paperclip.jpg', 2, off_x=100)
    pt.typewrite(msg, interval=.1)
    pt.typewrite('\n')


def close_reply_box():
    nav_to_image('images/x.jpg', 2)


def process_message(msg):
    raw_msg = msg.lower()

    if raw_msg.startswith('hap') or raw_msg.startswith('app') or raw_msg.startswith('wish') or raw_msg.startswith('many'):
        return "Thank you -Prateek's AI"
    elif raw_msg == 'yes':
        return 'Bot says you wrote yes! -'
    elif 'ok' in raw_msg:
        return 'You wrote ok!'
    else:
        return ' '


# Loop the code
delay = 10
last_message = ''

sleep(3)
while True:
    # Checks for new messages
    nav_to_image('images/green_circle.jpg', 2, off_x=-100)  # 1
    close_reply_box()  # 2

    message = get_message()  # 3
    if message != 0:
        send_message(process_message(message))
    else:
        print('No new messages...')

    sleep(5)
