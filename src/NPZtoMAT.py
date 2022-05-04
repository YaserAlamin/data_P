import numpy as np
import scipy.io as sio 
modelname='model_9829'

with np.load('models/'+modelname+'.npz') as data:
    
    centers = data['centers']
    features = data['features']
    spreads = data['spreads']
    weights = data['weights']
    
    
# print(type(centers),type(features),type(spreads),type(weights))
print(centers.shape, features.shape, spreads.shape , weights.shape)

print(features)
# print(spreads)

matfilename='models/'+modelname+'.mat'
sio.savemat(matfilename, {'centers':centers,'features':features,'spreads':spreads,'weights':weights})

print('ok',modelname)