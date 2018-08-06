import os
import argparse
import torchvision.models as models
import torch.nn.functional as F
import torchvision.transforms as transforms
import torch.optim as optim
from PIL import Image
import matplotlib.pyplot as plt
import torch.nn as nn
import copy
import numpy as np
import torch


#user options:
#num_steps =300
#style_weight=1e5
#style_num = 1
#
#path options:
# dir_path = '/run/media/why/DATA/why的程序测试/AI_Lab/AI-Avatar-Creater/hackweek/app/draw/static'
basedir = os.path.dirname(__file__)
dir_path = basedir + '/static'
origin_path = dir_path + '/train/'
style_path = dir_path + '/pic/'
out_path = dir_path + '/out/'

#edfault options:
cuda = True
max_size = 256


contentLayers = ['conv_4']
styleLayers = ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5']
contentWeight = 1
unloader = transforms.ToPILImage()
device = torch.device('cuda') if cuda else torch.device('cpu')
cnn = (models.vgg19(pretrained=True).features).eval().to(device)


def loadImg(path):
    img = Image.open(path)
    if img.shape[2] == 4:
        img = Image.open(path).convert("RGB")
    imgSize = img.size if max(img.size)<max_size else max_size
    loader = transforms.Compose(
    [transforms.Resize(imgSize), transforms.CenterCrop(imgSize), transforms.ToTensor()])
    img = (loader(img).unsqueeze(0)).to(device, torch.float)
    return img


def show(tensor):
    image = tensor.cpu().clone()
    image = image.squeeze(0)      # remove the fake batch dimension
    image = unloader(image)
    return image
    #plt.pause(0.1)  # pause a bit so that plots are updated


def calGram(featmap):
    bSize, mapNum, m, n = featmap.size()
    feat = featmap.view(bSize*mapNum, m*n)
    G = torch.mm(feat, feat.t())
    return G.div(bSize*mapNum*m*n)


class contentLoss(nn.Module):
    def __init__(self, content, weight):
        super().__init__()
        self.weight = weight
        self.func = nn.MSELoss()
        self.content = content.detach() * weight

    def forward(self, input):
        self.loss = self.func(input * self.weight, self.content)
        return input

    def backward(self):
        self.loss.backward(retain_graph=True)
        return self.loss


class styleLoss(nn.Module):
    def __init__(self, target, weight):
        super().__init__()
        self.weight = weight
        self.func = nn.MSELoss()
        self.target = calGram(target).detach() * weight

    def forward(self, input):
        self.output = input.clone()
        self.G = calGram(input)
        self.G.mul_(self.weight)
        self.loss = self.func(self.G, self.target)
        return self.output

    def backward(self):
        self.loss.backward(retain_graph=True)
        return self.loss


def calLoss(cnn, origin, target, style_weight):
    cnn = copy.deepcopy(cnn)
    model = nn.Sequential().to(device)
    C_losses = []
    S_losses = []
    i = 0
    for L in cnn.children():
        if isinstance(L, nn.Conv2d):
            i += 1
            name = 'conv_{}'.format(i)
        elif isinstance(L, nn.ReLU):
            name = 'relu_{}'.format(i)
            L = nn.ReLU(inplace=False)
        elif isinstance(L, nn.MaxPool2d):
            name = 'pool_{}'.format(i)
            model.add_module(name, L)
            continue
        model.add_module(name, L)

        if name in contentLayers:
            contentFeat = model(origin).detach()
            C_loss = contentLoss(contentFeat, contentWeight)
            model.add_module("contentLoss{}".format(i), C_loss)
            C_losses.append(C_loss)

        if name in styleLayers:
            styleFeat = model(target).detach()
            S_loss = styleLoss(styleFeat, style_weight)
            model.add_module("styleLoss{}".format(i), S_loss)
            S_losses.append(S_loss)
    return model, C_losses, S_losses


def transfer(cnn, origin, target, inputImg, num_steps, style_weight, style_name, origin_name):
    model, C_losses, S_losses = calLoss(cnn, origin, target, style_weight)
    prama = nn.Parameter(inputImg.data)
    optimizer = optim.LBFGS([prama])
    run = [0]
    while run[0] <= num_steps:
        def closure():
            prama.data.clamp_(0, 1)
            optimizer.zero_grad()
            model(prama)
            styleScore = 0
            contentScore = 0
            for sl in S_losses:
                styleScore += sl.backward()
            for cl in C_losses:
                contentScore += cl.backward()

            run[0] += 1
            if run[0] % 100 == 0:
                print("run {}:".format(run))
                print('Style Loss : {:4f} Content Loss: {:4f}'.format(
                    styleScore.data[0], contentScore.data[0]))
                print()
            return styleScore+contentScore
        optimizer.step(closure)
    prama.data.clamp_(0, 1)
    return prama.data

def main(style_name, origin_name, out_name, num_steps=1, style_weight=1e5):
    #plt.ion()
    target = loadImg(style_path + style_name)
    origin = loadImg(origin_path + origin_name)
    img = origin.clone()
    out = transfer(cnn, origin, target, img, num_steps, style_weight, style_name, origin_name)
    #plt.figure()
    #plt.imshow()
    img = show(out)
    img.save(out_path + out_name)
    # plt.ioff()
    # plt.savefig(out_path + out_name)
    #plt.show()

