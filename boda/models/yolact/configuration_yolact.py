import os
from typing import Optional, Tuple, List, Union, Any, Dict
from ...base_configuration import BaseConfig


YOLACT_PRETRAINED_CONFIG = {
    'yolact-base': 'https://drive.google.com/file/d/1i_Wqc4gxY_u4F7sn2kVbpmce5iQRxMKm/view?usp=sharing',
    'yolact-300': '',
    'yolact-700': '',
}


class YolactConfig(BaseConfig):
    """Configuration for YOLACT

    Args:
        max_size (:obj:`Union[int, Tuple[int]]`):
        num_classes (:obj:`int`):
        num_grids (:obj:`int`):
        num_grid_sizes (:obj:`int`):
        num_mask_dim (:obj:`int`):

        extra_layers (:obj:`int`):
        extra_layer_structure (:obj:`int`):
        proto_layer_structure (:obj:`List[]):
        mask_dim (:obj:`int`):
        num_grid_sizes (:obj:`int`):
        num_mask_dim (:obj:`int`):

    """
    model_name = 'yolact'

    def __init__(
        self,
        num_classes: int = 80,
        label_map: Dict = None,
        max_size: Tuple[int] = (550, 550),
        fpn_channels: int = 256,
        num_extra_fpn_layers: int = 2,
        selected_layers: List[int] = [1, 2, 3],
        aspect_ratios: List = [[[1, 1/2, 2]]] * 6,
        scales: List = [[24], [48], [96], [192], [384]],
        extra_head_layer_structure: List = [(256, 3, {'padding': 1})],
        num_extra_box_layers: int = 0,
        num_extra_mask_layers: int = 0,
        num_extra_score_layers: int = 0,
        use_preapply_sqrt: bool = False,
        use_pixel_scales: bool = True,
        use_square_anchors: bool = True,
        num_grids: int = 0,
        mask_size: int = 16,
        mask_dim: int = 0,
        protonet_structure: Optional[int] = None,
        box_weight: float = 1.0,
        mask_weight: float = 6.125,
        score_weight: float = 1.0,
        semantic_weight: float = 1.0,
        **kwargs
    ) -> None:
        super().__init__(max_size=max_size, **kwargs)
        self.num_classes = num_classes + 1
        self.label_map = {}
        self.fpn_channels = fpn_channels
        self.num_fpn_extra_layers = num_extra_fpn_layers
        self.selected_layers = selected_layers
        self.aspect_ratios = aspect_ratios
        self.scales = scales
        self.num_grids = num_grids
        self.mask_size = mask_size
        self.use_preapply_sqrt = use_preapply_sqrt
        self.use_pixel_scales = use_pixel_scales
        self.use_square_anchors = use_square_anchors

        self.num_extra_box_layers = num_extra_box_layers
        self.num_extra_mask_layers = num_extra_mask_layers
        self.num_extra_score_layers = num_extra_score_layers
        self.num_grids = num_grids
        self.mask_size = mask_size
        self.mask_dim = mask_dim

        self.extra_head_layer_structure = extra_head_layer_structure
        self.protonet_structure = protonet_structure

        self.box_weight = box_weight
        self.mask_weight = mask_weight
        self.score_weight = score_weight
        self.semantic_weight = semantic_weight