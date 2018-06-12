# Colab
Exploration of Google Colaboratory and Machine Learning

#### Introduction 
Installing the various software required to run Python and Tensorflow is tedious, especially if you are unfamiliar with Python and Linux or have slow and limted access to internet. However Google introduced a cloud service with a web based interface that uses IPython. With Python and Tensorflow already installed. Perfect so lets gets started!

Links
* https://www.python.org/
* https://www.tensorflow.org/
* https://cloud.google.com/
* https://ipython.org/
* https://guides.github.com/features/mastering-markdown/

## Project Goals 

- [x] Learn Colab
- [x] Learn Python
- [ ] Learn Machine Learning
- [ ] Learn Tensorflow

## Learn Colab

#### Introduction 
Setup is easy, all you need is a Google Account and follow the link to Google Colab and sign-in

Links
* https://accounts.google.com/SignUp
* https://colab.research.google.com/

#### Hello World
This link allows you to view a hello world example. If you want to edit it you can click on "OPEN IN PLAYGROUND" or save a copy to you Google Drive.

Links
* https://colab.research.google.com/drive/1S0O_NkZ9Z-tlYzGLDJuRi3Qd4mQQQQIR

```
print("hello world")
```
## Learn Python

#### Learning resources

Links
* http://cs231n.github.io/python-numpy-tutorial/

#### Write a IPython Magic class from scratch
The goal of this project is to learn how IPython Magic works and add the ablity to run and display the output of other
programming languages like Javascript, C, C++

- [x] Execute Python code inside cell with Python
- [x] Execute C++ code inside cell with Gcc
- [x] Execute Javascript code inside cell with Node

Links
* http://ipython.readthedocs.io/en/stable/interactive/magics.html

```
import subprocess
import IPython.core.magic as ipy
from IPython import get_ipython

@ipy.magics_class
class Cowboy_Magic(ipy.Magics):

    @ipy.cell_magic
    def Cowboy_Magic(self, line, cell):
        options = line.split(" ")

        with open(options[1], 'w', encoding="utf-8") as f:
          f.write(cell)

        process = subprocess.Popen(
          options,
          stdout=subprocess.PIPE,
          stderr=subprocess.STDOUT
        )

        a,b = process.communicate()
        print(a.decode("utf-8"))

get_ipython().register_magics(Cowboy_Magic)
```

Examples
* https://colab.research.google.com/drive/12MUJ1bfxf0vNW9GCh6-tchKc3BMWzhkN

#### Write a Python Class that accesses Google Drive
The goal of this project is to learn how Google Auth and Google Drive API works adding the ability to access Google Drive like a local drive inside a Colab Notebook. The primary reason for this functionality is to provide the ability to import libraries directly from Google Drive into separate Google Notebooks

- [x] Query files
- [x] List files
- [x] Make new folder
- [x] Change current folder
- [x] Push local file into current drive folder
- [x] Pull drive file from current drive folder into local drive
- [x] Use Cowboy_Magic to save cell to local drive
- [x] Use Cowboy_Drive to upload file to Google Drive
- [x] Use Cowboy_Drive to download file from Google Drive and import locally

Links
* https://developers.google.com/api-client-library/python/
* https://github.com/google/google-api-python-client
* https://github.com/google/oauth2client (deprecated)
* https://google-auth.readthedocs.io/en/latest/
* https://github.com/googlecolab/colabtools
* https://developers.google.com/drive/api/v3/about-sdk
* https://www.youtube.com/watch?v=-7YH6rdR-tk

```
from google.colab import auth
auth.authenticate_user()

import google.auth
from apiclient import http
from apiclient.discovery import build
import io 

class Cowboy_Drive:
  folderType = 'application/vnd.google-apps.folder'
  
  def __init__(self):
    self.files = drive.files()
    self.folder_id = 'root'
  
  def query(self,q):
    fields = 'files(name, id, mimeType)'
    results = self.files.list(q=q, fields=fields).execute()
    return results.get('files', [])
  
  def exists(self,name,mimeType=None):
    for item in self.list:
      if item['name'] == name:
        if mimeType is None: 
          return item
        if item['mimeType'] == mimeType:
          return item
    return None
        
  def dir(self):
    q = "'{}' in parents and trashed=false".format(self.folder_id)
    self.list = self.query(q)
    return self.list
  
  def chdir(self,name):
    if name != 'root':
      out = self.exists(name,self.folderType)
      if not out is None:
          self.folder_id = out['id']
    else:
      self.folder_id = 'root'

  def mkdir(self,name):
    body = {'name': name,'mimeType': self.folderType,'parents': [self.folder_id]}
    file = self.files.create(body=body,fields='id,parents').execute()
        
  def push(self,name):
    body = {'name': name,'parents': [self.folder_id]}
    media_body = http.MediaFileUpload(name)
    file = self.files.create(body=body,media_body=media_body,fields='id,parents').execute()
    self.file_id = file.get('id')
    
  def pull(self,name):
    file_id = self.exists(name)['id']
    request = self.files.get_media(fileId=file_id)
    fh = io.FileIO(name, 'wb')
    downloader = http.MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
      status, done = downloader.next_chunk()
```
Example
* https://colab.research.google.com/drive/1UQW1izGUmZWi7aeioULJMYz1fcznokcX

## Learn Machine Learning

Links
* http://karpathy.github.io/neuralnets/
* http://cs231n.github.io/

## Learn Tensorflow

Links

