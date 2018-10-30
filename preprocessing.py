import numpy as np

def dataHistogram(images, bins):
    histograms = []
    for image in images:
        histograms.append(np.histogram(image, bins=bins, range=(0, 255))[0])

    return np.stack(histograms)

def threeChannelHistogram(images, bins):
    histograms = []
    for image in images:
        redHist = np.histogram(image[:, :, 0], bins=bins, range=(0, 255))[0]
        greenHist = np.histogram(image[:, :, 0], bins=bins, range=(0, 255))[0]
        blueHist = np.histogram(image[:, :, 0], bins=bins, range=(0, 255))[0]
        #print(np.hstack((redHist, greenHist, blueHist)))
        histograms.append(np.hstack((redHist, greenHist, blueHist)))
        #histograms.append(np.histogram(image, bins=bins, range=(0, 255))[0])
    return np.stack(histograms)

def flattenData(images):
    return images.reshape(images.shape[0], -1)