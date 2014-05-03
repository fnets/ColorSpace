#This script takes two 1-D arrays of 256 pixels and puts them at the top and bottom of a 256x256px square.  The rest of the square is filled with color that smoothly transitions from one array to the other.
#The arrays' filenames and paths are read as strings from the arguments.
#This was designed for use with SoundSpectrum products, so that we could take our 1-D ColorMaps and turn them into 2-D ColorSpaces, but there's no reason why it couldn't work with any arrays of 256 pixels.
#I tried to be thorough with my comments, but if you have any questions please feel free to reach me at kingoftherobots@gmail.com

from PIL import Image
import math
import sys


im1 = Image.open(str(sys.argv[1])) #takes the filenames of the original image rows from the arguments
im2 = Image.open(str(sys.argv[2]))

field = Image.new("RGB", (256, 256), None) #creates a blank square for us to fill

pix1 = [ im1.getdata()[ i / 3 ][ i % 3 ] for i in xrange( 768 ) ] #reads RGB data from original image rows
pix2 = [ im2.getdata()[ i / 3 ][ i % 3 ] for i in xrange( 768 ) ]

spectrum = [0] * 768 #see comments in loop 
scale = [0] * 768 #see comments in loop

for x in xrange(len(pix1)):		
		
	spectrum[x] = float(pix2[x]-pix1[x])  #fill list with lists of differences of the RGB values of the top and bottom ColorMaps
		
	scale[x] = spectrum[x]/float(256) #create step size by dividing difference by span of distance between ColorMaps
	
	

output = list([0]*256) #stores values for rounding to int
total = list(pix1) #stores values for future use
row = Image.new("RGB", (256,1), None) #image for new row of ColorMaps

for i in xrange(1,256):
	n = 0
	
	for x in xrange(256): #creates a list of tuples with next-step RGB values in them
		data = [0]*3
		outdata = [0] * 3
		for y in xrange(3): #fills a tuple with next-step RGB values
			total[n] = scale[n] + total[n] 
			outdata[y] = int(math.floor(total[n]))
			
			n += 1
			
		outdata = tuple(outdata)
		output[x] = (outdata) #Collects RGB data in array
		
	row.putdata(output) #Takes new RGB data and creates new image row
	
	field.paste(row, (0,i,256,i+1)) #pastes new row underneath previous one

field.paste(im1, (0,0)) #pastes original image rows at the top and bottom of Color Space
field.paste(im2, (0,255))

field.save("ColorSpace.jpeg") #saves new ColorSpace
