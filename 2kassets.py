#!/usr/local/bin/python2.7
# encoding: utf-8
'''
2kassets -- Pass 2d assets to Vision API for multi-labeling


@author:     remyw@google.com

cmd-opt-enter = run

setup before executing (iOS):
-execute in terminal to install client library
pip install --user --upgrade google-cloud-vision


'''
#print("hello")

import io
import os
import csv

#load Google authentication key into environment
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/remyw/eclipse-workspace/Game Asset Vision/remy-sandbox-c93921f43144.json"

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate (if only one)
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     '/Users/remyw/Documents/Pictures/ein.JPG')

# Path to folder with images that you want labeled (.png) 
dirpath="/Users/remyw/eclipse-workspace/Game Asset Vision/AssetFiles/Candy expansion"

# Open csv file to write filepath and labels to
with open('asset_labels1.csv', mode='w') as asset_labels:
    asset_writer = csv.writer(asset_labels, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # Open images in environment to be passed to Vision API
    for file_name in os.listdir(dirpath):
        if file_name.endswith(".png"):
            with io.open(dirpath + "/" + file_name, 'rb') as image_file:
                content = image_file.read()
            
                image = types.Image(content=content)
    
        # Performs label detection on the image file
                response = client.label_detection(image=image)
                labels = response.label_annotations
                
         #Print labels to console and write each image+label as a row to CSV   
                print('Labels:')
                for label in labels:
                    print(label.description)
                    asset_writer.writerow([image_file, label.description])
                continue
        else:
                continue
asset_labels.close()
            
#print("finito")
