# coding: utf-8

import os
import cv2

def main():
	#files = os.listdir("./testdata_png")
	files = os.listdir("./A_png_cut")
	for file in files:
		if ".png" in file:
			print(file)
			#img = cv2.imread("./testdata_png/" + file)
			img = cv2.imread("./A_png_cut/" + file)
			new_img = cv2.resize(img, (32, 32))
			#cv2.imwrite("./testdata_32_png/" + file, new_img)
			cv2.imwrite("./A_png_cut_32/" + file, new_img)

if __name__ == "__main__":
	main()