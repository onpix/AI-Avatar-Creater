import os
from model64 import G, D
import torch
import torchvision
cuda = True
device = torch.device(
    'cuda') if torch.cuda.is_available() and opt.cuda else torch.device('cpu')
nz = 100

#########################    
# mode = 0   # '0 for normal style, 1 for soft style, -1 to debug')
# tune = False
# out_num = 1       #'num of output images.'
# batch_size = 1       #how many figures in a output image.')
# modelNum = [x*10+1 for x in range(10)]+[100]

batchSize = opt.batch_size
workDir = os.getcwd()
savePath = workDir + '/output'
modelPath = workDir + '/model_normal'
#################################################

class TestNet(object):
    def __init__(self, mode, modelNum, img_num, batch_size, tune):
        self.G = G().to(device)
        self.mode = mode
        self.modelNum = modelNum
        self.img_num = img_num
        self.batch_size = batch_size
        self.tune = tune
################ init noise code z: #################

    def init(self):
        if opt.tune:
            self.img_num = 1
            tmp = torch.randn(nz, 1, 1)
            initZ = torch.randn(batchSize, nz, 1, 1)
            for i in range(nz-5):
                for j in range(batchSize):
                    initZ[j][i] = tmp[i]
            self.initZ = initZ.to(device)

###################### test:#########################
    def test(self):
        for n in modelNum:
            GmodelPath = modelPath + '/Gnn-epoch{}.pkl'.format(n)
            self.G.load_state_dict(torch.load(GmodelPath))
            for i in range(self.img_num):
                if opt.tune:
                    z = self.initZ
                else:
                    z = torch.randn(batchSize, nz, 1, 1).to(device)
                torchvision.utils.save_image(self.G(z).detach(
                ), savePath+'/soft_M{}_{}.jpg'.format(n, i), normalize=True)
        print('\033[1;36;40m  generate over! \033[0m')

############## load model: ###############
#Dnn = D()
# Dnn.load_state_dict(torch.load(modelPath))

def main(mode=0, model_num=0, img_num=4, batch_size=1, tune=False):
    modelNum = [41, 61, 81, '20_1'] if mode==0 else [31, 71, '_origin']
    modelNum = [modelNum[model_num], ]
    testNet = TestNet(mode, modelNum, img_num, batch_size, tune)
    testNet.init()
    testNet.test()

if __name__ == '__main__':
    main(mode=0, model_num=0, img_num=4, tune=False)
