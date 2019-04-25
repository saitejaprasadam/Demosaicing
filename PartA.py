import library
import numpy as np
import cv2 as opencv

originalImage = opencv.imread(r"F:\Notes\Master's notes\Semester VI\Computer Vision\Assignments\Assignment 1\image_set\oldwell.jpg")
mosaicImage = opencv.imread(r"F:\Notes\Master's notes\Semester VI\Computer Vision\Assignments\Assignment 1\image_set\oldwell_mosaic.bmp")

splitedMosaicImage = opencv.split(mosaicImage)
splitedMosaicImage[0] = library.get_blue_channel(splitedMosaicImage[0])
splitedMosaicImage[1] = library.get_green_channel(splitedMosaicImage[1])
splitedMosaicImage[2] = library.get_red_channel(splitedMosaicImage[2])

red_filter = np.array([
    [0, 0.25, 0],
    [0.25, 1, 0.25],
    [0, 0.25, 0],
])

green_blue_filter = np.array([
    [0.25, 0.5, 0.25],
    [0.5, 1, 0.5],
    [0.25, 0.5, 0.25],
])

splitedMosaicImage[0] = opencv.filter2D(splitedMosaicImage[0], 0, green_blue_filter)
splitedMosaicImage[1] = opencv.filter2D(splitedMosaicImage[1], 0, green_blue_filter)
splitedMosaicImage[2] = opencv.filter2D(splitedMosaicImage[2], 0, red_filter)

resultImage = opencv.merge(splitedMosaicImage)
differenceImage = library.get_difference(originalImage, resultImage)
stackedImage = library.stack_images(originalImage, resultImage, differenceImage)

opencv.imshow('Linear Interpolation', stackedImage.astype(np.uint8))
opencv.waitKey(0)
opencv.destroyAllWindows()