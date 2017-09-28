#!/usr/bin/env python
# coding: utf-8
#
# Copyright (C) 2017 hidenorly
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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