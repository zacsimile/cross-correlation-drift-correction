# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:06:00 2019

@author: kkc29
"""

from PYME.recipes.base import register_module
from . import processing, localisations, io

def register_module_elsewhere(display_name, module_name, new_parent_module_name=__name__):
    """
        Allows registering recipe module under any branch despite folder/file structure.
        Overwrites __module__. May have unintended consequences.        
    """
        
    module_name.__module__ = __name__
    try:
        register_module(display_name)(module_name)
    except:
        print("failed at registering {} to {}".format(display_name, __name__))
    
register_module_elsewhere('Image_Pre_Clip&Filter', processing.PreprocessingFilter)
register_module_elsewhere('Image_Pre_Downsample', processing.Binning)

register_module_elsewhere('Image_RCC', processing.RCCDriftCorrection)

register_module_elsewhere('Image_Post_Shift', processing.ShiftImage)


register_module_elsewhere('Drift_Save', io.DriftOutput)
register_module_elsewhere('Drift_Load', io.LoadDrift)
register_module_elsewhere('Drift_Interpolate', io.InterpolateDrift)
register_module_elsewhere('Drift_Load_Interpolate', io.LoadDriftandInterp)
#register_module_elsewhere('Drift_Combine', io.DriftCombine)



register_module_elsewhere('Locs_RCC', localisations.RCCDriftCorrection)
register_module_elsewhere('Locs_Post_Shift', localisations.ApplyDrift)
