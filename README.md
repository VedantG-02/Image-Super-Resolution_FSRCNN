# Super Resolution of Low Resolution Images
This project reproduces the [paper](https://arxiv.org/abs/1608.00367) (FSRCNN: Fast Super Resolution CNN) using TensorFlow 2 implementation.

## FSRCNN Overview

FSRCNN is a CNN based learning approach for Super Resolution task. It is a single neural network that takes low resolution image as an input, 'cleverly' upscales it and return high resolution image, that is N times larger. N is upscaling factor, in this project N=4. FSRCNN is described as FSRCNN(d, s, m) in the paper where d, s, m are hyperparameters with more details given in the paper.

**Difference with the original paper:**

1. Instead of only SGD optimizer, I implemented RMSProp, Adam as well as SGD optimizers and obtained corresponding results and compared. Also added ReduceLROnPlateau and EarlyStopping callbacks.
2. Authors used [T91](https://www.kaggle.com/datasets/ll01dm/t91-image-dataset) and [General-100](http://mmlab.ie.cuhk.edu.hk/projects/FSRCNN.html) Dataset, but I used [DIV2K Dataset](https://data.vision.ee.ethz.ch/cvl/DIV2K/) as it is newer and larger dataset. I used high resolution images from the link given as both train and validation images. Total 900 images were used: [1..700] train, [701..800] val, [801..900] test. Low resolution of corresponding high resolution images were used as input to the model and were produced by downsampling. All the images are moved into folder `data/DIV2K_train_valid_HR`
3. RandomCrop, HorizontalFlip and ColorJitter image augmentation were used.

**Model Results (PSNR values)**

_Results for m=4_

_more information about PSNR: [here](https://in.mathworks.com/help/vision/ref/psnr.html)_
| d  | s | RMSProp | Adam | SGD |
| :---: | :---: | :---: | :---: | :---: | 
| **56** | **12** | 24.385 | 25.994 | 16.758 |
| **48** | **12** | 25.290 | 26.076 | 16.899 |
| **56** | **16** | 26.320 | 26.390 | 16.540 |
| **48** | **16** | 26.394 | 26.277 | 17.062 |

## Usage

```
python train.py --config config.yaml
```
   
