from PIL import Image
from SortFunctions import selection_sort, quick_sort
from SearchFunctions import  binary_search_sub
from PixelFunctions import store_pixels
from PixelFunctions import compare_pixels


def main():
    IMG_NAME = "monkey.jpeg"

    selected_type = None
    # open image and read each pixel to memory as im
    with Image.open(IMG_NAME) as im:
        im.show()

        try:
            while selected_type is None or selected_type == "":
                selected_type = input("Please enter a any of these keys. \n1.q \n2.r \n3.t \n4.c \n").lower()

                # if user selects q
                if selected_type == "q":
                    return im.save("orig" + IMG_NAME, "JPEG")

                pixels, yiq_pixels = store_pixels(im)
                selection_sort(yiq_pixels, compare_pixels)  # sort yig
                sorted_im = pixels_to_image(im, yiq_pixels)
                sorted_im.save("sorted_" + IMG_NAME + "jpg", "JPEG")

                target = (183 / 255, 198 / 255, 144 / 255)  # /255 for conversion with YIQ search
                yiq_target = colorsys.rgb_to_yiq(target[0], target[1], target[2])

                subi = binary_search_sub([r[0][0] for r in yiq_pixels],
                                         0, len(yiq_pixels) - 1, yiq_target[2])

                # if user selects r
                if selected_type == "r":
                    pixels_to_image(im, yiq_pixels[:subi])

                    # if user selects t
                if selected_type == "t":
                    subi = int(len(yiq_pixels) / 4)
                    pixels_to_image(im, yiq_pixels[subi:])

                    # if user selects c
                if selected_type == "c":
                    values = input("Please enter a value for r,g,b. Please sepearte by comma\n")
                    R, G, B = values.split(",")
                    target = (int(R) / 255, int(G) / 255, int(B) / 255)  # /255 for conversion with YIQ search
                    yiq_target = colorsys.rgb_to_yiq(target[0], target[1], target[2])
                    subi = binary_search_sub([r[0][0] for r in yiq_pixels],
                                             0, len(yiq_pixels) - 1, yiq_target[2])

        except KeyboardInterrupt:
            print("Thank you.")
            exit()

    im.save("neg_" + IMG_NAME, "JPEG")

if __name__ == "__main__":
    main()
