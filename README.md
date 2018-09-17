# Project Description
Era Classification project aims to identify the era of oil paintings using Convolutional Neural Networks. The target granularity is 50 years for paintings dating pre 19th century and 20 years for paintings dating from 19th century and onwards.

All of the code will be written with Python and 


# Installation
If you have Anaconda installed, it'd be the best to use a virtual environment for project setup. To create a conda virtual environment:
```
conda create -n ENV_NAME python=3.5
# Activate virtual environment
conda activate ENV_NAME
```
### Installing dependencies
Package dependencies are specified in the requirements.txt file. To setup this project locally:
+ Create an empty folder and clone this repo.
```
mdir /path/FOLDER_NAME
git clone https://github.com/inzva/era-classification /path/FOLDER_NAME
```
+ Install dependencies.
```
pip install -r requirements.txt
```

# Project Structure
1. data                   -->     Raw data sources, train and test images
2. src  
	* classify-image.py   -->     Classify images with the selected network
3. pretrained_models      -->     Saved model weights for InceptionV4
4. notebooks              -->     Jupyter notebooks for experimenting
5. requirements.txt       -->     Python package dependencies

### Data Sources
Ana dosya main.py olup, diğer query scriptlerinin birleştirilmiş halidir. Elektrik, sensör ve

### Pretrained Models
* Inception V3
* Inception V4
* Xception
* Inception - ResNet V2
* VGG19

### Scripts

# Resources to Get Started
