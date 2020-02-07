import ctypes,sys

def crc(command):
     mask = 0xfffffff7
     idx = 0
     
     initial = 0x07
     tagret  = 0x0
     poly  = 0xb0
     crc_mask = 0x07
     
     command = command & mask
     crc = initial
     idx = 32
     while idx > 0 :
          idx-=1
          if (0<(command & 0x80000000)): 
               bit = 0x01
          else:  
               bit = 0x00
          if (0!=bit ) : 
               crc = ((crc << 1) + bit) ^ poly
          else:          
               crc = ((crc << 1) + bit)
          crc = crc & crc_mask
          command = (command << 1) & 0xffffffff
     return crc

#testing with real commands          
def main(argv):
     #mosi
     expected_crc = 0x7 & 0xC0000008
     calculated_crc =  crc(0xC0000008)
     
     expected_crc = 0x7 & 0x21000018
     calculated_crc =  crc(0x21000018)
     
     expected_crc = 0x7 & 0x8000000C
     calculated_crc =  crc(0x8000000C)
     
     #miso
     expected_crc = 0x7 & 0x02200080
     calculated_crc =  crc(0x02200080)
     
     expected_crc = 0x7 & 0x00060764
     calculated_crc =  crc(0x00060764)
     
     expected_crc = 0x7 & 0x021000C1
     calculated_crc =  crc(0x021000C1)
     
     expected_crc = 0x7 & 0x021FFFC5
     calculated_crc =  crc(0x021FFFC5)
     

if __name__ == "__main__":
     main(sys.argv[1:])