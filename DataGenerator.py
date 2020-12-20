from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from PIL import Image


import numpy as np
img= load_img('bird.jpg')
img= img_to_array(img)
#chan1=im_array[:,:,0]
# img=Image.fromarray(chan1)
# img.show()

img= np.expand_dims(img,axis=0)
aug=ImageDataGenerator(rotation_range=30,zoom_range=0.15,width_shift_range=0.2,
                       shear_range=0.15,horizontal_flip=True,fill_mode='nearest'
                       ,channel_shift_range=100,brightness_range=(0.5,2.0)
                       ,vertical_flip=True,samplewise_center=True,rescale=1./255)


imgGen=aug.flow(img,batch_size=1,save_to_dir='./augmented_Images',save_prefix='agu',save_format='jpg')
total=0
for i in imgGen:
    #print(i)
    total+=1
    if total==100:
        break
