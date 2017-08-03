# -*- coding=utf-8 -*-

#import json
#
#def student2dict(std):
#	return{'name':std.name, 'age':std.age, 'score':std.score}
#
#def dict2student(d):
#	return Student(d['name'], d['age'], d['score'])
#
#class Student(object):
#	def __init__(self, name, age, score):
#		self.name = name
#		self.age = age
#		self.score = score
#
#def main1():
#	s = Student('Bob', 20, 88)
#	print(json.dumps(s, default=student2dict))
#	print(json.dumps(s, default=lambda obj: obj.__dict__))
#
#	json_str = '{"age": 20, "score": 88, "name": "Bob"}'
#	print(json.loads(json_str, object_hook=dict2student))

#import os
#from multiprocessing import Process
#
#def run_proc(name):
#	print 'Run child process %s (%s)...' % (name, os.getpid())
#
#def main():
#	print 'Parent process %s.' % os.getpid()
#	p = Process(target=run_proc, args=('test',))
#	print 'Process will start'
#	p.start()
#	p.join()
#	print 'Process end.'
#
#from multiprocessing import Pool
#import os, time, random
#
#def long_time_task(name):
#	print 'Run task %s (%s)...' % (name, os.getpid())
#	start = time.time()
#	time.sleep(random.random() * 3)
#	end = time.time()
#	print 'Task %s runs %0.2f seconds' % (name, (end-start))
#	
#def main():
#	print 'Parent process %s.' % os.getpid()
#	p = Pool(5)
#	for i in range(5):
#		p.apply_async(long_time_task, args=(i,))
#	print 'Waiting for all subprocesses done...'
#	p.close()
#	p.join()
#	print 'All subprocesses done.'
#
#from multiprocessing import Process, Queue
#import os, time, random
#
#def write(q):
#	for value in ['A', 'B', 'C']:
#		print 'Put %s to queue...' % value
#		q.put(value)
#		time.sleep(random.random())
#
#def read(q):
#	while True:
#		value = q.get(True)
#		print 'Get %s from queue.' % value
#
#def main():
#	q = Queue()
#	pw = Process(target=write, args=(q,))
#	pr = Process(target=read, args=(q,))
#	pw.start()
#	pr.start()
#	pw.join()
#	pr.terminate()
#
#import time, threading
#
#def loop():
#	print 'thread %s is running...' % threading.current_thread().name
#	n = 0
#	while n < 5:
#		n = n + 1
#		print 'thread %s >>> %s' % (threading.current_thread().name, n)
#		time.sleep(1)
#	print 'thread %s ended.' % threading.current_thread().name
#
#def main():
#	print 'thread %s is running...' % threading.current_thread().name
#	t = threading.Thread(target=loop, name='LoopThread')
#	t.start()
#	t.join()
#	print 'thread %s ended.' % threading.current_thread().name
#
#import time, threading
#
#balance = 0
#lock = threading.Lock()
#
#def change_it(n):
#	global balance
#	balance = balance + n
#	balance = balance - n
#
#def run_thread(n):
#	for i in range(100000):
#		lock.acquire()
#		try:
#			change_it(n)
#		finally:
#			lock.release()
#
#def main():
#	t1 = threading.Thread(target=run_thread, args=(5,))
#	t2 = threading.Thread(target=run_thread, args=(8,))
#	t1.start()
#	t2.start()
#	t1.join()
#	t2.join()
#	print balance
#
import threading

local_school = threading.local()

def process_student():
	print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
	local_school.student = name
	process_student()

def main():
	t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
	t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
	t1.start()
	t2.start()
	t1.join()
	t2.join()

if __name__ == '__main__':
	main()
