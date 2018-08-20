import array, sys, hashlib
from PIL import Image

# getting image data
imagePath = sys.argv[1]
image = Image.open(imagePath)
imageSize = image.size
imagePix = image.load()

# creating html file
htmlName = 'image'
html = open('./files/html/'+ htmlName +'.html', 'w+')

width  = 1
height = 1

htmlPart = "<style> \
                .imageRow{ display: block; width: max-content; } \
                .imagePixel{ display: inline-block; width: .2px; height: .2px; } \
           </style>"
html.write(htmlPart)

while height < imageSize[1]:
    html.write('<div class="imageRow">')
    
    while width < imageSize[0]:
        pixelRGB = imagePix[width, height]
        rgbNotation = 'rgb('+ str(pixelRGB[0]) +','+ str(pixelRGB[1]) +','+ str(pixelRGB[2]) +')'
        htmlPart = '<div class="imagePixel" style="background:'+ rgbNotation +'"></div>'
        html.write(htmlPart)
        width += 1

    html.write('</div>')
    width = 1
    height += 1


html.close()