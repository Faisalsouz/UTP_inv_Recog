#Three are three model as describe in class 'InvRecog'
#base mdoel, table model and cell_model
# base model path
base_cfg_file = "/net/store/ni/users/fkhalil/TF/InvRecog/darknet/data/custom_data/yolo-obj.cfg"
base_obj_file = "/net/store/ni/users/fkhalil/TF/InvRecog/darknet/data/custom_data/obj.data"
base_weights = "/net/store/ni/users/fkhalil/TF/InvRecog/darknet/backup/yolo-obj_last.weights"
base_thresh  = 0.25
# table mdoel paths
tb_cfg_file = "/net/store/ni/users/fkhalil/TF/InvRecog/darknet/data/custom_data/table_crop/yolo-obj.cfg"
tb_obj_file = "/net/store/ni/users/fkhalil/TF/InvRecog/darknet/data/custom_data/table_crop/obj.data"
tb_weights = "/net/store/ni/users/fkhalil/TF/InvRecog/darknet/backup/mdl_col/yolo-obj_best.weights"
tb_thresh  = 0.25
# model 'cell' paths
cell_cfg_file = "/net/store/ni/users/fkhalil/TF/InvRecog/darknet/data/custom_data/table_crop/cell_config/yolo-obj.cfg"
cell_obj_file = "/net/store/ni/users/fkhalil/TF/InvRecog/darknet/data/custom_data/table_crop/cell_config/obj.data"
cell_weights = "/net/store/ni/users/fkhalil/TF/InvRecog/darknet/backup/mdl_cell/yolo-obj_best.weights"
cell_thresh  = 0.25

#image path
img_path='/net/store/ni/users/fkhalil/TF/InvRecog/darknet/data/custom_data/yolo_data/file-81.jpg'