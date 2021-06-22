import cv2
from PIL import Image 
import numpy as np
import pyautogui
from time import sleep
  

img_location = input("Enter image location: ")
pyautogui.PAUSE = 0.000001

colour_coordinate = [(762,60),(828,60),(850,60),(872,60),(894,60),(916,60),(938,60),(762,85)] #index rep colour number
rectangle_coord = (440,65)
bucket_coord = (267,70)
pencil_coord = (243,70)


def Sort_Tuple(tup):  
    return(sorted(tup, key = lambda x: x[0]))   


def pencil_sketch(img_location):

	img = Image.open(img_location)

	tx,ty = img.size
	if ty>tx:
		img = img.resize(((100*ty)//tx,100))
	else:
		img = img.resize((300,(300*ty)//tx))
		
		

	img = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
	gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	inverted_gray_image = 255 - gray_image
	blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21),0) 
	inverted_blurred_img = 255 - blurred_img
	sketch = cv2.divide(gray_image, inverted_blurred_img, scale = 256.0)

	sketch = cv2.cvtColor(sketch, cv2.COLOR_BGR2RGB)
	img = Image.fromarray(sketch)
	
	img = img.convert('P', palette=Image.ADAPTIVE, colors=2,dither=Image.FLOYDSTEINBERG)
	
	img_array = np.array(img)
	return img, img_array


def draw_bw(img_array):
	
	for i in range(len(img_array)):
		for j in range(len(img_array[0])):
			if img_array[i][j] == 1:
				pyautogui.moveTo(300+j,300+i)
				pyautogui.click()


def colour_sketch(img_location):

	img = Image.open(img_location)
	width, height = img.size
	p_img = Image.new('P', ((300*width)//height,300))
	img = img.resize(((300*width)//height,300))
	
	pall = [0,0,0,237,28,36,255,127,39,255,242,0,39,177,76,0,162,232,63,72,204,255,255,255]#[227, 217, 210, 215, 190, 172, 176, 120, 85, 118, 64, 36]
	p_img.putpalette(pall * 32)

	conv = img.quantize(palette=p_img, dither=Image.FLOYDSTEINBERG)
	return conv,np.array(conv)


def draw_colour(img_array):

	sorted_colour = Sort_Tuple(test.getcolors())
	
	#TODO draw rectangle
	prominent = sorted_colour.pop(-1)[1]
	pyautogui.moveTo(colour_coordinate[prominent])
	pyautogui.click()
	pyautogui.click(rectangle_coord)
	pyautogui.moveTo(300,300)
	pyautogui.dragTo(300+len(img_array[0]),300+len(img_array))
	pyautogui.click(bucket_coord)
	pyautogui.moveTo(300+(len(img_array[0])//2),300+(len(img_array)//2))
	pyautogui.click()
	pyautogui.click(pencil_coord)


	
	for color in range(8):
		if color==prominent:
			pass
		else:
			pyautogui.moveTo(colour_coordinate[color])
			pyautogui.click()
			for i in range(len(img_array)):
				for j in range(len(img_array[0])):
					if img_array[i][j] == color:
						pyautogui.moveTo(300+j,300+i)
						pyautogui.click()


choice = input("Colour(c) or Pencil(p)?")
if choice=="c":
	test,img_array = colour_sketch(img_location)
	test.show()
	print(test.size)
	ans = input("Draw?(y/n): ")
	if ans=='y':
		sleep(5)
		draw_colour(img_array)
elif chice=="p":
	test,img_array = pencil_sketch(img_location)
	test.show()
	print(test.size)
	ans = input("Draw?(y/n): ")
	if ans=='y':
		sleep(5)
		draw_pencil(img_array)


else:
	pass

