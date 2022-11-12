from random import randint
from PIL import Image, ImageColor
from time import time
from os import getcwd, mkdir
photo = Image.new(mode = 'RGBA', size = (850,1100))

for width in range (850):
    for height in range(1100):
        r,g,b = randint(0,255) , randint(0,255), randint(0,255)
        photo.putpixel((width,height), (r,g,b))
print(r,g,b)




dir = getcwd()+"/Pics"
try:
    photo.save(getcwd()+"/Pics/Unique_photo_"+str(time())+".png")

except IOError:
    mkdir(dir)
    photo.save(getcwd()+"/Pics/Unique_photo_"+str(time())+".png")

