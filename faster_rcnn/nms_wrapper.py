# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from nms.cpu_nms import cpu_nms

def nms(dets, thresh, force_cpu=True):
  """Dispatch to CPU NMS implementations."""

  if dets.shape[0] == 0:
    return []
  
  return cpu_nms(dets, thresh)
