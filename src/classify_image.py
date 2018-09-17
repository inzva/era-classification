# Load necessary packages
from keras.applications import ResNet50
from keras.applications import InceptionV3
from keras.applications import Xception 
from keras.applications import VGG19
from keras.applications import imagenet_utils
from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img

import numpy as np
import argparse
import cv2

# Parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="Path to the input image")
ap.add_argument("-model", "--model", type=str, default="vgg19",
	help="Name of pre-trained network to use")
args = vars(ap.parse_args())

# Create a model dictionary
MODELS = {
	"resnet": ResNet50,
	"vgg19": VGG19,
	"inceptionv3": InceptionV3,
	"xception": Xception, 
}
 
# Ensure the input is a valid model name 
if args["model"] not in MODELS.keys():
	raise AssertionError("The --model command line argument should "
		"be a key in the `MODELS` dictionary")

'''
Initialize the input image shape (224x224 pixels) along with
the pre-processing function (this might need to be changed
based on which model we use to classify our image). ResNet50 and
 VGG19 require 224x224 image inputs.
'''
inputShape = (224, 224)
preprocess = imagenet_utils.preprocess_input

'''
If we are using the InceptionV3, InceptionV4 or Xception networks, then we
need to set the input shape to (299x299) rather than (224x224)
and use a different image processing function
'''
if args["model"] in ("inceptionv3", "xception"):
	inputShape = (299, 299)
	preprocess = preprocess_input

''' 
The network weights will be loaded whenfrom disk when 
running this script for the first time for any given network.
Depending on which network you are using, the weights can be 90-575MB,
the weights will be cached and subsequent runs of this script 
will be much faster.
'''
print("[INFO] loading {}...".format(args["model"]))
Network = MODELS[args["model"]]
model = Network(weights="imagenet")

'''
Load the input image using the Keras helper utility while 
ensuring the image is resized to the required `inputShape`
'''
print("[INFO] loading and pre-processing image...")
image = load_img(args["image"], target_size=inputShape)
image = img_to_array(image)

''' 
Our input image is now represented as a NumPy array of shape
(inputShape[0], inputShape[1], 3) however we need to expand the
dimension by making the shape (1, inputShape[0], inputShape[1], 3)
so we can pass it through the network.
'''
image = np.expand_dims(image, axis=0)
 
'''
Pre-process the image using the appropriate function based on the 
selected model
'''
image = preprocess(image)