import os
import shutil
#Lists of various file types
ImageTypes = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
TextTypes = ['.txt', '.doc', '.docx']
VideoTypes = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.mpg', '.mpeg', '.m4v', '.webm']
PDF = ['.pdf']
Filetypes = {}
#Creating a while loop so that the program doesn't just end if wrong input
Tries = 0
while Tries == 0:
#Input a filepath and then the files in that folder get listed out
  Filepath = input('Input the file path: ')
  Directory = Filepath
#Tries to list the directory inputed and if there's an error it lets the user retry
  try:
    ListDirectory = os.listdir(Directory)
    print(ListDirectory, '\n')
    Tries += 1
  except:
    print('Not a valid file path. The folder was not found.')
    Retry = input('Would you like to try again? Y/N: ')
    if Retry.lower() != 'y':
      Tries += 2
#Looping through the files and putting them in a dictionary if they're not in already
if Tries == 1:
  for file in ListDirectory:
    Extention = os.path.splitext(file)[1]
    if Extention not in Filetypes:
      Filetypes[Extention] = []
    Filetypes[Extention].append(file)
  print(Filetypes)
#Default or Custom folder names
  Rename = input('\nWould you like to rename your new folders? Y/N: ')
#Creates new folder if file type exists and if the folder doesn't exist already
  if Rename.lower() != 'y':
    if any(filetype in Filetypes for filetype in ImageTypes):
      ImageFolder = os.path.join(Directory, 'Images')
      os.makedirs(ImageFolder, exist_ok=True)

    if any(filetype in Filetypes for filetype in TextTypes):
      TextFolder = os.path.join(Directory, 'Text Documents')
      os.makedirs(TextFolder, exist_ok=True)

    if any(filetype in Filetypes for filetype in VideoTypes):
      VideoFolder = os.path.join(Directory, 'Videos')
      os.makedirs(VideoFolder, exist_ok=True)

    if any(filetype in Filetypes for filetype in PDF):
      PDFFolder = os.path.join(Directory, 'PDF')
      os.makedirs(PDFFolder, exist_ok=True)
    print('\nCreated!')
  else:
    if any(filetype in Filetypes for filetype in ImageTypes):
      ImageName = input('\nName your folder for images: ')
      ImageFolder = os.path.join(Directory, ImageName)
      os.makedirs(ImageFolder, exist_ok=True)

    if any(filetype in Filetypes for filetype in TextTypes):
      TextName = input('Name your folder for text documents: ')
      TextFolder = os.path.join(Directory, TextName)
      os.makedirs(TextFolder, exist_ok=True)

    if any(filetype in Filetypes for filetype in VideoTypes):
      VideoName = input('Name your folder for videos: ')
      VideoFolder = os.path.join(Directory, VideoName)
      os.makedirs(VideoFolder, exist_ok=True)
      
    if any(filetype in Filetypes for filetype in PDF):
      PDFName = input('Name your folder for PDFs: ')
      PDFFolder = os.path.join(Directory, PDFName)
      os.makedirs(PDFFolder, exist_ok=True)
    print('\nCreated!')