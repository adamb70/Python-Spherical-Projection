from PIL import Image
from cube2equi import find_corresponding_pixel


def convert_img(infile, outfile):
    inimg = Image.open(infile)

    wo, ho = inimg.size

    # Calculate height and width of output image, and size of each square face
    h = wo/3
    w = 2*h
    n = ho/3

    # Create new image with width w, and height h
    outimg = Image.new('RGB', (w, h))

    # For each pixel in output image find colour value from input image
    for ycoord in range(0, h):
        for xcoord in range(0, w):
            corrx, corry = find_corresponding_pixel(xcoord, ycoord, w, h, n)

            outimg.putpixel((xcoord, ycoord), inimg.getpixel((corrx, corry)))
        # Print progress percentage
        print str(round((float(ycoord)/float(h))*100, 2)) + '%'


    outimg.save(outfile, 'PNG')


convert_img('input.jpg', 'output.jpg')