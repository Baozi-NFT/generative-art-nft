# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder. 
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random. 
#       - array: An array of numbers where each number represents a weight. 
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.                

CONFIG = [
    {
        'id': 1,
        'name': 'Background',
        'directory': 'Background',
        'required': True,
        'rarity_weights': [1111, 1111, 1111, 1111, 1111, 1111, 444, 1111],
    },
    {
        'id': 2,
        'name': 'Body',
        'directory': 'Body',
        'required': True,
        'rarity_weights': [2666, 311, 89, 244, 5000, 244, 133],
    },
    {
        'id': 3,
        'name': 'Head',
        'directory': 'Head',
        'required': True,
        'rarity_weights': [2666, 311, 89, 244, 5000, 244, 133],
    },
    {
        'id': 4,
        'name': 'Clothes',
        'directory': 'Clothes',
        'required': False,
        'rarity_weights': [142, 56, 56, 188, 188, 188, 188, 142, 188, 188, 188, 188, 142, 142, 188, 188, 188, 188, 188, 56, 188, 124, 142, 188, 188, 188, 188, 188, 124, 124, 56, 142, 188, 188, 188, 188, 74, 124, 124, 124],
    },
    {
        'id': 7,
        'name': 'Face',
        'directory': 'Face',
        'required': False,
        'rarity_weights': [5733, 356],
    },
    {
        'id': 5,
        'name': 'Eyes',
        'directory': 'Eyes',
        'required': True,
        'rarity_weights': [533, 356, 533, 444, 267, 133, 3333, 889, 178, 356],
    },
    {
        'id': 6,
        'name': 'Mouth',
        'directory': 'Mouth',
        'required': True,
        'rarity_weights': [111, 444, 444, 356, 622, 444, 178, 622, 622, 1978, 178, 111, 356, 178],
    },
    {
        'id': 8,
        'name': 'Eye Accessories',
        'directory': 'Eye Accessories',
        'required': False,
        'rarity_weights': [6488, 444, 444, 178, 444, 133, 444],
    },
    {
        'id': 9,
        'name': 'Head Accessories',
        'directory': 'Head Accessories',
        'required': False,
        'rarity_weights': [1788, 200, 340, 340, 340, 200, 139, 267, 267, 267, 139, 200, 267, 267, 139, 340, 340, 340, 340, 89],
    },
    {
        'id': 10,
        'name': 'Neck Accessories',
        'directory': 'Neck Accessories',
        'required': False,
        'rarity_weights': [5000, 711, 356, 444],
    },
]
