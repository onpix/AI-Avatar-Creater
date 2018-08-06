import os
from model64 import G, D
import torch
import torchvision
mode = 0   # '0 for normal style, 1 for soft style, -1 to debug')
cuda = True
tune = False
out_num = 1       #'num of output images.'
model_num = 1
batch_size = 1       #how many figures in a output image.')


device = torch.device(
    'cuda') if torch.cuda.is_available() and opt.cuda else torch.device('cpu')
nz = 100
# modelNum = [x*10+1 for x in range(10)]+[100]
if opt.mode == -1:
    modelNum = [41, 61, 81, '20_1'] if opt.mode==0 else [31, 71, '_origin']
else:
    modelNum = [opt.model_num, ]
    NAME = 'normal' if opt.mode==0 else 'soft'
batchSize = opt.batch_size
batchNum = opt.out_num
workDir = os.getcwd()
savePath = workDir + '/output'
modelPath = workDir + '/model_normal'
#################################################

class TestNet(object):
    def __init__(self):
        self.G = G().to(device)
        self.batchNum = batchNum
################ init noise code z: #################

    def init(self):
        if opt.tune:
            self.batchNum = 1
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
            for i in range(batchNum):
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


if __name__ == '__main__':
    testNet = TestNet()
    testNet.init()
    testNet.test()
