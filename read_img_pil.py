from PIL import Image

im = Image.open("0.png").convert('RGBA').convert('L')
im.save("grayscale.png")


for i in range(im.size[0]):
    for j in range(im.size[1]):
        # print "pixel [", i, j, "] : ", im.getpixel((i, j)), "\n"
        if(im.getpixel((i,j))>120):
            im.putpixel((i,j), 255)
        else:
            im.putpixel((i,j),0)

im.save("black_white.png")

size = 100, 100
# im.thumbnail(size)
# im.thumbnail(size, Image.ANTIALIAS)
im = im.resize(size, Image.BILINEAR)

print "................................."
im.save("0_square.png")


for i in range(im.size[0]):
    for j in range(im.size[1]):
        print "pixel [",i,j,"] : ",im.getpixel((i,j)),"\n"

