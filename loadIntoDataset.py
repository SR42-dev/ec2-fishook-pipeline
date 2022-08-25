# a script to load the images from the misclassified images' directory to the dataset

# library imports
import os
import shutil

# annotation mappings
annotationMappings = {
    '0': 'Gilt-Head Bream',
    '1': 'Black Sea Sprat',
    '2': 'Trout',
    '3': 'Shrimp',
    '4': 'Red Sea Bream',
    '5': 'Striped Red Mullet',
    '6': 'Red Mullet',
    '7': 'Sea Bass',
    '8': 'Hourse Mackerel'
}

# iterating through the misclassified images' directory
for file in os.listdir('./misclassifications'):
    annotation = annotationMappings[file[0:1]]
    
    # moving the files to the dataset directory
    src_path = './misclassifications/' + file
    dst_path = './datasets/dataset/' + annotation + '/' + annotation  + '/' + file
    shutil.move(src_path, dst_path)
