import torch.nn as nn
import torch
# [DCGAN info] epoch == 10左右已经收敛，效果最好的情况在epoch == 60和80处，epoch == 100开始出现大量随机噪声


nz = 100        # size of z
nc = 3         # channel数
ndf = 64      # D的feature map数量
ngf = 64       # G的feature map数量
device = torch.device(
    'cuda') if torch.cuda.is_available() else torch.device('cpu')

class D(nn.Module):
    def __init__(self):
        super(D, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(nc, ndf, 4, 2, 1),
            nn.BatchNorm2d(ndf),
            nn.LeakyReLU(0.2, inplace=True),
        )
        self.layer2 = nn.Sequential(
            nn.Conv2d(ndf, ndf*2, 4, 2, 1),
            nn.BatchNorm2d(ndf*2),
            nn.LeakyReLU(0.2, inplace=True)
        )
        self.layer3 = nn.Sequential(
            nn.Conv2d(ndf*2, ndf*4, 4, 2, 1),
            nn.BatchNorm2d(ndf*4),
            nn.LeakyReLU(0.2, inplace=True)
        )
        self.layer4 = nn.Sequential(
            nn.Conv2d(ndf*4, ndf, 4, 2, 1),
            nn.BatchNorm2d(ndf),
            nn.LeakyReLU(0.2, inplace=True)
        )
        self.layer5 = nn.Sequential(
            nn.Conv2d(ndf, 1, 4, 1, 0),
            nn.Sigmoid()
        )

    def forward(self, x):
        # return self.layers(input).view(-1, 1).squeeze(1)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.layer5(x)
        return x


class G(nn.Module):
    def __init__(self):
        super(G, self).__init__()
        self.layers = nn.Sequential(
            nn.ConvTranspose2d(nz, ngf*4, 4),
            nn.BatchNorm2d(ngf*4),
            nn.ReLU(),

            nn.ConvTranspose2d(ngf*4, ngf*2, 4, 2, 1),
            nn.BatchNorm2d(ngf*2),
            nn.ReLU(),

            nn.ConvTranspose2d(ngf*2, ngf, 4, 2, 1),
            nn.BatchNorm2d(ngf),
            nn.ReLU(),

            nn.ConvTranspose2d(ngf, int(ngf/2), 4, 2, 1),
            nn.BatchNorm2d(int(ngf/2)),
            nn.ReLU(),

            nn.ConvTranspose2d(int(ngf/2), nc, 4, 2, 1),
            nn.Tanh()
        )

    def forward(self, x):
        return self.layers(x)