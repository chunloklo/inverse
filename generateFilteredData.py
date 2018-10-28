import os
from os import listdir
from os.path import isfile, join
from instaFilters import *
import matplotlib.pyplot as plt

def generateFilteredData(path, outPath, fil):
    abspath = os.path.abspath(path)
    print(abspath)
    files = listdir(abspath)
    absFiles = [join(abspath, f) for f in files if isfile(join(abspath, f))]

    absOutPath = os.path.abspath(outPath)

    print(files[0:10])

    i = 0
    for f in files:
        if i % 10 == 0:
            print("Converting image number " + str(i))
        i += 1
        image = plt.imread(join(abspath, f))

        if fil == 'clarendon':
            filteredImage = clarendon(image)
        if fil == 'gingham':
            filteredImage = gingham(image)
        if fil == 'juno':
            filteredImage = juno(image)
        if fil == 'lark':
            filteredImage = lark(image)
        if fil == 'gotham':
            filteredImage = gotham(image)
        if fil == 'reyes':
            filteredImage = reyes(image)

        plt.imsave(join(absOutPath, f), filteredImage)


def generateSpecificFilter(filterName):
    rootPath = 'C:\\Users\\Chunlok Lo\\Documents\\cs4476\\Inverse\\data\\a\\'
    directories = [join(rootPath, f) for f in listdir(rootPath) if not isfile(join(rootPath, f))]

    saveRootPath = 'C:\\Users\\Chunlok Lo\\Documents\\cs4476\\Inverse\\data\\a_' + filterName '\\'
    saveDirectories = [join(saveRootPath, f) for f in listdir(saveRootPath) if not isfile(join(saveRootPath, f))]


    for i in range(len(directories)):
        generateFilteredData(directories[i], saveDirectories[i], filterName)


if __name__ == '__main__':

    rootPath = 'C:\\Users\\Chunlok Lo\\Documents\\cs4476\\Inverse\\data\\a\\'
    directories = [join(rootPath, f) for f in listdir(rootPath) if not isfile(join(rootPath, f))]

    saveRootPath = 'C:\\Users\\Chunlok Lo\\Documents\\cs4476\\Inverse\\data\\a_clarendon\\'
    saveDirectories = [join(saveRootPath, f) for f in listdir(saveRootPath) if not isfile(join(saveRootPath, f))]


    for i in range(len(directories)):
        generateFilteredData(directories[i], saveDirectories[i], 'clarendon')


