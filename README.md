# ec2-fishook-pipeline
A package to get an image and an annotation from a Flutter app, add to the dataset, retrain the model and send the model with the annotation file back.

### Workflow :

0. loop - continually scan for files in firebase bucket
1. download from firebase into local
2. delete in firebase 
3. send file to correct sub directory in dataset
4. retrain the fishnofish and classification models with new data
5. push model directory content to firebase

### Annotation mappings :

The first character of every file uploaded to the /misclassifications bucket on firebase must be any number from 0 to 8 as per the following mapping ...

'0' : 'Gilt-Head Bream'

'1' : 'Black Sea Sprat'

'2' : 'Trout'

'3' : 'Shrimp'

'4' : 'Red Sea Bream'

'5' : 'Striped Red Mullet'

'6' : 'Red Mullet'

'7' : 'Sea Bass'

'8' : 'Hourse Mackerel'

### Setup instructions :

Assuming the cloud server repository is public, execute the following commands in the linux terminal once :

```git clone https://github.com/SIH-ClapForKrishna/ec2-fishook-pipeline.git```

```cd ec2-fishook-pipeline```

```chmod 777 setup```

```./setup```

Once the previous commands are executed, run this script whenever the server has to carry out the aforementioned workflow. Feel free to call this using any other existing script :

```./run``` 

To run the pipeline periodically every 20 minutes ...

```./server```

Keyboard Interrupt for watch : 

 ```Ctrl + C```

