import pyscreenshot as ImageGrab
import cv2
from PIL import Image

screenshot_name = "ExampleScreenshot"
full_screenshot_name = screenshot_name + "Full.png"
cropped_screenshot_name = screenshot_name + "Cropped.png"
rotated_screenshot_name = screenshot_name + "Rotated.png"
changed_resolution_screenshot_name = screenshot_name + "ChangedResolution.png"

screenshot_full = ImageGrab.grab()
screenshot_full.save(full_screenshot_name) # saving full screenshot

screenshot_crop = ImageGrab.grab(bbox=(10, 10, 500, 500))
screenshot_crop.save(cropped_screenshot_name) # saving cropped screenshot

screenshot_to_rotate = cv2.imread(full_screenshot_name)
screenshot_rotate_90_clockwise = cv2.rotate(screenshot_to_rotate, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite(rotated_screenshot_name, screenshot_rotate_90_clockwise) # saving rotated screenshot

size = 1300,500
to_resize = Image.open(full_screenshot_name)
screenshot_resize = to_resize.resize(size, Image.ANTIALIAS)
screenshot_resize.save(changed_resolution_screenshot_name) # saving changed resolution screenshot