import os, sys
import Image

im = Image.open("dog.png")
x = 3
y = 4

pix = im.load()
print pix[x,y]