# -*- coding: utf-8 -*-
"""
Editor de Spyder
"""
import os
from nilearn import plotting
data_path = 'D:\P\Medica'
example_file = os.path.join(data_path, 'T1_brain_extractedBrainExtractionBrain.nii.gz')

import nibabel as nib
img = nib.load(example_file)
plotting.plot_stat_map(img, threshold=3)
