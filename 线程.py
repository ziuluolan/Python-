import threading 
import time

def write(name,word,sleep_time):
	for i in range(10):
		time.sleep(sleep_time)
		print(name+"----"+word+"----")

t1 = threading.Thread(target = write,args = ("thread1","hello",0.5))
t2 = threading.Thread(target = write,args = ("thread1","word",1))
for t in [t1,t2]:
	t.setDaemon(True)
	t.start()
#等待子线程结束
for t in [t1,t2]:
	t.join()
print("end progress")


