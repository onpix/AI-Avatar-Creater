import os
from model64 import G, D
import torch
import torchvision
cuda = True
device = torch.device(
    'cuda') if torch.cuda.is_available() and cuda else torch.device('cpu')
nz = 100

#########################    
# mode = 0   # '0 for normal style, 1 for soft style, -1 to debug')
# tune = False
# out_num = 1       #'num of output images.'
# batch_size = 1       #how many figures in a output image.')
# modelNum = [x*10+1 for x in range(10)]+[100]

workDir = os.getcwd()
modelPath = workDir + '/model_normal'
# savePath = workDir + '/output'
# batchSize = opt.batch_size
#################################################

class TestNet(object):
    def __init__(self, out_path, mode, modelNum, img_num, batch_size, tune):
        self.G = G().to(device)
        self.mode = mode
        self.out_path = out_path
        self.modelNum = modelNum
        self.img_num = img_num
        self.batch_size = batch_size
        self.tune = tune

################ init noise code z: #################

    def init(self):
        if self.tune:
            self.img_num = 1
            tmp = torch.randn(nz, 1, 1)
            initZ = torch.randn(self.batch_size, nz, 1, 1)
            for i in range(nz-5):
                for j in range(self.batch_size):
                    initZ[j][i] = tmp[i]
            self.initZ = initZ.to(device)

###################### test:#########################
    def test(self):
        for n in self.modelNum:
            GmodelPath = modelPath + '/Gnn-epoch{}.pkl'.format(n)
            self.G.load_state_dict(torch.load(GmodelPath))
            for i in range(self.img_num):
                if self.tune:
                    z = self.initZ
                else:
                    z = torch.randn(self.batch_size, nz, 1, 1).to(device)
                torchvision.utils.save_image(self.G(z).detach(
                ), self.out_path+'/soft_M{}_{}.jpg'.format(n, i), normalize=True)
        print('\033[1;36;40m  generate over! \033[0m')

############## load model: ###############
#Dnn = D()
# Dnn.load_state_dict(torch.load(modelPath))

def main(out_path, mode=0, model_num=0, img_num=4, batch_size=1, tune=False):
    modelNum = [41, 61, 81, '20_1'] if mode==0 else [31, 71, '_origin']
    modelNum = [modelNum[model_num], ]
    testNet = TestNet(out_path, mode, modelNum, img_num, batch_size, tune)
    testNet.init()
    testNet.test()

if __name__ == '__main__':
    main(out_path='./output', mode=1, model_num=0, img_num=1, batch_size=64, tune=False)
