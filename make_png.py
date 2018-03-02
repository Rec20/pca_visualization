# encoding: utf-8

import os
from PIL import Image, ImageDraw, ImageFont

# google fontsから取得したttfファイルのうち、regularと付く名前のものをpngに変換
SIZE = W, H = 512, 512
def main():
    directory = "./ttf_regular"
    files = os.listdir(directory)
    for file in files:
        if ".ttf" in file:
            savename = file.replace(".ttf", "")
            print(savename)
            # フォント特有の空白が存在するため文字を中央に寄せている
            text_canvas = Image.new("RGB", SIZE, (255, 255, 255))
            draw = ImageDraw.Draw(text_canvas)
            filename = directory + "/" + file
            font = ImageFont.truetype(filename, size=256)
            tw, th = font.getsize("A")
            print("tw:" + str(tw))
            print("th:" + str(th))
            draw.text(((W - tw) / 2, (H - th) / 2), "A", font=font, fill="#000")
            savename = "./font_png/" + savename + ".png"
            text_canvas.save(savename, "PNG", quality=100, optimize=True)

        
if __name__ == "__main__":
    main()
