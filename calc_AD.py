import numpy as np
from sklearn.metrics import pairwise_distances


def getNeighborsDitance(trainingSet, testInstance, k):
    neighbors_k= pairwise_distances(trainingSet, Y=testInstance, metric='dice', n_jobs=-1)
    neighbors_k.sort(0)
    similarity= 1-neighbors_k
    return similarity[k-1,:]

def calc_AD(fp, model_fps, model_AD_limit):
    cpd_AD_calc = getNeighborsDitance(model_fps, (np.array(fp).reshape(1, -1)), 5)[0]
    cpd_value = np.round(cpd_AD_calc, 2)
    cpd_AD = np.where(cpd_value >= model_AD_limit, 'Inside AD', 'Outside AD')
    return cpd_AD