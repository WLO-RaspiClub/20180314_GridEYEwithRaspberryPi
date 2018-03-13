#!/usr/bin/env python
import smbus
import time
bus = smbus.SMBus(1)
addr = 0x68
 
def color(temp):
        if temp <20 :
                return("\b\x1b[36m\x1b[7m..")
        if temp >=20 and temp<22 :
                return("\b\x1b[38;5;124m  \x1b[36m")
        if temp >=22 and temp<24 :
                return("\b\x1b[38;5;161m  \x1b[36m")
        if temp >=24 and temp<26 :
                return("\b\x1b[38;5;198m  \x1b[36m")
        if temp >=26 and temp<28 :
                return("\b\x1b[38;5;200m  \x1b[36m")
        if temp >=28 and temp<30 :
                return("\b\x1b[38;5;212m  \x1b[36m")
        if temp >=30 and temp<32 :
                return("\b\x1b[38;5;219m  \x1b[36m")
        if temp >=32 :
                return("\b\x1b[38;5;225m  \x1b[36m")
 
while 1:
        time.sleep(0.1)
        linedata=[]
        for i in range(8) :
                data = bus.read_i2c_block_data(addr , 0x80+0x10*i, 16) 
                oneline =[]
                for j in range(8) :
                       oneline.append( (int((data[2*j+1] & 0x07) *256 + data[2*j]))*0.25 )
                linedata.append(oneline)
#       print linedata
        print "\x1b[36m\x1b[7m0 1 2 3 4 5 6 7 "
        for i in range(8):
                for j in range(8):
                        print color(linedata[i][j]),
                print i
        print "\x1b[10F" #10 line move
