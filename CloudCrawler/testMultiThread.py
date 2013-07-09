import threading  
import time  
class timer(threading.Thread): #The timer class is derived from the class threading.Thread  
    def __init__(self, num, interval):  
        threading.Thread.__init__(self)  
        self.thread_num = num  
        self.interval = interval  
        self.thread_stop = False  
   
    def run(self): #Overwrite run() method, put what you want the thread do here  
        while not self.thread_stop:  
            print 'Thread Object(%d), Time:%s/n' %(self.thread_num, time.ctime())  
            time.sleep(self.interval)  
    def stop(self):  
        self.thread_stop = True  
         
      
if __name__ == '__main__':  
    test()  