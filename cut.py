# coding: utf-8

import os
import cv2
import numpy as np

def main():
	directory = "./A_png"
	files = os.listdir(directory)
	for file in files:
		if ".png" in file:
			print(file)
			img = cv2.imread(directory + "/" + file)
			img = cut(img)
			img = make_square(img)

			cv2.imwrite("./A_png_cut/" + file, img)



def cut(img):
	num = top(img)
	print("Space of top: " + str(num))
	img = cutting_top(img, num)

	num = left(img)
	print("Space of left: " + str(num))
	img = cutting_left(img, num)

	num = right(img)
	print("Space of right: " + str(num))
	img = cutting_right(img, num)

	num = bottom(img)
	print("Space of bottom: " + str(num))
	img = cutting_bottom(img, num)

	return img


def top(img):
	w = img.shape[0]
	h = img.shape[1]
	data = [255, 255, 255]
	white = np.array(data)
	# 横幅の数だけ
	num = 0
	for i in range(w):
		for j in range(h):
			if np.allclose(img[i][j], white):
				pass
			else:
				return num
		# 1行が全て白だった場合
		num = num + 1
	# 全て白だった場合
	print("all white!")
	return num

def cutting_top(img, num):
	h = img.shape[0]
	w = img.shape[1]
	img = img[num:,:]
	return img


def left(img):
	w = img.shape[0]
	h = img.shape[1]
	data = [255, 255, 255]
	white = np.array(data)
	num = 0
	for i in range(h):
		for j in range(w):
			if np.allclose(img[j][i], white):
				pass
			else:
				return num
		num = num + 1
	print("all white!")
	return num

def cutting_left(img, num):
	w = img.shape[0]
	h = img.shape[1]
	img = img[:,num:]
	return img


def right(img):
	w = img.shape[0]
	h = img.shape[1]
	data = [255, 255, 255]
	white = np.array(data)
	num = 0
	for i in reversed(range(h)):
		for j in range(w):
			if np.allclose(img[j][i], white):
				pass
			else:
				return num
		num = num + 1
	print("all white!")
	return num

def cutting_right(img, num):
	w = img.shape[0]
	h = img.shape[1]
	img = img[:,:h-num]
	return img

def bottom(img):
	w = img.shape[0]
	h = img.shape[1]
	data = [255, 255, 255]
	white = np.array(data)
	# 横幅の数だけ
	num = 0
	for i in reversed(range(w)):
		for j in range(h):
			if np.allclose(img[i][j], white):
				pass
			else:
				return num
		# 1行が全て白だった場合
		num = num + 1
	# 全て白だった場合
	print("all white!")
	return num

def cutting_bottom(img, num):
	h = img.shape[0]
	w = img.shape[1]
	img = img[:h-num,:]
	return img

def make_square(img):
	tmp = img[:,:]
	h, w = img.shape[:2]
	if(h > w):
		size = h
		limit = w
	else:
		size = w
		limit = h
	start = int((size - limit) / 2)
	fin = int((size + limit) / 2)

	new_img = cv2.resize(np.zeros((1, 1, 3), np.uint8), (size, size))
	new_img.fill(255)
	#new_img = cv2.resize(white_img, (size, size))
	if size == h:
		new_img[:,start:fin] = tmp
	else:
		new_img[start:fin,:] = tmp
	return new_img


if __name__ == "__main__":
	main()