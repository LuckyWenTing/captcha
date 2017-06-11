from PIL import Image

im = Image.open("resize.png")
str2 = ""
try:
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if (im.getpixel((i, j)) > 120):
                str2 = "{0}{1}".format(str2, ".")
            else:
                str2 = "{0}{1}".format(str2, "1")
            # print "pixel [", i, j, "] : ", im.getpixel((i, j)), "\n"
except Exception as e:
    print "Exception", e

print "str:"+ str2