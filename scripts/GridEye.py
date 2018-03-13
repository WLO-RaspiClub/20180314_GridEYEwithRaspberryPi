# -*- coding: utf-8 -*-

import smbus


class GridEye:
    __REG_FPSC = 0x02
    __REG_TOOL = 0x0E
    __REG_PIXL = 0x80

    def __init__(self, address=0x68):
        self.i2c = smbus.SMBus(1)   # 0 for Raspberry Pi Model B(256MB)
        self.address = address
        self.i2c.write_byte_data(self.address, self.__REG_FPSC, 0x00)

    def thermistorTemp(self):
        result = self.i2c.read_word_data(self.address, self.__REG_TOOL)
        if(result > 2047):
            result = result - 2048
            result = -result
        return result * 0.0625

    def pixelOut(self):
        out = []
        for x in xrange(0, 64):
            temp = self.i2c.read_word_data(
                self.address, self.__REG_PIXL + (x * 2))
            if(temp > 2047):
                temp = temp - 4096
            out.append(temp * 0.25)
        return out
