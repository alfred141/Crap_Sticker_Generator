from PIL import Image, ImageDraw, ImageFont

# 假設我們有以下列表中的文字
text_list = ["這是第一張圖片", "這是第二張圖片", "這是第三張圖片"]

# 創建字體物件，需要一個支持中文的字體檔案
font = ImageFont.truetype('Arial Unicode.ttf', 50)

for index, text in enumerate(text_list):
    # 創建一個空白圖片，大小為 800 x 800 像素
    img = Image.new('RGB', (800, 800), color = (255, 255, 255))

    # 創建 ImageDraw 物件
    d = ImageDraw.Draw(img)

    # 獲取文字大小
    text_width, text_height = d.textsize(text, font=font)

    # 計算將文字置中的位置
    position = ((800-text_width)/2, (800-text_height)/2)

    # 在圖片上寫入文字
    d.text(position, text, fill=(0, 0, 0), font=font)

    # 儲存圖片
    img.save(f"image_{index+1}.png")