# Covid-19-Detection-Training-Model
We are training a model based on Convolutional Neural Networks(CNN) in keras 
to detect Covid-19. <br>
Firstly, we coded a program to create our dataset for training our model as in the 
data which we have, have chest x-ray in multiple view angles but we needed chest 
x-ray in posteroanterior (PA) view. The PA chest view examines the lungs, bony 
thoracic cavity, mediastinum and great vessels which is necessary to detect 
Covid-19. <br>
After creating our dataset, we started to code program to train our model. In this 
we multiple python libraries such as numpy, matplotlib, and keras. We use 
sequential model to train our model. In this first we apply four convolutional 2D 
layers then a flattening and a dense layer. After making the setup, we start training 
the model from scratch. Firstly, we alter the image to our needs by rescaling, 
zooming, and other necessary changes. Then we provide path for the model of 
our dataset and divide into classes which is Covid and Normal here. Then we 
divide them into batches so that they can be easily validated. Finally we validate 
the data we have by using model.fit_generator and epoch. In this model which
we trained, we got almost 96.67% accuracy.
