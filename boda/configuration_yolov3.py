from typing import Tuple, List, Dict
from urllib.parse import MAX_CACHE_SIZE
from .configuration_base import PretrainedConfig


YOLOV1_PRETRAINED_CONFIG = {
    'yolov1-base': None,
    'yolov1-tiny': None,
}


class Yolov3Config(PretrainedConfig):
    def __init__(
        self, 
        selected_layers=-1,
        grid_size=7, 
        num_boxes=2,
        max_size=416,
        num_classes=20,
        **kwargs):
        super().__init__(max_size=max_size, **kwargs)
        self.selected_layers = selected_layers
        self.grid_size = grid_size
        self.num_boxes = num_boxes
        self.num_classes = num_classes
        self.obj_scale = 1
        self.noobj_scale = 0.5
        self.class_scale = 1
        self.coord_scale = 5
        self.jitter = 0.3
        self.lambda_coord = 5.0
        self.lambda_noobj = 0.5
        self.sqrt = 1
        self.anchors = ((10, 13), (16, 30), (33, 23), (30, 61), (62, 45), (59, 119), (116, 90), (156, 198), (373, 326))
        self.ignore_thresh = 0.7
        self.truth_thresh = 1.0



        

#    'name': 'yolov1 base',
#     'dataset': pascal_voc_datset,
#     'backbone': darknet9_backbone,
#     'augmentation': None,
#     'max_size': (448, 448),  # width, height
#     'batch_size': 32,  # train batch size 64
#     'max_iter': 40000,  # max_batches
#     'lr': 0.0005,
#     'momentum': 0.9,
#     'decay': 0.0005,
#     'lr_steps': (200, 400, 600, 20000, 30000),
#     'lr_scales': (2.5, 2.0, 2.0, 0.1, 0.1),
#     'num_boxes': 2,
#     'grid_size': 7,
#     'object_scale': 1,
#     'noobject_scale': 0.5, 
#     'class_scale': 1,
#     'coord_scale': 5,
#     'jitter': 0.2, 
#     'rescore': 1,
#     'sqrt': 1,
#     'num': 3,  # ????
#     'lambda_coord': 5.0,
#     'lambda_noobj': 0.5,

# cfg = [
#     (7, 64, 2), 'M', 
#     (3, 192), 'M',
#     (1, 128), (3, 256), (1, 256), (3, 512), 'M',
#     [(1, 256), (3, 512), 4], (1, 512), (3, 1024), 'M',
#     [(1, 512), (3, 1024), 2], (3, 1024), (3, 1024), 
#     (3, 1024), (3, 1024),
# ]


# backbone_base = Config({
#     'name': 'base backbone',
#     'pretrained': bool,
#     'path': 'path/to/pretrained/weights',
# })

# model_base = Config({
#     'name': 'base model',
#     'path': 'path/to/pretrained/weights',
#     'dataset': dataset_base,
#     'backbone': backbone_base,
#     'batch_size': int,
#     'max_size': Tuple[int, int],
#     'lr': float,
# })





