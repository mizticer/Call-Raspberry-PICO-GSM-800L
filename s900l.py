from machine import UART, Pin
import utime

NEW_LINE = "\r\n"
BAUDRATE = 115200

uart = UART(0, BAUDRATE, tx=Pin(0), rx=Pin(1))

def Send_command(cmd, back, timeout=2000):  # Send AT command
        rec_buff = b''
        uart.write((cmd+'\r\n').encode())
        prvmills = utime.ticks_ms()
        while (utime.ticks_ms()-prvmills) < timeout:
            if uart.any():
                rec_buff = b"".join([rec_buff, uart.read(1)])
        if rec_buff != '':
            if back not in rec_buff.decode():
                print(cmd + ' back:\t' + rec_buff.decode())
                return 0
            else:
                print(rec_buff.decode())
                return 1
        else:
            print(cmd + ' no responce')
            
def wait_resp_info(timeout=3000):
        prvmills = utime.ticks_ms()
        info = b""
        while (utime.ticks_ms()-prvmills) < timeout:
            if uart.any():
                info = b"".join([info, uart.read(1)])
        print(info.decode())
        return info
    
def Check_and_start(): # Initialize SIM Module 
        while True:
            uart.write(bytearray(b'ATE1\r\n'))
            utime.sleep(2)
            uart.write(bytearray(b'AT\r\n'))
            rec_temp = wait_resp_info()
            if 'OK' in rec_temp.decode():
                print('Pico 2G is ready\r\n' + rec_temp.decode())
                break
            else:
                print('Pico 2G is starting up, please wait...\r\n')
                
def Network_checking():# Network connectivity check
        for i in range(1, 3):
            if Send_command("AT+CGREG?", "0,1") == 1:
                print('SIM868 is online\r\n')
                break
            else:
                print('SIM868 is offline, please wait...\r\n')
                utime.sleep(2)
                continue
    
def call(mobile_number,time):
        Check_and_start() # Initialize SIM Module 
        Network_checking() # Network connectivity check
        
        Send_command('AT+CHFA=1', 'OK')
        Send_command("ATD"+mobile_number+";", 'OK')
        utime.sleep(time)
        Send_command('AT+CHUP;', 'OK')