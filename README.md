# Python-Spherical-Projection
Convert cubemap image to an equirectangular spherical projection image using Python 2.7.

Currently only works with cubemaps laid out in the following format:
  
             ________
            |        |
            |   top  |
            |        |
     _______|________|_________________
    |       |        |        |        |
    | left  |  front |  right |  back  |
    |       |        |        |        |
    |_______|________|________|________|
            |        |
            |        |
            |  down  |
            |________|

**Input Image**
![input](https://github.com/adamb70/Python-Spherical-Projection/blob/master/Example/Example%201/input.jpg)

**Output Image**
![output](https://github.com/adamb70/Python-Spherical-Projection/blob/master/Example/Example%201/output.jpg)


## Instructions

* Open an image using PIL or equivalent.
* Calculate dimensions of output image. (Width must be 2xheight. Height can be any percentage of input image, but larger output images lead to less precise results.)
* Calculate length of each square face (ie. 1/3 height of the input, due to height being made from 3 faces - top,front,down)
* Create an output image using the new dimensions.
* For each pixel location in the output image run `cube2equi.find_corresponding_pixel()` to return the corresponding pixel in the input image.
* Take the colour value for the input image pixel and apply it to the pixel in the output.

## TODO

* Automate all setup steps
* Allow for different cubemap layouts
