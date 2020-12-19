import os,sys
import time
'
#sys.path.append('/home/peter/darknet/python')
# sys.path.append('/home/peter/darknet')

from darknet import performDetect
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import pdb
import shutil
import numpy as np
import cv2
from PIL import Image



#net = dn.load_net(b'/home/peter/darknet/cfg/yolov3-tiny_pdq.cfg',b'/home/peter/darknet/backup/yolov3-tiny_pdq_25700.weights',0)
#meta = dn.load_meta(b'/home/peter/darknet/data/pdq_obj.data')
cfg_file = "/net/store/ni/users/fkhalil/TF/InvRecog/darknet/data/custom_data/table_crop/col_config/yolo-obj.cfg"
obj_file = "/net/store/ni/users/fkhalil/TF/InvRecog/darknet/data/custom_data/table_crop/col_config/obj.data"
weights = "/net/store/ni/users/fkhalil/TF/InvRecog/darknet/backup/mdl_cell/yolo-obj_best.weights"
folder = '/net/store/ni/users/fkhalil/TF/InvRecog/darknet/data/custom_data/table_crop/col_data'
thresh  = 0.25

#while True:
files = os.listdir(folder)
print(files)
#dn.detect fails occasionally. I suspect a race condition.
time.sleep(5)
for f in files:
   if f.endswith(".jpg"):
       print (f)
       path = os.path.join(folder, f)
       pathb = path.encode('utf-8')
       #res = dn.detect(net, meta, pathb)
       try:
          res=performDetect(folder+"/"+f,thresh,cfg_file,weights,obj_file,False,True,False)
          print (res) #list of name, probability, bounding box center x, center y, width, height
       # except:
       #     print('someting went worng')
          i=0
          #new_path = None #initialized to none
          save_path = '/net/store/ni/users/fkhalil/TF/InvRecog/darknet/data/custom_data/table_crop/col_imgs/cell_imgs/' + str(
              i) + f
          img = cv2.imread(path,cv2.IMREAD_COLOR) #load image in cv2
          # img2=imagecv = Image.open(path)
          while i<len(res):

              res_type = res[i][0]

              if "col_head" in res_type:
                  #new_path = '/net/store/ni/users/fkhalil/TF/InvRecog/darknet/data/custom_data/table_crop/col_imgs/cell_imgs/'+str(i)+f
                  box_color = (0, 0, 255)
              # if "cell" in res_type:
              #     box_color=(0,255,0)




                  #copy file to person directory
                  # new_path = '/home/peter/Pictures/person/'+f
                  #set the color for the person bounding box
                  #box_color = (0,255,0)
              # elif "cat" in res_type:
              #     new_path = '/net/store/ni/users/fkhalil/TF/InvRecog/darknet/data/custom_data/table_corp'+f
              #     box_color = (0,255,255)
              # elif "bird" in res_type:
              #     new_path = '/home/peter/Pictures/bird/'+f
              #     box_color = (255,0,0)
              # elif "squirrel" in res_type:
              #     new_path = '/home/peter/Pictures/squirrel/'+f
              #     box_color = (0,0,255)
              #get bounding box
                  center_x=int(res[i][2][0])
                  center_y=int(res[i][2][1])
                  width = int(res[i][2][2])
                  height = int(res[i][2][3])

                  UL_x = int(center_x - width/2) #Upper Left corner X coord
                  UL_y = int(center_y - height/2) #Upper left Y
                  LR_x = int(center_x + width/2)
                  LR_y = int(center_y - height/2)

                  #for cropping the portion and save them.

                  # col_crop=img2.crop((UL_x,UL_y,UL_x+width,UL_y+height))
                  # print(new_path)
                  # col_crop.save(new_path)

              #write bounding box to image
                  cv2.rectangle(img,(UL_x,UL_y),(UL_x+width,UL_y+height),box_color,4)#
                  #put label on bounding box
                  font = cv2.FONT_HERSHEY_SIMPLEX#
                  cv2.putText(img,res_type,(center_x,center_y),font,2,box_color,2,cv2.LINE_AA)#
              i=i+1
          cv2.imwrite(save_path,img) #wait until all the objects are marked and then write out.#
          print('writing image')
          #todo. This will end up being put in the last path that was found if there were multiple
          #it would be good to put it all the paths.
          # try:
          #    os.remove(path) #remove the original
          # except FileNotFoundError as err:
          #    print (err) #file may have been removed by another process
       except ValueError as err:
          print (err)
           
