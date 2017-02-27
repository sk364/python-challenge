from PIL import Image

chimg = Image.open('oxygen.png')

img_w, img_h = chimg.width, chimg.height

res = [ chr(chimg.getpixel((5 + 7*i, 47))[0]) for i in xrange(86)]
fres = 's'+''.join(res)

print fres

print "\nConverting the list of values in pixel ASCII back to char\n"

idx = fres.index('[')

ff = fres[43:len(fres)-1]

level_name_ascii = ff.split(', ')

level_name = [chr(int(c)) for c in level_name_ascii]

print ''.join(level_name)
