import sublime, sublime_plugin,subprocess,threading,tempfile,os

class createpackagesCommand(sublime_plugin.WindowCommand):

    def run(self,paths):
        self.path = paths[0]
        self.objectTypePrompt();

    def objectTypePrompt(self):
        self.window.show_input_panel("Object Type","",self.containerIDPrompt,"","") 
  
    def containerIDPrompt(self,user_input):
        self.objectType = user_input
        self.window.show_input_panel("Container ID","",self.passwordPrompt,"","")      

    def passwordPrompt(self,user_input):
        self.containerID = user_input
        self.window.show_input_panel("Password","",self.createXML,"","");

    def createXML(self,user_input):
        self.password = user_input
        self.scriptFile = tempfile.mkstemp()
        f = open(self.scriptFile[1],'w')
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<ProjectMerge>\n  <Preview>\n  </Preview>\n  <MigrationAction>3</MigrationAction>\n  <GenerateUndoPackage>\n  </GenerateUndoPackage>\n  <ImportPackage>\n  </ImportPackage>\n  <PackageFile>'+self.path+'\\'+self.objectType+'.mmp</PackageFile>\n  <AddDependents>No</AddDependents>\n  <ContainerID>'+self.containerID+'</ContainerID>\n  <Connections>\n    <SourceConnection>\n      <Location>elvmad746</Location>\n      <Project>Console</Project>\n      <ConnectionMode>3-tier</ConnectionMode>\n      <AuthenticationMode>Standard</AuthenticationMode>\n      <Login>administrator</Login>\n    </SourceConnection>\n  </Connections>\n  <Rules>\n    <Operations>\n      <CategoryLevel>\n        <Application>\n          <Replace />\n        </Application>\n        <Configuration>\n          <KeepBoth />\n        </Configuration>\n        <Schema>\n          <Replace />\n        </Schema>\n      </CategoryLevel>\n    </Operations>\n    <Options>\n      <Option>\n        <ID>ACL</ID>\n        <UseExisting />\n      </Option>\n      <Option>\n        <ID>UpdateSchema</ID>\n        <SchemaUpdateNoneSchemaUpdateRefreshSchema />\n      </Option>\n      <Option>\n        <ID>OMOnOffSettings</ID>\n        <None />\n      </Option>\n    </Options>\n  </Rules>\n  <Logs>\n    <Log>\n      <File>c:\Temp\PrjMrg.Log</File>\n      <LogLevel>All</LogLevel>\n    </Log>\n  </Logs>\n</ProjectMerge>')
        f.close()
        os.close(self.scriptFile[0])
        self.window.open_file(f.name)
        print('Attempting to start thread.\n')
        self.runThread()

    def runThread(self):
        thread1 = myThread1(1,"Thread-1",1,self.password,self.scriptFile)
        thread1.start()


class myThread1 (threading.Thread):
    def __init__(self, threadID, name, counter,password,scriptFile):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.password = password
        self.scriptFile = scriptFile
        
    def run(self):
        print ("Starting " + self.name)
        command = 'projectmerge.exe -f"'+self.scriptFile[1]+'" -sp'+self.password+' -smp'+self.password
        CREATE_NO_WINDOW = 0x08000000
        subprocess.check_call(command,creationflags=CREATE_NO_WINDOW)
        os.remove(self.scriptFile[1])
        print ("Exiting " + self.name)