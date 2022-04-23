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

a lot of convolutional layers, followed by a fully connected layer. In the learnopencv page, this final layer is re-learned with a new class of images, and the learning process is actually feasible on a laptop CPU!

## Semantic segmentation
https://learnopencv.com/pytorch-for-beginners-semantic-segmentation-using-torchvision/

https://github.com/spmallick/learnopencv/tree/master/PyTorch-Segmentation-torchvision

How to train this? -> see image-segmentation.ipynb

tbh so much simpler than I imagined- the learning structure is exactly the same, the very same network could also possibly be used for classification (as long as the output dimensions are correct). It's the structure that makes it better suited for segmentation, but in theory segmentation could also be done with a conventional MLP. It sounds like dataset collection is the hard part...
