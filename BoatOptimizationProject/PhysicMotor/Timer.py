import time 

class Timer(object):  
    def __enter__(self):  
        self.start()  
        # __enter__ must return an instance bound with the "as" keyword  
        return self  
      
    # There are other arguments to __exit__ but we don't care here  
    def __exit__(self, *args, **kwargs):   
        self.stop()  
      
    def start(self):  
        if hasattr(self, 'interval'):  
            del self.interval  
        self.start_time = time.time()  
  
    def stop(self):  
        if hasattr(self, 'start_time'):  
            self.interval = time.time() - self.start_time  
            del self.start_time # Force timer reinit  


"""  
with Timer() as timer:  
    content = call_server()  
    result = process_data(content)  
print 'Total time in seconds for first call:', timer.interval 
"""

class LoggerTimer(Timer):  
    @staticmethod  
    def default_logger(msg):  
        print (msg)
  
    def __init__(self, prefix='', func=None):  
        # Use func if not None else the default one  
        self.f = func or LoggerTimer.default_logger  
        # Format the prefix if not None or empty, else use empty string  
        self.prefix = '{0}:'.format(prefix) if prefix else ''  
  
    def stop(self):  
        # Call the parent method  
        super(LoggerTimer, self).stop()  
        # Call the logging function with the message  
        self.f('{0}{1}'.format(self.prefix, self.interval)) 
        
"""
# With default print function  
with LoggerTimer('Server call and processing'):  
    content = call_server()  
    result = process_data(content)  
  
# With custom logging function  
import logging  
logger = logging.getLogger('loggertimer.test')  
with LoggerTimer('Server call and processing', logger.debug):  
    content = call_server()  
    result = process_data(content) 
    
"""
if (__name__ == '__main__'):
    def f():
        a=1
        for i in range(100000):
            a += i
            
    with LoggerTimer('Function'):
        f()