import os

Filenames = []
Filetypes = {}

Filepath = input('Input the file path: ')
Directory = Filepath
try:
  ListDirectory = os.listdir(Directory)
except:
  print('Not a valid file path. The folder was not found.')
  
print(ListDirectory)