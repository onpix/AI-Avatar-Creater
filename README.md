# AI-Avatar-Creater
Use GAN (Generative adversarial network) to generate your anime avatar and style transfer!

Note: This codebase was developed in 2018, which is out of date in the 2020s. This code is only for reference and will no longer be updated. Today, a diffusion-based model is recommended for image generation tasks.


![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/hackweek/app/static/pic/bg-index.png)

***

## Contributors

* Algorithm & design：@creeper121386
* Web：@Benjaminyuan
* Deployment：@ThinCats

***

## Introduction

### Real-time style transfer

This is [paper](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf?spm=5176.100239.blogcont62518.12.e6rUdh&file=Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)，可以将用户上传的图片转换特定风格：
  
![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/2018-08-07%2010-35-08%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)
![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/2018-08-07%2010-35-11%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)
![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/2018-08-07%2010-35-17%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)

***

### Use `GAN` to generate anime avatars


![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/sample-epoch41-test0.jpg)

![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/test_2.jpg)

***

## Build
To build, you need:
* NVIDIA with Cuda-toolkit
* PyTorch
```sh
$ pip install PyTorch
```
* Flask (for web view)
```sh
$ pip install flask
```
* Mataplotlib

## Run
1. Go to `hackweek` directory, and then run using `python manage.py`
2. It will download the PyTorch model automatically; wait patiently.
3. If successful, it should appear the basic server information. Go to http://localhost:5000 to have fun

## Future
Docker image (Still waited to be optimized)
