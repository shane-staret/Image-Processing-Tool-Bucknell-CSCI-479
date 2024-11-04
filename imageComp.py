"""
Contains packages and functions to create a vantage-point tree for image comparison

Source: https://www.pyimagesearch.com/2017/11/27/image-hashing-opencv-python/

For all imageName var besides in getHash, we took off ".png" 
"""

# imports
from imutils import paths
import argparse
import time
import sys
import cv2
import os



"""
compresses an image to a grayscale 9x8 to compute horizontal gradient between pixels
      - when comparing two dhash values, more matches means more similarities
"""
def getHash(imageName, hashSize=8):  # difference hashing function
    # load image
    image = cv2.imread(imageName, cv2.IMREAD_GRAYSCALE)

    # resize the input image to compute horizontal gradient
    resized = cv2.resize(image, (hashSize + 1, hashSize))

    # compute the horizontal gradient between adjacent column pixels
    diff = resized[:, 1:] > resized[:, :-1]

    # convert the difference image to hash (this is an int)
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])



"""
generates an image comparison report by recursively searching all files,
reading in hash values of previous images, and comparing the different
hash values
"""
def generateImageCompReport(imageName, rootDir, currentHash):
    outputFileName = imageName[:-4] + "-ImageCompReport.txt"

    # parsing through the directories and subdirectories
    for subdir, dirs, files in os.walk(rootDir):
        for file in files:
            if "ImageCompHash.txt" in file:
                # print(os.getcwd())
                # print(file)
                with open(outputFileName, "a") as fw, open(os.path.join(subdir,file), "r") as fr:
                    comparison = compareHash(str(currentHash), fr.read())
                    fw.write(imageName + " has a comparison score of " + comparison + " with " + os.path.join(subdir, file.replace("-ImageCompHash.txt", ".png")) + ".\n")



"""
Saves the hash value of the current image into a hidden txt file
"""
def saveHash(fullImageName, imageName, hashValue):
    f = open(fullImageName.replace(imageName, "." + imageName) + "-ImageCompHash.txt", "w+")
    f.write(str(hashValue))
    f.close()


"""
returns a int representing how many hash values matched between the two input hashs
"""
def compareHash(currentHash, previousHash):
    # make sure both Hash are the same length
    diff = len(currentHash) - len(previousHash)
    if diff < 0:
        currentHash += (-diff)*'x'
    if diff > 0:
        previousHash += diff*'x'

    # go through each index of both hashes and increment a variable if they are the same
    total = 0
    for i in range(len(currentHash)):
        if str(currentHash)[i] == str(previousHash)[i]:
            total += 1

    # return the number of shared hashes out of total hash length
    return str(total) + "/" + str(len(currentHash))
