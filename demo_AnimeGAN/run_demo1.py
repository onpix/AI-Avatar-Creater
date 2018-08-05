import os
import argparse
from PIL import Image
import random
import torch
import torchvision.utils as vutils
import torchvision.transforms
import models
import re
parse = argparse.ArgumentParser()
parse.add_argument('--mode', type=int, default=1, help='0 for LL style, 1 for dark style, -1 for test.')
parse.add_argument('--cuda', action='store_true', help='use cuda in trainning.')
parse.add_argument('--tune', action='store_true', help='to freeze some dimensions of tensor z to tune the image.')
parse.add_argument('--choose', type=int, default=16, help='set 0 to close choose mode, set n to choose the best image from n generated samples')
parse.add_argument('--model_num', type=str, required=True, help='num of model to use.')
opt = parse.parse_args()

DIR = '/run/media/why/DATA/why的程序测试/AI_Lab/Task/AnimeProject/demo_AnimeGAN'
device = torch.device('cuda') if opt.cuda else torch.device('cpu')
per_num = 4
save_path = DIR + '/output'
if opt.mode == 1:
    model_path = DIR + '/model_dark/'
    modelNum = ['024_M01', '007_M01']
    modelNum = [opt.model_num, ]
elif opt.mode == 0:
    model_path = DIR + '/model_LL/'
    modelNum = ['40', '60', '80', '160', '80_E3', '80_B16']
    modelNum = [opt.model_num, ]
elif opt.mode == -1:
    model_path = DIR + '/Data/'
    modelNum = [20, 40, 60, 80]
# modelNum = list(range(1, 25))


def convert_img(img_tensor, nrow):
    img_tensor = img_tensor.to(device)
    grid = vutils.make_grid(img_tensor, nrow=nrow, padding=2)
    grid = grid.cpu()
    ndarr = grid.mul(0.5).add(0.5).mul(
        255).byte().transpose(0, 2).transpose(0, 1).numpy()
    im = Image.fromarray(ndarr)
    return im


def load_old():
    # ngpu, nz, nc, ngf, n_extra_layers
    netG = models._netG_1(1, 100, 3, 64, 1)
    netG = netG.to(device)
    if opt.cuda:
        state_dict = torch.load(model_path)
    else:
        state_dict = torch.load(
            model_path, map_location=lambda storage, loc: storage)
    self_state = netG.state_dict()
    for name, param in state_dict.items():
        param = param.to(device)
        if name not in self_state and isinstance(param, torch.Tensor):
            for x, y in self_state.items():
                res = re.match(name, x)
                if res:
                    self_state[x].copy_(param)
                    break
    return netG


def loadG(num):
    # ngpu, nz, nc, ngf, n_extra_layers
    netG = models._netG_1(1, 100, 3, 64, 1)
    #netG = models._netG_2(1, 100, 3, 64)
    netG = netG.to(device)
    path = model_path+'netG_epoch_{}.pth'.format(num)
    if opt.cuda:
        state_dict = torch.load(path)
    else:
        state_dict = torch.load(
            path, map_location=lambda storage, loc: storage)
    netG.load_state_dict(state_dict)
    return netG


def loadD(num):
    netD = models._netD_1(1, 100, 3, 64, 0)
    netD = netD.to(device)
    path = model_path+'netD_epoch_{}.pth'.format(num)
    if opt.cuda:
        state_dict = torch.load(path)
    else:
        state_dict = torch.load(
            path, map_location=lambda storage, loc: storage)
    netD.load_state_dict(state_dict)
    return netD


def set_z(z):
    tmp = torch.randn(100, 1, 1)
    new_z = torch.randn(64, 100, 1, 1)
    for i in range(100-5):
        for j in range(64):
            new_z[j][i] = tmp[i]
    return new_z.to(device)


def test():
    for i in modelNum:
        netG = loadG(i)
        for j in range(per_num):
            noise_batch = torch.FloatTensor(
                1, 100, 1, 1).normal_(0, 1).to(device)
            if opt.tune:
                noise_batch = set_z(noise_batch)
            fake_batch, _ = netG(noise_batch)
            im = convert_img(fake_batch.data, 8)
            im.save('{}/epoch{}_{}.jpg'.format(save_path, i, random.randint(0, 1e5)))


def test_new():
    for i in modelNum:
        netG = loadG(i)
        netD = loadD(i)
        for j in range(per_num):
            noise_batch = torch.FloatTensor(
                opt.choose, 100, 1, 1).normal_(0, 1).to(device)
            if opt.tune:
                noise_batch = set_z(noise_batch)
            fake_batch, _ = netG(noise_batch)
            score = netD(fake_batch)
            # tmp = torch.ones(score.size()).to(device)
            # score = torch.abs(score - tmp)
            ix = int(torch.argmax(score))
            im = convert_img(fake_batch[ix].data, 8)
            im.save('{}/epoch{}_{}.jpg'.format(save_path, i, random.randint(0, 1e5)))


if opt.choose:
    test_new()
else:
    test()
