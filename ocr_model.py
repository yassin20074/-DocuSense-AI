#Calling the libraries 

import pytesserac #To convert images to text 
from PIL import Image #Converting image arrays into processable images 
import cv2 # Image enhancement 
import numpy as np #Working with digital arrays 
import io #Handling files in memory 

#A function that accepts a file in bytes 
def extract_text_from_image(file_bytes):
    # Converting bytes to an OpenCV array 
    nparr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Pre-processing using OpenCV to improve accuracy 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Improving contrast (Thresholding) to make the text clearer 
    processed_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Converting an OpenCV array to a PIL image for processing with Tesseract 
    pil_img = Image.fromarray(processed_img)
    
    text = pytesseract.image_to_string(pil_img)
    #Return the text 
    return text
