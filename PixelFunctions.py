from PIL import Image, ImageDraw
import colorsys


def compare_pixels(pix1, pix2):
    return pix1[0][0] > pix2[0][0]  # only comparing red values
# end def compare_pixels(pix1, pix2):

def store_pixels(im):
    width = int(im.size[0])
    height = int(im.size[1])

    # store pixels in a list
    pixel_array = []
    yiq_pixels = []
    for i in range(width):  # for loop for x position
        for j in range(height):  # for loop for y position
            # get r and g and b values of pixel at position
            r, g, b = im.getpixel((i, j))  # make an i, j tuple before passing
            yiq = colorsys.rgb_to_yiq(r/255, g/255, b/255)
            yiq_pixels.append([yiq, (i, j)])
            pixel_array.append([(r, g, b), (i, j)])  # store pixels in double tuple
        # end for i
    return (pixel_array, yiq_pixels ) # send array back to main
# end def store_pixels(im):

def pixels_to_image(im, pixels):
    outimg = Image.new("RGB", im.size)

    # check list element 0, tuple value 0, inner tuple val 0
    if type(pixels([0][0][0])) == float: # dealing with YIQ
        print("YIQ")
        yiq_out = []
    for p in pixels:
        r, g, b = colorsys.yiq_to_rgb(p[0][0], p[0][1], p[0][2])
        #  rgb comes out of that conversation as float between 0-1
        r, g, b = int(g*255), int(g*255), int(b*255)
        yiq_out.append((r, g, b))
    # end for p in pixels:
        outimg.putdata(yiq_out)
    else: # dealing with RGB
        outing.putdata([p[0] for p in pixels])
    outimg.show()
    return outimg
# end def pixels_to_image(im, pixels):

def pixels_to_points(im, pixels):
    # writes pixels passed in to image passed in
    for p in pixels:
        if type(p[0][0]) == float: # dealing with YIQ
            im.putpixels(p[1], tuple([int(v*255)
                    for v in colorsys.yiq_to_rgb(p[0][0], p[0][1], p[0][2])]))
        else: # dealing with rgb
            im.putpixels(p[1], p[0]) # pixels at their coordinate
    im.show()
# end def pixels_to_points(size, pixels):


def grayscale(im, pixels):
    draw = ImageDraw.Draw(im)
    for px in pixels:
        gray_av = int((px[0][0] + px[0][1] + px[0][2]) / 3)
        draw.point(px[1], (gray_av, gray_av, gray_av))
# end def grayscale(im, pixels):
