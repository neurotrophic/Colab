# Cowboy Coder
# https://github.com/neurotrophic

from google.colab import auth
import google.auth
from apiclient import http
from apiclient.discovery import build
import io 

auth.authenticate_user()

class Cowboy_Drive:
  folderType = 'application/vnd.google-apps.folder'
  
  def __init__(self):
    credentials, project = google.auth.default()
    drive = build('drive', 'v3', credentials=credentials)
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
    

import subprocess
import IPython.core.magic as ipy
from IPython import get_ipython

# Usage %%Cowboy [g++, node, ...] [file.c, file.cpp, ...] [flags, ...]

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
