'''
usage:
main(mode, out_path, tune=0, model_num=2, img_num=4)
    -- out_path: file path without .jpg
    -- tune: set num to config tune level.
'''
import os
from PIL import Image
import random
import torch
import torchvision.utils as vutils
import torchvision.transforms
import models
import re
CUDA = True
# mode =1, # '0 for LL style, 1 for dark style, -1 for test.'
# tune  = False
# choose = 16 # set 0 to close CHOOSE mode
# model_num = 0
DIR = os.getcwd()
device = torch.device('cuda') if CUDA else torch.device('cpu')


def convert_img(img_tensor, nrow):
    img_tensor = img_tensor.to(device)
    grid = vutils.make_grid(img_tensor, nrow=nrow, padding=2)
    grid = grid.cpu()
    ndarr = grid.mul(0.5).add(0.5).mul(
        255).byte().transpose(0, 2).transpose(0, 1).numpy()
    im = Image.fromarray(ndarr)
    return im


def loadG(num, model_path):
    # ngpu, nz, nc, ngf, n_extra_layers
    netG = models._netG_1(1, 100, 3, 64, 1)
    #netG = models._netG_2(1, 100, 3, 64)
    netG = netG.to(device)
    path = model_path+'netG_epoch_{}.pth'.format(num)
    if CUDA:
        state_dict = torch.load(path)
    else:
        state_dict = torch.load(
            path, map_location=lambda storage, loc: storage)
    netG.load_state_dict(state_dict)
    return netG


def loadD(num, model_path):
    netD = models._netD_1(1, 100, 3, 64, 0)
    netD = netD.to(device)
    path = model_path+'netD_epoch_{}.pth'.format(num)
    if CUDA:
        state_dict = torch.load(path)
    else:
        state_dict = torch.load(
            path, map_location=lambda storage, loc: storage)
    netD.load_state_dict(state_dict)
    return netD


def set_z(z, tune, img_num):
    tmp = torch.randn(100, 1, 1)
    new_z = torch.randn(img_num, 100, 1, 1)
    for i in range(100-tune):
        for j in range(img_num):
            new_z[j][i] = tmp[i]
    return new_z.to(device)


def test_tune(mode, tune, img_num, out_path, modelNum, model_path):
    for i in modelNum:
        netG = loadG(i, model_path)
        noise_batch = torch.FloatTensor(
            1, 100, 1, 1).normal_(0, 1).to(device)
        noise_batch = set_z(noise_batch, tune, img_num)
        fake_batch, _ = netG(noise_batch)
        for x in fake_batch:
            im = convert_img(x.data, 8)
            im.save(out_path+'{}.jpg'.format(random.randint(0, 1e5)))


def test_new(mode, choose, img_num, out_path, modelNum, model_path):
    for i in modelNum:
        netG = loadG(i, model_path)
        netD = loadD(i, model_path)
        for j in range(img_num):
            noise_batch = torch.FloatTensor(
                choose, 100, 1, 1).normal_(0, 1).to(device)
            fake_batch, _ = netG(noise_batch)
            score = netD(fake_batch)
            ix = int(torch.argmax(score))
            im = convert_img(fake_batch[ix].data, 8)
            im.save(out_path+'{}.jpg'.format(random.randint(0, 1e5)))


def main(mode, out_path, tune=0, model_num=0, img_num=1):
    root = '/run/media/why/DATA/why的程序测试/AI_Lab/AI-Avatar-Creater/demo_AnimeGAN'
    if mode == 2:
        model_path = root + '/model_dark/'
        modelNum = ['024_M01', '007_M01']
        modelNum = [modelNum[model_num], ]
    elif mode == 6:
        model_path = root + '/model_LL/'
        modelNum = ['40', '60', '80', '160', '80_E3', '80_B16']
        modelNum = [modelNum[model_num], ]
    elif mode == -1:
        model_path = root + '/Data/'
        modelNum = [20, 40, 60, 80]
    # modelNum = list(range(1, 25))
    if tune:
        test_tune(mode, tune, img_num, out_path, modelNum, model_path)
    else:
        test_new(mode, choose=64, img_num, out_path, modelNum, model_path)

if __name__ =='__main__':
    main(mode=6, out_path='./output/tmp', tune=0, model_num=2, img_num=4)
