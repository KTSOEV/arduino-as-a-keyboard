import time

import pyautogui
import serial

ser = serial.Serial('COM5', 9600)
while True:
    ser_bytes = ser.readline()
    type(ser_bytes)
    str_rn = ser_bytes.decode()
    str_rn
    str = str_rn.rstrip()
    type(str)
    f = int(str)
    if f == 1:
        pyautogui.press('ctrl')

    elif f == 2:
        pyautogui.press('w')

    elif f == 3:
        pyautogui.press('s')

    elif f == 4:
        pyautogui.press('d')

    elif f == 5:
        pyautogui.press('a')

    elif f == 6:
        pyautogui.press('shift')