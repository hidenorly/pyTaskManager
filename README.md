# pyTaskManager

This is utility class to manage tasks running in worker threads.

You can use this as Java's concurrent executor but different.
(For instance, Future.get() is not implemented. This is a kind of just worker thread manager as of now.)

What you need to do are
 * to derive ```PyTask``` class
 * and override onExecute() on your derived class
 * and register the instance to ```PyTaskManager``` with ```addTask()```.
 * and execute registered tasks with ```executeAll()```
 * and join (wait to finish) tasks with ```finalize()```


# How to use

```
import time
from pyTaskManager import PyTask,PyTaskManager

class MyTask(PyTask):
	def __init__(self, description = ""):
		super(MyTask, self).__init__(description)

	def onExecute(self):
		print "MyTask is running...(" + self.description + ")"
		for i in range(10):
			time.sleep(0.1)
			if True == self.mStopRunning:
				break

if __name__ == '__main__':
	taskMan = PyTaskManager(4); # using 4 threads
	taskMan.addTask(MyTask("task-1"));
	taskMan.addTask(MyTask("task-2"));
	taskMan.addTask(MyTask("task-3"));
	taskMan.addTask(MyTask("task-4"));
	taskMan.addTask(MyTask("task-5"));
	taskMan.executeAll();

	time.sleep(1)
	taskMan.finalize();
```

You can use ```cancelTask(yourTask)```, ```stopAll()``` on ```TaskManager```.

And on your derived class of ```PyTask```, you can refer to ```mStopRunning``` in ```onExecute()``` for checking your thread is needed to stop or not.


# Confirmed environment

## Ubuntu 16.04.3 LTS

```
$ python --version
Python 2.7.12
$ python3 --version
Python 3.5.2
```

## Mac OS X 10.11.6

```
$ python --version
Python 2.7.13
$ python3 --version
Python 3.6.1
```
