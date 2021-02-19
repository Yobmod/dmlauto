import time
import serial

# python -m serial.tools.list_ports

# ser = serial.Serial('COM6', 9600)

"""
if ser.isOpen():
    ser.close()
ser.open()
ser.isOpen()
"""

"""
with serial.Serial('/dev/ttyS1', 19200, timeout=1) as ser:
    x = ser.read()          # read one byte
    s = ser.read(10)        # read up to ten bytes (timeout)
    line = ser.readline()   # read a '\n' terminated line
"""
  

while True:
    # message = ser.readline()
    # print(message)
    # ser.open()

    with serial.Serial('COM6', 9600, timeout=0.1) as ser:
        command = b'red \r\n'
        ser.write(command) # sends command to cpy board
        time.sleep(0.2)
    
    with serial.Serial('COM6', 9600, timeout=0.4) as ser:
        message = ser.readline()
        print(message)
        time.sleep(0.1)


    with serial.Serial('COM6', 9600, timeout=0.1) as ser:
        command = b'none \r\n'
        ser.write(command)  # sends command to cpy board
        time.sleep(0.2)

    
    with serial.Serial('COM6', 9600, timeout=0.4) as ser:
        message = ser.readline()
        print(message)
        time.sleep(0.1)

    with serial.Serial('COM6', 9600, timeout=0.1) as ser:
        command = b'yel \r\n'
        ser.write(command)  # sends command to cpy board
        time.sleep(0.2)

    
    with serial.Serial('COM6', 9600, timeout=0.4) as ser:
        message = ser.readline()
        print(message)
        time.sleep(0.1)

