from PIL import Image
import pandas as pd 
# Open Image
list_image = ["mawar1.jpg","mawar2.jpg","mawar3.jpg","mawar4.jpg"]

#init list
R = []
G = []
B = []
images = []

for image in list_image:
    im = Image.open(image)
 
    # Convert Image to RGB
    rgb_im = im.convert('RGB')
     
    # Use the .size object to retrieve a tuple contain (width,height) of the image
    # and assign them to width and height variables
    width = rgb_im.size[0]
    height = rgb_im.size[1]
     
    # set some counters for current row and column and total pixels
    row = 1
    col = 1
    pix = 0
     
    # create an empty output sum r,g,b
    sumr = 0
    sumg = 0
    sumb = 0 
    # loop through each pixel in each row outputting RGB value as we go...
    # all the plus and minus ones are to deal with the .getpixel class being
    # zero indexed and we want the output to start at pixel 1,1 not 0,0!
    while row < height + 1:
        while col < width + 1:
            # get the RGB values from the current pixel
            r, g, b = rgb_im.getpixel((col - 1, row - 1))
            sumr += r
            sumg += g
            sumb += b
            # increment the column count
            col = col + 1
            # increment the pixel count
            pix = pix + 1
        # increment the row...
        row = row + 1
        # reset the column count
        col = 1

    #add to list
    images.append(image)
    R.append(sumr/pix)
    B.append(sumb/pix)
    G.append(sumg/pix)

row_data = {'Gambar':images,
            'R':R,
            'G':G,
            'B':B
            }
#save to csv
df = pd.DataFrame(row_data, columns = ['Gambar','R','G','B'])
df.to_csv("gambar.csv")