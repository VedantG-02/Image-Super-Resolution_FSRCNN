from tensorflow import keras
from keras import Sequential
from keras import initializers
from keras.layers import Conv2D, Conv2DTranspose, InputLayer, PReLU, Activation

from utils.constants import LR_IMG_SIZE, UPSCALING_FACTOR, COLOR_CHANNELS

def create_model(
        d: int,
        s: int,
        m: int,
        input_size: tuple = LR_IMG_SIZE,
        upscaling_factor: int = UPSCALING_FACTOR,
        color_channels: int = COLOR_CHANNELS,
):
    '''
    function to create a model with architecture as given in the referred paper
    '''
    model = Sequential()
    model.add(InputLayer(input_shape=(input_size[0], input_size[1], color_channels)))

    # feature extraction
    model.add(Conv2D(
        kernel_size=5,
        filters=d,
        padding='same',
        kernel_initializer=initializers.HeNormal(),
    ))
    model.add(PReLU(alpha_initializer="zeros", shared_axes=[1, 2]))

    # shrinking
    model.add(Conv2D(
        kernel_size=1,
        filters=s,
        padding='same',
        kernel_initializer=initializers.HeNormal(),
    ))
    model.add(PReLU(alpha_initializer="zeros", shared_axes=[1, 2]))

    # mapping
    for _ in range(m):
        model.add(Conv2D(
            kernel_size=3,
            filters=s,
            padding='same',
            kernel_initializer=initializers.HeNormal(),
        ))
        model.add(PReLU(alpha_initializer="zeros", shared_axes=[1, 2]))
    
    # expanding
    model.add(Conv2D(
        kernel_size=1,
        filters=d,
        padding='same'
    ))
    model.add(PReLU(alpha_initializer="zeros", shared_axes=[1, 2]))

    # deconvolution
    model.add(Conv2DTranspose(
        kernel_size=9,
        filters=color_channels,
        strides=upscaling_factor,
        padding='same',
        kernel_initializer=initializers.RandomNormal(mean=0, stddev=0.001),
    ))


    return model
