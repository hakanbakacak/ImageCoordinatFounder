import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt
import sys


def searchImage(input_starMap, input_image):
  starMap = np.array(input_starMap)
  input = np.array(input_image)
  
  starMapX = starMap.shape[0]
  starMapY = starMap.shape[1]
  
  smallAreaX = input.shape[0]
  smallAreaY = input.shape[1]


  stopx = starMapX - smallAreaX + 1
  stopy = starMapY - smallAreaY + 1

  plt.imshow(input)
  
  for x in range(0, stopx):
    for y in range(0, stopy):
      x2 = x + smallAreaX
      y2 = y + smallAreaY
      tempImage = starMap[y:y2, x:x2]
      if np.array_equal(tempImage, input):
        #print(x,y)
        return x,y, x2, y2
        
  
  return -1, -1, -1, -1


if(len(sys.argv)<3):
    print("please enter path of star map and input image for example main.py /starmap.png /input_image")
    sys.exit()



starMapPath = sys.argv[1]
inputImagePath = sys.argv[2]

starMap = cv2.imread(starMapPath)
inputImage = cv2.imread(inputImagePath)


print("searching")
x1,y1, x2,y2 = searchImage(starMap, inputImage)
print(str(x1) + ", " + str(y1) + ", " + str(x2) + ", " + str(y2) )
