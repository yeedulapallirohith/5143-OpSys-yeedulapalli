#import files
import os
import stat
import sys
import time
import subprocess
import shutil


class historyManager(object):
    def __init__(self):
        self.command_history = []
		
    def push_command(self,cmd):
        self.command_history.append(cmd)
		
    def get_commands(self):
        return self.command_history
		
    def number_commands(self):
        return len(self.command_history)
		
class parserManager(object):
    def __init__(self):
        self.parse_list = []
        
    def parse(self,cmd):
        self.parse_list = cmd.split(" ")
        return self.parse_list
		
class commandManager(parserManager,historyManager):
    def __init__(self):
        self.command = None
		
    def run_command(self,cmd):
        self.command = cmd
        self.command = self.parse(self.command)
        return self.command
       
    def listing(self):
        path=os.getcwd()
        files = []
        files=os.listdir(path)
        return files
        
		
    def ls(self,parse_list): # file listing in specified formats
        try:
            if(parse_list[0]=='ls' and parse_list[1]=='-l'):
                files=[]
                files=self.listing()
                print(" File Name         Size       Permissions       Accessed Time                  Modified Time                        changed time")
                print("-----------        -----      ------------      --------------                 --------------                       ------------")
                for x in range(0,len(files)):
                    print(files[x],'\t\t  ',(os.stat(files[x]).st_size),'\t\t',(oct(os.stat(files[x])[stat.ST_MODE])[-3:]),'\t\t',(time.ctime(os.path.getmtime(files[x]))),'\t',(time.ctime(os.stat(files[x]).st_atime)),'\t',(time.ctime(os.stat(files[x]).st_ctime)))
            elif(parse_list[0]=='ls' and parse_list[1]=='-a'):
                files=[]
                path=os.getcwd()
                atime = lambda f: os.stat(os.path.join(path, f)).st_atime
                files= list(sorted(os.listdir(path), key=atime))
                print(" File Name         Size       Permissions       Accessed Time                        Modified Time                  changed time")
                print("-----------        -----      ------------      --------------                       --------------                 ------------")
                for x in range(0,len(files)):
                   print(files[x],'\t\t  ',(os.stat(files[x]).st_size),'\t\t',(oct(os.stat(files[x])[stat.ST_MODE])[-3:]),'\t\t',(time.ctime(os.path.getmtime(files[x]))),'\t',(time.ctime(os.stat(files[x]).st_atime)),'\t',(time.ctime(os.stat(files[x]).st_ctime)))
            elif(parse_list[0]=='ls' and parse_list[1]=='-m'):
                files=[]
                path=os.getcwd()
                mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
                files= list(sorted(os.listdir(path), key=mtime))
                print(" File Name         Size       Permissions       Accessed Time                        Modified Time                  changed time")
                print("-----------        -----      ------------      --------------                       --------------                 ------------")
                for x in range(0,len(files)):
                    print(files[x],'\t\t  ',(os.stat(files[x]).st_size),'\t\t',(oct(os.stat(files[x])[stat.ST_MODE])[-3:]),'\t\t',(time.ctime(os.path.getmtime(files[x]))),'\t',(time.ctime(os.stat(files[x]).st_atime)),'\t',(time.ctime(os.stat(files[x]).st_ctime)))   
            elif(parse_list[0]=='ls' and parse_list[1]=='-c'):
                files=[]
                path=os.getcwd()
                ctime = lambda f: os.stat(os.path.join(path, f)).st_ctime
                files= list(sorted(os.listdir(path), key=ctime))
                print(" File Name         Size       Permissions       Accessed Time                        Modified Time                  changed time")
                print("-----------        -----      ------------      --------------                       --------------                 ------------")
                for x in range(0,len(files)):
                    print(files[x],'\t\t  ',(os.stat(files[x]).st_size),'\t\t',(oct(os.stat(files[x])[stat.ST_MODE])[-3:]),'\t\t',(time.ctime(os.path.getmtime(files[x]))),'\t',(time.ctime(os.stat(files[x]).st_atime)),'\t',(time.ctime(os.stat(files[x]).st_ctime)))               
            else:
                print("command not found")
        except IndexError:
            print("File listing") 
            print("------------")
            for f in self.listing():
                print(f)
            print("------------")
		
		
    def cat(self,file): # dispalying a file( read mode )
        try:
            f = open(file,'r')
            text = f.read()
            print(text)
            f.close()
        except FileNotFoundError:
            print("No such file or directory")
		
		
    def cd(self,parse_list): # all formats of changing directories
        try:	
            if(parse_list[0]=='cd' and parse_list[1]=='..'):
                os.chdir("..")
            elif(parse_list[0]=='cd' and parse_list[1]=='~'):
                os.chdir((os.path.expanduser('~')))
            else:
                if(parse_list[1]):
                    os.chdir(os.path.join(os.getcwd(),parse_list[1]))       
        except FileNotFoundError:
            print("Specified directory doesn't exist")
            
    def cp(self,file1,file2): # copying files
        if(os.path.isfile(file1)):
            if(os.path.isfile(file2)):
                shutil.copyfile(file1, file2)
                print("copy successful")
            else:
                file = open('file2','w+')
                shutil.copyfile(file1, file2)
                print("copy successful")
        else:
            print("No such file or directory")
		
    def mv(self,file1,file2): #renaming files
        if(os.path.isfile(file1)):
            os.rename(file1,file2)
        else:
            print("No such file or directory")
			
    def rm(self,file): #removing files
        if(os.path.isfile(file)):
            os.remove(file)
        else:
            print("No such file or directory")
        
    def chmod(self,parse_list): # changing file access permissions of file
        try:
            if(os.path.isfile(parse_list[2])):
                subprocess.call(['chmod',parse_list[1], parse_list[2]])	
            else:
                print("No such file or directory")							
        except (ValueError,IndexError):
            print("missing operand")
		
    def wc(self,parse_list): # computing counts of word,lines and characters
        try:
            if(parse_list[0]=="wc" and parse_list[1]=="-l"):
                if(os.path.isfile(parse_list[2])):
                    self.linecount =0
                    with open(parse_list[2], 'r') as f:
                        for line in f:
                            self.linecount += 1
                    print(" %d %s" %(self.linecount,parse_list[2]))
                else:
                    print("no such file or directory")

            else:
                self.line_count = 0
                self.word_count = 0
                self.char_count = 0
                if(os.path.isfile(parse_list[1])):
                    with open(parse_list[1],'r') as f:
                        for line in f:
                            self.words = line.split()
                            self.line_count += 1
                            self.word_count += len(self.words)
                            self.char_count += len(line)
                    print(" %d  %d %d %s"%(self.line_count,self.word_count,self.char_count,parse_list[1]))
                else:
                    print("No such file or directory")
        except IndexError:
            print("command not found")

