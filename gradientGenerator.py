# Square Gradient generator by RaddedMC
# Did this instead of sleeping or doing uni homework -- have fun :D

# pip install Pillow numpy
from PIL import Image, ImageDraw
import numpy

## USER-CONTROLLED VARIABLES ##
startColor = (234,80,255) # Color #1
endColor = (255,255,0) # Color #2
resolution = (1920,1080) # Image resolution -- gradient is generated along the x-axis
tilesWidth = resolution[0] # Leave unchanged for a perfect gradient

squareImage = Image.new(mode = "RGB", size=resolution);
squareImageDraw = ImageDraw.Draw(squareImage);

for i in range(tilesWidth):
    # Variables? Who needs those??
    squareImageDraw.rectangle(
        [
            (i*resolution[0]/tilesWidth,0),
            ((i+1)*resolution[0]/tilesWidth,resolution[1])
        ],
        fill=tuple(
            numpy.subtract(
                startColor, numpy.subtract(startColor,endColor) * i/tilesWidth).astype(int))            
    )

squareImage.show()