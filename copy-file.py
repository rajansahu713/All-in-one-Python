import os  
import shutil  
  
# Creating a new folder in the current directory  
os.mkdir('Python')  
  
# It will show the empty folder  
print('Empty Folder:', os.listdir('Python'))  
  
# testcompare.py file will be copied in the javatpoint folder  
shutil.copy('test.py', 'Python')  
  
# After coping the file folder shows the file  
print('File Copied Name:', os.listdir('Python'))  