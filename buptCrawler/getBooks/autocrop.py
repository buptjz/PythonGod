# by Mingyang Chen 20110315
import os
import Image
import sys
#from PIL import _imaging


pathTobeStored = "/Users/wangjz/Desktop/down/crop_images_noRetain/"
pathTobeCroped="/Users/wangjz/Desktop/down/images"

def imageCrop(imageToBeCroped,path):
	im = Image.open(path+"/" + imageToBeCroped)
	im.load()
	xsize, ysize = im.size
	xsize -= 1
	ysize -= 1 
	print xsize, ysize
	
	print im.getbands()
	#r, g, b = im.split()
	
	# 1. top
	tag_loop_break = 0
	t1 = 0 # x=0
	t2 = 0 # y=0
	t3 = xsize
	t4 = ysize
	for i in xrange(xsize):
		if tag_loop_break:
			t1 = i
			print t1
			break
		for j in xrange(ysize):
			xy = i, j
			#rtmp = r.getpixel(xy)
			#gtmp = g.getpixel(xy)
			#btmp = b.getpixel(xy)
			alltmp = im.getpixel(xy)
			#print alltmp	
			if alltmp != (255,255,255):
				tag_loop_break = 1
				break
	tag_loop_break = 0
	for i in xrange(ysize):
		if tag_loop_break:
			t2 = i
			print t2
			break
		for j in xrange(xsize):
			xy = j, i
			#rtmp = r.getpixel(xy)
			#gtmp = g.getpixel(xy)
			#btmp = b.getpixel(xy)
			#print "DEBUG"
			alltmp = im.getpixel(xy)
			#print alltmp	
			if alltmp != (255,255,255):
				tag_loop_break = 1
				break
	
	tag_loop_break = 0
	for i in xrange(xsize):
		if tag_loop_break:
			t3 = xsize - i
			print t3
			break
		for j in xrange(ysize):
			xy = (xsize - i), j
			#rtmp = r.getpixel(xy)
			#gtmp = g.getpixel(xy)
			#btmp = b.getpixel(xy)
			alltmp = im.getpixel(xy)
			#print "xy", xy
			#print alltmp	
			if alltmp != (255,255,255):
				tag_loop_break = 1
				break
	
	tag_loop_break = 0
	for i in xrange(ysize):
		if tag_loop_break:
			t4 = ysize - i
			print t4
			break
		for j in xrange(xsize):
			xy = j, (ysize - i)
			#rtmp = r.getpixel(xy)
			#gtmp = g.getpixel(xy)
			#btmp = b.getpixel(xy)
			alltmp = im.getpixel(xy)
			#print alltmp	
			if alltmp != (255,255,255):
				tag_loop_break = 1
				break
	#Retain some white line		
	#if t1 > 5:
		#t1 -= 4
	#if t2 > 5:
		#t2 -= 4
	#if xsize - t3 > 5:
		#t3 += 4
	#if ysize - t4 > 5:
		#t4 += 4
	
	newim = im.crop((t1,t2,t3,t4))
	outpu = pathTobeStored+ imageToBeCroped
	newim.save(outpu)
	print("[Success] crop image:"+imageToBeCroped)
	
def main():
	for root,dirs,files in os.walk(pathTobeCroped):
		for f in files:
			if f.endswith(".jpg"):
				imageCrop(f,root)

if __name__ =='__main__':
	main()
