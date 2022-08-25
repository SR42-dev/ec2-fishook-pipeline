# ec2-fishook-pipeline
A package to get an image and an annotation from a Flutter app, add to the dataset, retrain the model and send the model with the annotation file back.

workflow :

0. loop - continually scan for files in firebase bucket
1. download from firebase into local
2. delete in firebase 
3. send file to correct sub directory in dataset
4. retrain the fishnofish and classification models with new data
5. push model directory content to firebase

setup instructions :

```git clone ```
