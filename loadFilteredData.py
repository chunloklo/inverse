import os
from os import listdir
from os.path import isfile, join

import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import shuffle

def loadFilteredData(path, filPath):
    abspath = os.path.abspath(path)
    absFilPath = os.path.abspath(filPath)
    files = [f for f in listdir(abspath) if isfile(join(abspath, f))]

    imgList = []
    imgFilteredList = []

    for f in files:
        img = plt.imread(join(abspath, f))
        imgList.append(img)

        imgFil = plt.imread(join(absFilPath, f))
        imgFilteredList.append(imgFil)
    imgData = np.stack(imgList)
    imgFilteredData = np.stack(imgFilteredList)

    return imgData, imgFilteredData

def createTrainingData(images, trainPercentage):
    categories = len(images)

    imgList = []
    vectors = []

    testImgList = []
    testVectors = []


    #data for original image
    for c in range(categories):
        numImages = images[c].shape[0]
        numTrain = int(numImages * trainPercentage)
        imgList.append(images[c][:numTrain])

        featureVector = np.zeros((numTrain, categories))
        featureVector[:, c] = 1
        vectors.append(featureVector)

        #testing data
        testImgList.append(images[c][numTrain:])
        featureVector = np.zeros((numImages - numTrain, categories))
        featureVector[:, c] = 1
        testVectors.append(featureVector)


    X = np.vstack(imgList)
    y = np.vstack(vectors)

    Xtest = np.vstack(testImgList)
    ytest = np.vstack(testVectors)

    X, y = shuffle(X, y, random_state=0)
    Xtest, ytest = shuffle(Xtest, ytest, random_state=0)
    return X, y, Xtest, ytest

    print(X.shape)
    print(y.shape)

if __name__ == '__main__':

    path = 'C:\\Users\\Chunlok Lo\\Documents\\cs4476\\Inverse\\data\\a\\abbey'
    filPath = 'C:\\Users\\Chunlok Lo\\Documents\\cs4476\\Inverse\\data\\a_clarendon\\abbey'

    origImg, filImg = loadFilteredData(path, filPath, .9)

    Xtest, ytest = createTrainingData([origImg, filImg])


    # rootPath = 'C:\\Users\\Chunlok Lo\\Documents\\cs4476\\Inverse\\data\\a\\'
    # directories = [join(rootPath, f) for f in listdir(rootPath) if not isfile(join(rootPath, f))]

    # saveRootPath = 'C:\\Users\\Chunlok Lo\\Documents\\cs4476\\Inverse\\data\\a_clarendon\\'
    # saveDirectories = [join(saveRootPath, f) for f in listdir(saveRootPath) if not isfile(join(saveRootPath, f))]


    # for i in range(len(directories)):
    #     generateFilteredData(directories[i], saveDirectories[i], 'clarendon')