# coding: utf-8

import os
import shutil

# ttfファイルの中でRegularという名前のつくものを他のフォルダにコピー
def main():
	files = os.listdir("./all_ttf_original")
	regular = []
	for file in files:
		if "-Regular.ttf" in file:
			savename = file.replace("-Regular", "")
			print(file)
			filename = "./all_ttf_original/" + file
			copyname = "./ttf_regular/" + savename
			shutil.copyfile(filename, copyname)


if __name__ == "__main__":
	main()