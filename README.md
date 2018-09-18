# Project Description
Era Classification project aims to identify the era of oil paintings using Convolutional Neural Networks. The target era granularity is 50 years for paintings dating pre 19th century and 20 years for paintings dating from 19th century and onwards. 

Models pre-trained for object recognition on ImageNet will be used to predict artwork era instead of content occurrences. The last layers of models are retrained for era classification using the Web Gallery of Art dataset.

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
mdir /PATH/FOLDER_NAME
git clone https://github.com/inzva/era-classification /PATH/FOLDER_NAME
```
+ Install dependencies.
```
pip install -r requirements.txt
```

# Project Structure
1. data                   -->     Raw data sources, train and test images
	* catalog.csv
	* image folders of each era
2. src                    -->     Scripts for preprocessing, feature extraction and image classification
	* classify-image.py 
	* linear_svm.py
	* efm-knn.py  
3. pretrained_models      -->     Saved model weights for InceptionV4
4. notebooks              -->     Jupyter notebooks for experimenting
5. requirements.txt       -->     Python package dependencies

### Data Sources
The main data source for this project is the Web Gallery of Arts, the **catalog.csv** file had the links to the images as well as their corresponding labels in terms of style, year, artist and materials used. The downloaded images are stored in separate folders based on their era label.

### Pretrained Models
Includes model weights (last layers are removed). Training CNN models from scratch can be extremely time-consuming, saving model weights is an efficient way of speeding up experiments. The models we are using are:
* Inception V3
* Inception V4
* Xception
* Inception - ResNet V2
* VGG19

### Scripts
Includes all the python files needed to preprocess and classify images. Apart from the Convolutional Neural Networks, linear SVM and EFM-KNN models are used as baseline models for comparison purposes. 
**Classifying Images**
* classify-image.py

**Models**
* linear_svm.py
* efm-knn.py

# Outline of the Project
**Proposed Steps**
1. Preprocessing
	* Tagging images with the corresponding era
	* Resizing images based on the required model input shape
2. Exploration
	* Visualizing the distribution of the dataset with t-SNE
3. Creating Baseline Models
	* Linear SVM classifier
	* EFM- KNN classifier
4. Feature Extraction


### Improvements and Ideas for Experiments
**Data Augmentation Through Distortion** <br>
Augmenting the training dataset by applying distortions to the input images in order to increase the robustness of our models and their ability to generalise to a broad
range of unknown pictures. We could use the following distortions: random, horizontal flips, rotations, axial translations and zooming.

**Bagging** <br>
Bagging is the process of averaging the output of different predictions produced 
by the model on several variations of input data. It can be used to increase the accuracy and stability of our classifier.

# Resources to Get Started
### Papers
* Lecoutre, A., Negrevergne, B. & Yger, F. “Recognizing Art Style Automatically in painting with deep learning.” 
http://www.lamsade.dauphine.fr/~bnegrevergne/webpage/documents/2017_rasta.pdf
* Bar, Y., Levy, N. & Wolf, L. "Classification of Artistic Styles using Binarized Features Derived from a Deep Neural Network"
https://www.cs.tau.ac.il/~wolf/papers/genrestyle.pdf
* Banerji, S., Sinha, A. "Painting Classification using a Pre-trained Convolutional Neural Network"
http://math.lakeforest.edu/banerji/research_files/WCVA16.pdf
* Balakrishan, T., Rosston, S., Tang, E. "Using CNN to Classify and Understand Artists from the Rijksmuseum"

### Code Tutorials and Tools
[Using Keras Pre-trained Deep Learning models for your own dataset](https://gogul09.github.io/software/flower-recognition-deep-learning) <br>
[Keras Classification Models](https://github.com/titu1994/Keras-Classification-Models) <br>
[Artist Identification Using CNN](https://github.com/shashankvasisht/Artist-Identification-using-CNN) <br>

