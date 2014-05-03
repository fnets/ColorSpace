Hello, World!  I'm Frank, and you can reach me at kingoftheorobots@gmail.com. This project was created when SoundSpectrum wanted to create 2-D ColorSpaces (original 2-D arrays of pixels) for a 3-D music visualizer project.  We had many 1-D arrays of pixels, and wanted a way to quickly generate ColorSpaces. The result was the short script contained in this repository.  To run it, you must have Python 2.7 or later.  I'm not sure if it's compatible with Python 3, but feel free to let me know if you have any trouble.

I use Cygwin for all my Python projects, so I wrote this script to read the paths and filenames of the pixel arrays as strings from the arguments.  If you'd like to change the input method, the comments should guide you to which lines to change.

This script takes two 1-D arrays of 256 pixels and puts them at the top and bottom of a 256x256 pixel square.  The rest of the square is filled with a color gradient that smoothly transitions from one array to the other. 

This was designed for use with SoundSpectrum products, but there's no reason why it couldn't work with any arrays of 256 pixels.  Even so, I've included 2 ColorMaps that I created, so that you can try it out right now.  Place all of the files in the same folder.  When you run the script the first and second arguments will be the top and bottom arrays, respectively.  The ColorSpace should be created in your folder, and named "ColorSpace.jpg"

I tried to be thorough with my comments, but if you have any questions please feel free to contact me.