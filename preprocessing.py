import numpy as np

def dataHistogram(images):
    histograms = []
    for image in images:
        histograms.append(np.histogram(image, bins=10000, range=(0, 255))[0])

    return np.stack(histograms)

def flattenData(images):
    return images.reshape(images.shape[0], -1)