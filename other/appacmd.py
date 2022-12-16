# from serial import Serial

# def data_send(v):
#     if v == 0:
#         hex_string = '55 55 00 00 AA'
#     elif v == 1:
#         hex_string = '55 55 00 00 AA'
#     elif v == 2:
#         hex_string = '55 55 00 00 AA'
#     message = bytes.fromhex(hex_string)
#     ser = Serial(port='COM4', baudrate=9600, timeout = 0.1)
#     ser.open()
#     #self.write(ser, message)
#     if ser.is_open:
#         ser.flushInput()
#         ser.flushOutput()
#         sleep(0.1)
#         try:
#             ser.write(message)
#         except Exception as exc:
#             print('type: {0}, message: {1}'.format(type(exc), str(exc)))
#         else:
#             res = ser.readline()
#             print(res)
#             ser.close()

import time
import serial

# from ctypes import *

from threading import Timer
from datetime import datetime

from check_crc import *
from appa_109n import *

# 5555000e02000001e31f001201f40100790240
# b'UU\x00\x0e\x01\x00\x00\x00\x19\x04\x00\x0c\x01\x00\x00\x00y\x02^' 19

# Not connected...
# Please connect the device

# class data_read(Structure):
#     _fields_ = [("appa_mod0", c_ubyte),
#                 ("appa_mod1", c_ubyte),
#                 ("appa_mod2", c_ubyte),
#                 ("appa_mod3", c_ubyte),
#                 ("rotor_code", c_ubyte),
#                 ("blue_code", c_ubyte),
#                 ("key_code", c_ubyte),
#                 ("range_code", c_ubyte),
#                 ("main_read0", c_ubyte),
#                 ("main_read1", c_ubyte),
#                 ("main_read2", c_ubyte),
#                 ("main_read3", c_ubyte),
#                 ("main_read4", c_ubyte),
#                 ("sub_read0", c_ubyte),
#                 ("sub_read1", c_ubyte),
#                 ("sub_read2", c_ubyte),
#                 ("sub_read3", c_ubyte),
#                 ("sub_read4", c_ubyte),
#                 ("check_sum", c_ubyte)]

class DataAppa:
    def __init__(self, 
        index_count, 
        time_receive, 
        rotor_code, 
        blue_code, 
        range_code, 
        main_read, 
        sub_read, 
        main_pointcode, 
        func_table, 
        unitcode):
        self.index_count = index_count
        self.time_receive = time_receive
        self.rotor_code = rotor_code
        self.blue_code = blue_code
        self.range_code = range_code
        self.main_read = main_read
        self.sub_read = sub_read
        self.main_pointcode = main_pointcode
        self.func_table = func_table
        self.unitcode = unitcode




def value_to_float(value: int, point_code: int) -> float:
    v = len(str(value))
    p = point_code
    if v > p:
        return float(str(value)[0:len(str(value)) - 
                                point_code]+"."+str(value)[len(str(value)) -
                                point_code:len(str(value))])
    elif v == p:
        return float("0."+str(value))        
    else:
        if v == 2 or (p-v) == 1:
            return float("0.0"+str(value))   
        elif v == 1 or (p-v) == 2:
            return float("0.00"+str(value))    
        elif (p-v) == 3:
            return float("0.000"+str(value)) 


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


data_appa = DataAppa(0, None, None, None, None, None, None, None, None, None)
# print(data_appa.range_code)
# data_appa.range_code = "1000V"
# print(data_appa.range_code)


poll_time = 0.5


# ind_counts = 0

# main_rotor_code =0
# main_blue_code=0
# main_range_code = 0
# main_value_b=0
# main_value = 0

global time_receive
global data_receive



def send_port():
    # global ind_counts

    global main_rotor_code, main_blue_code, main_range_code
    global main_value_b, main_value
   
    if data_appa.index_count == 0:
        ser.write(data_send)
        time.sleep(0.5)
    data_receive = ser.readline()
   
    data_appa.time_receive = datetime.isoformat(
        datetime.now(), sep=' ', timespec='milliseconds')    

 
            
    if check_crc(data_receive):
        crc = "OK"

        appa_type = data_receive[0:4] # Получаем тип мультиметра
        if appa_type.hex() == "5555000e": # Для APPA 109N
            # main_status_bits = 0
            # point_code_bits = 0
            data_appa.index_count += 1

            data_appa.rotor_code = rotorcode(data_receive[4:5])

            data_appa.blue_code  = bluecode(data_receive[4:5] + data_receive[5:6])

            data_appa.range_code = rangecode(data_receive[4:5] + data_receive[5:6] + data_receive[7:8])  

            # main_value_b = int_to_bytes((tmp[8]<<16) | (tmp[9]<<8) | tmp[10])

            # main_value = int.from_bytes(main_value_b, byteorder = "little")     
            data_appa.main_read = int.from_bytes(
                data_receive[8:9]  + 
                data_receive[9:10] + 
                data_receive[10:11], 
                byteorder = "little")

           
            data_appa.main_pointcode = pointcode(bin(data_receive[11])[2:].zfill(8)[5:])
            data_appa.unitcode = unitcode(bin(data_receive[11])[2:].zfill(8)[0:5])            
           

            func_table = functiontable(data_receive[12:13])

            print(
                data_appa.index_count, 
                data_appa.time_receive, 
                value_to_float(data_appa.main_read, data_appa.main_pointcode), 
                data_appa.main_pointcode,
                data_appa.unitcode)
        else:
            print("Unidentified DMM")
            
    else:
        crc ="ER"
        print("CRC Error")

    


    ser.write(data_send)


appa_109n = "55 55 00 00 AA"
data_send = bytes.fromhex(appa_109n)

ser = serial.Serial(
    port     = "COM3", 
    parity   = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    xonxoff  = False,
    timeout  = 0)
    
ser.close()  

ser.open()
ser.flush()

# while True:
#     try:
#         if ser.is_open:
#             send_port(p_time)
#     except Exception as exc:
#         print("type: {0}, message: {1}".format(type(exc), str(exc)))
#         break


if ser.is_open:
    send_port() 
    rt = RepeatedTimer(poll_time, send_port)


try:
    time.sleep(5) # your long-running job goes here...
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!