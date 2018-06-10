# Colab
Exploration of Google Colaboratory and Machine Learning

#### Introduction 
Installing the various software required to run Python and Tensorflow is tedious, especially if you are unfamiliar with Python and Linux or have slow and limted access to internet. However Google introduced a cloud service with a web based interface that uses IPython. With Python and Tensorflow already installed. Perfect so lets gets started!

1. https://www.python.org/
1. https://www.tensorflow.org/
1. https://cloud.google.com/
1. https://ipython.org/
1. https://guides.github.com/features/mastering-markdown/

## Project Goals 

- [x] Learn Colab
- [x] Learn Python
- [ ] Learn Machine Learning
- [ ] Learn Tensorflow

## Learn Colab

#### Introduction 
Setup is easy, all you need is a Google Account and follow the link to Google Colab and sign-in

1. https://accounts.google.com/SignUp
2. https://colab.research.google.com/

#### Hello World
This link allows you to view a hello world example. If you want to edit it you can click on "OPEN IN PLAYGROUND" or save a copy to you Google Drive.

Colab Notebookhttps://colab.research.google.com/drive/1S0O_NkZ9Z-tlYzGLDJuRi3Qd4mQQQQIR

## Learn Python

#### Learning resources

1. http://cs231n.github.io/python-numpy-tutorial/

#### Write a IPython Magic class from scratch
The goal of this project is to learn how IPython Magic works and add the ablity to run and display the output of other
programming languages like Node, C, C++

1. http://ipython.readthedocs.io/en/stable/interactive/magics.html

https://colab.research.google.com/drive/12MUJ1bfxf0vNW9GCh6-tchKc3BMWzhkN

```
import subprocess
import IPython.core.magic as ipy
from IPython import get_ipython

@ipy.magics_class
class Cowboy(ipy.Magics):

    @ipy.cell_magic
    def Cowboy(self, line, cell):
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

get_ipython().register_magics(Cowboy)
```
