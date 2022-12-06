#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import time
#ser = serial.Serial(21)     # open first serial port
#print ser.portstr       # check which port was really used
#ser.write("hello")      # write a string
#ser.close()             # close port

SIZE_OF_PD_PACKAGE = 114

class CommuInterface:
    def open(self, aport='COM68', abaudrate=115200) :
        print "aport", aport
        print "abaudrate", abaudrate
        self.sp = serial.Serial(
            port=aport,
            baudrate=abaudrate,     # baudrate
            bytesize=8,             # number of databits
            parity=serial.PARITY_NONE,
            stopbits=1,
            xonxoff=0,              # enable software flow control
            rtscts=0,               # disable RTS/CTS flow control
            timeout=None            # set a timeout value, None for waiting forever
        )

    def close(self):
        self.sp.close()

    def reset(self):
        self.sp.setDTR(0)
        time.sleep(0.1)
        self.sp.setDTR(1)
        time.sleep(0.5)

    def _wait_for_ask(self, info = ""):
        # wait for ask
        try:
            ask = ord(self.sp.read())
        except:
            raise CmdException("Can't read port or timeout")
        else:
            if ask == 0x79:
                # ACK
                return 1
            else:
                if ask == 0x1F:
                    # NACK
                    raise CmdException("NACK "+info)
                else:
                    # Unknow responce
                    raise CmdException("Unknow response. "+info+": "+hex(ask))

    def initChip(self):
        # Set boot
        self.sp.setRTS(0)
        self.reset()
#        self.sp.write("a")
#        data = self.sp.read(69)
#        print "Readback" +data
#        self.sp.write("\x7F")       # Syncro
#        return self._wait_for_ask("Syncro")

    def releaseChip(self):
        self.sp.setRTS(1)
        self.reset()

    def cmdGeneric(self, cmd):
        self.sp.write(chr(cmd))
        self.sp.write(chr(cmd ^ 0xFF)) # Control byte
        return self._wait_for_ask(hex(cmd))

    def cmdSilPDVerCheck(self):
        self.sp.write("PDVERCK\n")
        version = self.sp.read(8) # reply should be "SI_PD_VER_XXX\n"
        print "xxx" + version
        if(0 == cmp(version[0:5],"PDVER")):
            print version[5:8]
            return version[5:8]
        else:
            return False

    def cmdSendGoodREC(self):
        time.sleep(0.1)
        self.sp.write("GOODREC\n")

    def cmdStartCapture(self, package_size):
        PD_package = self.sp.read(package_size)
        # print PD_package
        # print len(PD_package)
        if len(PD_package) == SIZE_OF_PD_PACKAGE:
            # print "Receive valid PD package data"
            # print "start to send the GOODREC xS later"
            # time.sleep(3)
            self.cmdSendGoodREC()
            # print "end to send the GOODREC\n\n"
            #def cmdStartCapture(self, package_size):
        return PD_package

    def cmdGet(self):
        if self.cmdGeneric(0x00):
            mdebug(10, "*** Get command");
            len = ord(self.sp.read())
            version = ord(self.sp.read())
            mdebug(10, "    Bootloader version: "+hex(version))
            dat = map(lambda c: hex(ord(c)), self.sp.read(len))
            mdebug(10, "    Available commands: "+str(dat))
            self._wait_for_ask("0x00 end")
            return version
        else:
            raise CmdException("Get (0x00) failed")

    def cmdGetVersion(self):
        if self.cmdGeneric(0x01):
            mdebug(10, "*** GetVersion command")
            version = ord(self.sp.read())
            self.sp.read(2)
            self._wait_for_ask("0x01 end")
            mdebug(10, "    Bootloader version: "+hex(version))
            return version
        else:
            raise CmdException("GetVersion (0x01) failed")

# conf = {
        # 'port': 'COM68',
        # 'baud': 115200,
        # 'address': 0x00001000,
        # 'erase': 0,
        # 'write': 0,
        # 'verify': 0,
        # 'read': 0,
        # 'len': 1000,
        # 'fname':'',
        # }

# cmd = CommuInterface()

# cmd.open(conf['port'],conf['baud'])
# if cmd.cmdSilPDVerCheck():
    # cmd.cmdSendGoodREC()
    # print "Start to capture PD data"
    # cmd.cmdStartCapture(114, 4)


# cmd.reset()
# cmd.close()








#import time
#from communication import CommuInterface

tmpBuffSize = SIZE_OF_PD_PACKAGE * 4;

conf = {
        'port': 'COM68',
        'baud': 115200,
        'address': 0x00001000,
        'erase': 0,
        'write': 0,
        'verify': 0,
        'read': 0,
        'len': 1000,
        'fname':'',
        }

cmd = CommuInterface()
cmd.open(conf['port'],conf['baud'])

fp = open('data.pd', 'w')

if cmd.cmdSilPDVerCheck():
    cmd.cmdSendGoodREC()
    print "Start to capture PD data"
    pdDataLength = 0;
    # pdData = cmd.cmdStartCapture(114)
    # print pdData
    # pdLength = len(pdData)
    # print "%d" % pdLength
    while (pdDataLength < 114*259):
        pdData = cmd.cmdStartCapture(114)
        fp.write(pdData)
        print pdData
        print "%d" % ord(pdData[6])
        pdLength = len(pdData)
        # print "pdLength = %d" % pdLength
        pdDataLength += pdLength
        print "pdDataLength = %d count = %d" % (pdDataLength, (pdDataLength/114))
        # if (pdDataLength/114) == 253:
            # print "start sleep....."
            # time.sleep(10)


cmd.reset()
cmd.close()