class driver(object):
    def __init__(self):
        self.history = historyManager()
        self.commands = commandManager()
        self.number_commands = 0
    def runShell(self):
        number_commands = 0
        while True:
            self.input = input("parser-$ ")      
            self.history.push_command(self.input)   
            parse_list = self.commands.run_command(self.input)
            if(parse_list[0]=='history'): # printing history
                history=[]
                history=self.history.get_commands()
                for x in range(0,self.history.number_commands()): 
                    print(" %d %s"%(x+1,history[x])) 
            elif(parse_list[0]=='cat'):
                self.commands.cat(parse_list[1])
            elif(parse_list[0]=='cd'):
                self.commands.cd(parse_list)
            elif(parse_list[0]=='cp'):
                self.commands.cp(parse_list[1],parse_list[2])
            elif(parse_list[0]=='wc'):
                self.commands.wc(parse_list)    
            elif(parse_list[0]=='mv'):
                self.commands.mv(parse_list[1],parse_list[2])
            elif(parse_list[0]=='rm'):
                self.commands.rm(parse_list[1])
            elif(parse_list[0]=='ls'):
                self.commands.ls(parse_list)
            elif(parse_list[0]=='chmod'):
                self.commands.chmod(parse_list)
            else:
                print("command not found")
				
if __name__=="__main__":
    d = driver()    
    d.runShell()

