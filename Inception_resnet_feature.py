import numpy as np
import os
from keras.models import Sequential
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.layers.core import Flatten, Dense, Dropout
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from args import parser

args = parser.parse_args()
path_save_InceptionResnet= args.InceptionResnet_features_path

path_audio_img= args.audio_images_folder_path

path_save_rgb= os.path.join(path_audio_img, 'RGB_sound.npy')

RGB_sound=np.load(path_save_rgb)

print('shape RGB sound',RGB_sound.shape)


model = InceptionResNetV2(weights='imagenet', include_top=False)


preds = model.predict(RGB_sound)


print('pred_reduc taille',preds.shape)

modelbis = Sequential()

modelbis.add(ZeroPadding2D((1,1),input_shape=(8,8,1536)))
modelbis.add(MaxPooling2D((2,2), strides=(2,2)))


pred_reduc_pool=modelbis.predict(preds)

print('pool pred_reduc taille',pred_reduc_pool.shape)

pred_reduc_pool = pred_reduc_pool.reshape((-1,1536 * 5 * 5))

print('concatenate in size',pred_reduc_pool.shape)


path_save_features= os.path.join(path_save_InceptionResnet, 'InceptionResnet_feat')


np.save(path_save_features,pred_reduc_pool)
print('ended successfully')