from PIL import Image

bg = Image.open("poster_bg.png")
banner = Image.open("../convert/banner.png")
x = (bg.width - banner.width) // 2
y = (bg.height - banner.height) // 2
bg.paste(banner, (x, y))
bg.save("poster.png")
