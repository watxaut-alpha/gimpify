# Gimpify

This repository is intended for creating automatic montages: it pastes
faces onto others faces. That's about it.

## DISCLAIMER
- The aim of this package is not to make it beautiful, it is to make
it a nightmare
- I know there is still room for improvement on the maths for pasting 
images. I will work on it when I have time. Help appreciated! 

## Installation
```bash
pip3 install gimpify-watxaut
```
This package uses [face-recognition](https://github.com/ageitgey/face_recognition) 
from Adam Geitgey to get the faces and 
[pillow](https://pillow.readthedocs.io/en/stable/) to modify and paste 
them. Both get installed when installing this package.

## How to run?
### 1. Search for your images
First, you will need two separate folders, one with 'backgrounds' 
and another with 'faces'. When I talk about backgrounds I mean 
photographs with people AND faces visible. In fact, only the faces are
needed, no need to show any other part of the body. One example of
background:
![This is a background](resources/test/backgrounds/theoffice.png)

When I talk about faces, I mean PNG images with only the face visible, 
like this one:
![This is a face](resources/test/faces/boy.png)

When you have this two folders populated, you are ready to start the
second phase.

### 2.1 The fast approach
If you need to test the power of this package fast, you can do the 
following:
```python
import gimpify
montages_path = "path/out/montages"
path_to_faces_folder = "path/to/folder/faces"
path_to_backgrounds_folder = "path/to/folder/backgrounds"
montage_file_path = gimpify.create_random_montage(montages_path, path_to_backgrounds_folder, path_to_faces_folder)
```

In the montage_file_path variable will be the path to your newly created
montage. This will create a json file inside the images paths so that
the next time will try to get the json instead of loading again the 
images.
CAUTION: if you put new images, you will need to erase the json to
force the creation again.
 

### 2.2: create_face_json and create_background_json
```python
import gimpify
path_to_faces_folder = "path/to/folder/faces"
path_to_backgrounds_folder = "path/to/folder/backgrounds"
json_faces = "path/to/json/faces.json"
json_backgrounds = "path/to/json/backgrounds.json"
gimpify.create_face_json(path_to_faces_folder, path_to_faces_folder)
gimpify.create_background_json(path_to_backgrounds_folder, path_to_backgrounds_folder)
```