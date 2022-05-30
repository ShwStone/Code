from PIL import Image
for i in range(10) :
    b = 2 ** i
    pic = Image.new('RGB', (1024, 1024))
    for x in range(1024) :
        for y in range(1024) :
            xx, yy = x // b, y // b
            if xx % 2 == yy % 2 : pic.putpixel((x, y), (255, 0, 0))
            else : pic.putpixel((x, y), (0, 255, 0))
    pic.show()
