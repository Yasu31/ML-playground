# Machine Learning Playground
Python scripts to learn various ML (& some statistics) concepts


learnopencv.com is your friend

## three sets
* training set
* validation set: is not used to update model parameters, but to check if model isn't overfitting
* test set

## transfer learning
https://github.com/spmallick/learnopencv/tree/master/Image-Classification-in-PyTorch

Use ResNet50 but change the last layer which is fc 

ResNet: before this, deeper models were hard to train because of the vanishing gradient problem. ResNet introduced a shortcut identity connections (skip connections) skipping 1 or more layers, enabling much deeper networks.

a lot of convolutional layers, followed by a fully connected layer.

