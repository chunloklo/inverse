from scipy.stats import mode
import numpy as np

def splitImg(X):
    Xsmall = []
    for i in range(X.shape[0]):
        l = 0
        for j in range(0, X.shape[1], X.shape[1] // 4):
            for k in range(0, X.shape[1], X.shape[1] // 4):
                block = X[i, j : j + 32, k : k + 32]
                Xsmall.append(block)
                l += 1
    Xsmall = np.array(Xsmall)
    return Xsmall


def predictionVoting(prediction):
    mapping = ["original", "clarendon", "gingham", "juno", "lark", "gotham", "reyes"]
    predictOrig = []
    votes = np.argmax(predict[i], axis=1)
    vote = mode(votes)
    return mapping[vote]