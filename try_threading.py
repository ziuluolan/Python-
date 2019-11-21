import threading 
import time

def write(name,word,sleep_time):
	for i in range(10):
		time.sleep(sleep_time)
		print(name+"----"+word+"----")


#target指向调用子线程去执行的函数，args 为一个元组执行函数接收的参数 
t1 = threading.Thread(target = write,args = ("thread1","hello",0.5))
t2 = threading.Thread(target = write,args = ("thread1","word",1))
for t in [t1,t2]:
	t.setDaemon(True)#设置为守护进程，意味着该线程不重要，主线程结束子线程直接结束
	t.start()
#调用join方法，让主线程等待子线程结束
for t in [t1,t2]:
	t.join()
print("end progress")


