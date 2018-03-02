# coding: utf-8

import os
import csv
import cv2
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# 1024次元のデータを作成
def data_1024():
	files = os.listdir("./A_png_cut_32")
	dataset = []
	for file in files:
		if ".png" in file:
			img = cv2.imread("./A_png_cut_32/" + file)
			tmp_data = []
			tmp_data.append(file)
			for i in range(32):
				for j in range(32):
					pixel_value = img[i, j]
					tmp_data.append(str(pixel_value[0]))
			dataset.append(tmp_data)
	return dataset


# name,x,y,zの形のlistを返す
def pca_3d(d):
	dataset = np.array(d)
	data = np.delete(dataset, 0, 1)
	# ここのdtypeの指定がなくてしばらく詰まった
	data = np.array(data, dtype=float)
	pca = PCA(n_components = 3, whiten = False)
	pca.fit(data)
	# 三次元に変換
	x = pca.transform(data)
	# このようにしないと一次元しかlistにならない
	x = x.tolist()
	for i in range(len(x)):
		x[i].insert(0, d[i][0])
	return x


# pcaした値を0~1の範囲に圧縮
def conversion(dataset):
	# maxとminの計算
	x = []
	y = []
	z = []
	for i in range(len(dataset)):
		x.append(float(dataset[i][1]))
		y.append(float(dataset[i][2]))
		z.append(float(dataset[i][3]))
	max_value = max(max(x), max(y), max(z))
	min_value = min(min(x), min(y), min(z))
	denominator = max_value - min_value
	# 新しい値に変換
	dataset_new = []
	for i in range(len(dataset)):
		tmp_data = []
		x = (float(dataset[i][1]) - min_value) / (denominator)
		y = (float(dataset[i][2]) - min_value) / (denominator)
		z = (float(dataset[i][3]) - min_value) / (denominator)
		# -50 から 50 に変換
		x = x * 100 - 50
		y = y * 100 - 50
		z = z * 100 - 50
		# 配列を作成
		tmp_data.append(dataset[i][0])
		tmp_data.append(x)
		tmp_data.append(y)
		tmp_data.append(z)
		dataset_new.append(tmp_data)
	# keyを追加
	key = ["name", "x", "y", "z"]
	dataset_new.insert(0, key)
	return dataset_new


# 配列からcsvを作成
def make_csv(data):
	f = open("data.csv", "w")
	csvWriter = csv.writer(f)
	for d in data:
		csvWriter.writerow(d)


# ファイルの名前一覧のテキストファイルを作成
def make_name():
	f = open("name.txt", "w")
	files = os.listdir("./A_png_cut_32")
	for file in files:
		if ".png" in file:
			f.writelines(file + "\n")


# main関数
def main():
	dataset = data_1024()
	pca = pca_3d(dataset)
	con = conversion(pca)
	make_csv(con)
	make_name()


if __name__ == "__main__":
	main()