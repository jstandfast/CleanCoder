import time
import os.path,subprocess
from subprocess import STDOUT,PIPE

def compile_java(path, java_file):
  os.chdir(path)
  cmd = 'javac ' + java_file
  subprocess.Popen(cmd, shell=True)

def execute_java(path, java_file):
  os.chdir(path)
  class_file = java_file + '.class'

  # Added delay since this was running prior to creation of class file
  while not os.path.isfile(os.getcwd() + '\\' + class_file):
    time.sleep(.01)

  output = subprocess.check_output('java ' + java_file, shell=True)
  print(output.decode('utf-8'))