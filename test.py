import keras

def unpickle(file):
    import cPickle
    with open(file, 'rb') as fo:
        dict = cPickle.load(fo)
    return dict

d = unpickle("./data_batch_1")
print(d["labels"])