from PIL import Image
import numpy as np
import scipy.misc




k1 = Image.open("key1.png")
k2 = Image.open("key2.png")
I = Image.open("I.png")
e  = Image.open("E.png")
ee  = Image.open("Eprime.png")

#image input

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
        
#image to array 
  
w = np.array([0,0,0]) # 1x3 array

maxlimit = 10
temp_w0 = 5
temp_w1 = 5
temp_w2 = 5

#set param


epoch = 1
print(  w[0] , w[1] , w[2] )
while epoch < maxlimit and abs(w[0] - temp_w0) > 0.00001 and abs(w[1] - temp_w1) > 0.00001 and abs(w[2] - temp_w2) > 0.00001:
    
    temp_w0 = w[0]
    temp_w1 = w[1]
    temp_w2 = w[2]
    
    for i, x in enumerate(data): 
            temp = w[0] * data[i][0] + w[1] * data[i][1] + w[2] * data[i][2]
            w = w + 0.00001 *(e_arr[i] - temp) * x

    print(w[0], w[1], w[2])
    epoch += 1
    
    
#LMS

ima = np.zeros((300,400),int)
for y in range(height):
    for x in range(width):
        ima[y][x] = (ee.getpixel((x,y)) - w[1] *k1.getpixel((x,y)) -w[2] * k2.getpixel((x,y)))/w[0]
        
        
    

scipy.misc.imsave('outfile.jpg', ima)

#array to png


        




