import sys
import os
import png

# filepath = sys.argv[1]

filepath = r'D:\captcha'

list_of_files = {}

if os.path.isdir(filepath):
    for (dirpath, dirnames, filenames) in os.walk(filepath):
        for filename in filenames:
            if filename.endswith('.png') and not dirpath.endswith('thumb'):
                list_of_files[filename] = os.sep.join([dirpath, filename])

print list_of_files

for k, v in list_of_files.iteritems():
    try:
        with open(v, 'rb') as fp:
            r = png.Reader(file=fp)
            width, height, pixels, metadata = r.asRGBA()
            pixels = tuple(tuple(row.tolist()) for row in pixels)

            with open(v, 'wb') as fq:
                w = png.Writer(width, height, greyscale=True, alpha=True)
                def fn():
                    for row in pixels:
                        row = list(row)
                        # row[0::4] = row[1::4] = row[2::4] = [0] * width
                        row[0::4] = [0] * width
                        del row[1::4]
                        del row[1::3]
                        yield row
                w.write(fq, fn())
    except Exception as e:
        print "error with ", e
