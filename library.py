import cv2 as opencv
import numpy as np


def get_blue_channel(imageData):
    for x in range(0, len(imageData)):
        for y in range(0, len(imageData[x])):
            if not (x % 2 == 0 and y % 2 == 0):
                imageData[x][y] = 0

    return imageData


def get_red_channel(imageData):
    for x in range(0, len(imageData)):
        for y in range(0, len(imageData[x])):
            if not ((x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0)):
                imageData[x][y] = 0

    return imageData


def get_green_channel(imageData):
    for x in range(0, len(imageData)):
        for y in range(0, len(imageData[x])):
            if not (x % 2 != 0 and y % 2 != 0):
                imageData[x][y] = 0

    return imageData


def stack_images(image1, image2, image3):
    margin = np.full((len(image1), 1, 3), 255).astype(np.uint8)
    return np.concatenate((image1, margin, image2, margin, image3), axis=1)


def get_difference(originalImage, resultImage):
    originalImage = originalImage.astype(np.float32)
    resultImage = resultImage.astype(np.float32)
    return abs(originalImage - resultImage).astype(np.uint8)


def float32(splitedMosaicImage):
    splitedMosaicImage[0] = splitedMosaicImage[0].astype(np.float32)
    splitedMosaicImage[1] = splitedMosaicImage[1].astype(np.float32)
    splitedMosaicImage[2] = splitedMosaicImage[2].astype(np.float32)
    return splitedMosaicImage


def unit8(splitedMosaicImage):
    splitedMosaicImage[0] = abs(splitedMosaicImage[0])
    splitedMosaicImage[1] = abs(splitedMosaicImage[1])
    splitedMosaicImage[2] = abs(splitedMosaicImage[2])

    splitedMosaicImage[0] = splitedMosaicImage[0].astype(np.uint8)
    splitedMosaicImage[1] = splitedMosaicImage[1].astype(np.uint8)
    splitedMosaicImage[2] = splitedMosaicImage[2].astype(np.uint8)
    return splitedMosaicImage
