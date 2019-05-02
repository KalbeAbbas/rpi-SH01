from SH01 import*
#import time
SH01=SH01()

while True:
 btn=SH01.read_button()

 if (btn=='Triangle'):
     print('Triangle')
     #device.touch=1

 if (btn=='Cross'):
     print('Cross')
     #device.touch=2
     
 time.sleep(0.1)
