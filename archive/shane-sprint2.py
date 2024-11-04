#!/usr/bin/env python3

# Argument Table -- not accurate rn
# argv0: script name
# argv1: timeUntilScreenshot
# argv2: screenshot name


import sys
import pyscreenshot as ImageGrab
import cv2
import time
import os
from PIL import Image
import shutil
# argument representing the time until screenshotting occurs from when script is ran


def demo():
    try:
        timeUntilScreenshot = int(sys.argv[1]) #time until screenshotting converted to an int
        screenshotName = sys.argv[2]
       # basedir = sys.argv[2] #string of directory where we want to save otuput
        takeScreenshots(timeUntilScreenshot, screenshotName)

    except ValueError:
        print("USAGE: ./script time-until-screenshot screenshot-name")
        print("ValueError: Please enter a time as an interger in seconds. For EX: 5")
        return


def takeScreenshots(timeUntilScreenshot, screenshotName):
    #set screenshot names
    screenshot_name = screenshotName

    path = os.getcwd() + '/' #HAVE TO DO THIS BEFORE SAVING
    #print("PATH: " + path)
    subDir = path + screenshot_name
    #print("subDir: "+ subDir)
    try:
        os.mkdir(subDir)
    except FileExistsError:
        print("\nAborting...")
        print("\nThe subdirectory you chose already exists at this location. Name it differently or delete the previous version.")
        return

    #delay so user can open whatever application
    time.sleep(timeUntilScreenshot)

    original(screenshot_name, path, subDir)
    crop(screenshot_name, path, subDir)
    rotate(screenshot_name, path, subDir)
    changeResolution(screenshot_name, path, subDir)


def original(screenshot_name, path, subDir):
    #grab actual images
    original_screenshot = ImageGrab.grab()
    original_screenshot.save(screenshot_name) # saving full screenshot
    shutil.move(path + "/" + screenshot_name, subDir )


def crop(screenshot_name, path, subDir):
    cropped_screenshot_name = screenshot_name + "Cropped.png"
    screenshot_crop = ImageGrab.grab(bbox=(10, 10, 500, 500))
    screenshot_crop.save(cropped_screenshot_name) # saving cropped screenshot
    shutil.move(path + "/" + cropped_screenshot_name, subDir)

def rotate(screenshot_name, path, subDir):
    rotated_screenshot_name = screenshot_name + "Rotated.png"
    screenshot_to_rotate = cv2.imread(screenshot_name)
    screenshot_rotate_90_clockwise = cv2.rotate(screenshot_to_rotate, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(rotated_screenshot_name, screenshot_rotate_90_clockwise) # saving rotated screenshot
    shutil.move(path + "/" + rotated_screenshot_name, subDir )

def changeResolution(screenshot_name, path, subDir):
    changed_resolution_screenshot_name = screenshot_name + "ChangedResolution.png"
    size = 1300,500
    to_resize = Image.open(screenshot_name)
    screenshot_resize = to_resize.resize(size, Image.ANTIALIAS)
    screenshot_resize.save(changed_resolution_screenshot_name) # saving changed resolution screenshot
    shutil.move(path + "/" + changed_resolution_screenshot_name, subDir )


if __name__ == "__main__":
    demo()
