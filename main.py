import os

Filenames = []
Filetypes = {}
# Creating a while loop so that the program doesn't just end if wrong input
Tries = 0
while Tries == 0:
# Input a filepath and then the files in that folder get listed out
  Filepath = input('Input the file path: ')
  Directory = Filepath
# Tries to list the directory inputed and if there's an error it lets the user retry
  try:
    ListDirectory = os.listdir(Directory)
    print(ListDirectory)
    Tries += 1
  except:
    print('Not a valid file path. The folder was not found.')
    Retry = input('Would you like to try again? Y/N ')
    if Retry.lower() != 'y':
      Tries += 1