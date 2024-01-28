import time
import RPi.GPIO as GPIO
import socket

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(16, GPIO.IN)
#123
udp_host = '192.168.30.101'
udp_port = 50007
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
COMMAND_DELAY = 0.3
def send_command(command):
    udp_socket.sendto(command, (udp_host, udp_port))


BUTTON1 = 26
BUTTON2 = 19
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def handle_button1(channel):
    if GPIO.input(BUTTON1) == GPIO.LOW:
        send_command(b'\xaa\xa1\x00\x05Zoom-U\xa1\xbe\xfe\xc1.>\x0e\x07\x15m')
        print('Zooming in')
    else:
        send_command(b'\xaa\xa1\x00\x05Stop_U\x95=y\xc1\x1c\xb4\x04\xca\xb4\xfe')
        print('Stopping')

def handle_button2(channel):
    if GPIO.input(BUTTON2) == GPIO.LOW:
        send_command(b'\xaa\xa1\x00\x05Zoom+U::\x18\xd2s\xba\x84\x96\xf9\xaf')
        print('Zooming out')
    else:
        send_command(b'\xaa\xa1\x00\x05Stop_U\x95=y\xc1\x1c\xb4\x04\xca\xb4\xfe')
        print('Stopping')


GPIO.add_event_detect(BUTTON1, GPIO.BOTH, callback=handle_button1, bouncetime=300)
GPIO.add_event_detect(BUTTON2, GPIO.BOTH, callback=handle_button2, bouncetime=300)



previous_state = "NEUTRAL"

def check_joystick():
    global previous_state
    current_state = "NEUTRAL"

    if GPIO.input(6) == GPIO.LOW:
        current_state = "RIGHT"
    elif GPIO.input(21) == GPIO.LOW:
        current_state = "UP"
    elif GPIO.input(20) == GPIO.LOW:
        current_state = "LEFT"
    elif GPIO.input(16) == GPIO.LOW:
        current_state = "DOWN"


    if current_state != previous_state:
        if current_state == "RIGHT":
            send_command(b'\xaa\xa1\x00\x05RightU\x89t\x86\xc7\x1c\xc7\x9cw\x1a\x8d')
            print("RIGHT")
        elif current_state == "UP":
            send_command(b'\xaa\xa1\x00\x05_Up__U\xd8\xea\x80\xee\x03\xce]\x08\x1e\xfb')
            print("UP")
        elif current_state == "LEFT":
            send_command(b'\xaa\xa1\x00\x05Left_UNP\xadW\x9d\x0f\x8d\x03O\x88')
            print("LEFT")
        elif current_state == "DOWN":
            send_command(b'\xaa\xa1\x00\x05Down_U\x96}\xeb\xe3\xb4\xe7\xee\xd97\x86')
            print("DOWN")
        elif current_state == "NEUTRAL":
            send_command(b'\xaa\xa1\x00\x05Stop_U\x95=y\xc1\x1c\xb4\x04\xca\xb4\xfe')
            print("STOP")
        
        previous_state = current_state
        time.sleep(COMMAND_DELAY)

try:
    while True:
        check_joystick()
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
