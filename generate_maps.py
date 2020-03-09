from rdkit.Chem.Draw import SimilarityMaps
from matplotlib import cm



def pred_frag(mol, model, radius=3, nBits=2048):

    def getProba(fp, probabilityfunc):
        return probabilityfunc(fp)[0][1]

    def fpFunction(mol,atomId=-1):
        fp = SimilarityMaps.GetMorganFingerprint(mol,
                                                 atomId=atomId,
                                                 radius=radius,
                                                 nBits=nBits)
        return fp

    fig = SimilarityMaps.GetSimilarityMapForModel(mol,
                                                  fpFunction,
                                                  lambda x: getProba((x,),
                                                  model.predict_proba),
                                                  colorMap=cm.PiYG_r)