import sublime, sublime_plugin,subprocess,threading

class OpeninexcelCommand(sublime_plugin.ApplicationCommand):
	def run(self,paths):
		thread1 = myThread(1,"Thread-1",1,paths[0])
		thread1.start()

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter,path):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.path = path
    def run(self):
        print ("Starting " + self.name)
        command = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE " + '"' +   self.path + '"'
        print (command)
        subprocess.call(command)
        print ("Exiting " + self.name)