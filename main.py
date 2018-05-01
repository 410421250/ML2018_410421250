from PIL import Image
import numpy as np




k1 = Image.open("key1.png")
k2 = Image.open("key2.png")
I = Image.open("I.png")
e  = Image.open("Eprime.png")
ee  = Image.open("e.png")

print ( k1.format , k1.size , k1.mode )

data = np.zeros((120000,3),int)
e_arr = np.zeros((120000),int)
 
width, height = k1.size

for y in range(height):
    for x in range(width):
        data[y*400+x][0] =  I.getpixel((x,y))
        data[y*400+x][1] =  k1.getpixel((x,y))
        data[y*400+x][2] =  k2.getpixel((x,y))
        e_arr[y*400+x] =  e.getpixel((x,y))
  
w = np.array([0,0,0]) # 1x3 array

stop = False
epoch = 1
print(  w[0] , w[1] , w[2] )
while not stop:
    grad = [0, 0, 0]
    stop = True
    for i, x in enumerate(data): 
            temp = w[0] * data[i][0] + w[1] * data[i][1] + w[2] * data[i][2]
            w = w + 0.00001 *(e_arr[i] - temp) * x

    print(w[0], w[1], w[2])
    epoch += 1



        




