"""
Test the roi utilities.

Caveat assumes that the MNI template image is available at
in ~/.nipy/tests/data
"""

import numpy as np
import nifti
import os
import tempfile
from nipy.neurospin.utils.roi import ROI, MultipleROI
from nipy.testing import anatfile
RefImage = anatfile
WriteDir = tempfile.mkdtemp()

def test_roi1(verbose=0):
    nim = nifti.NiftiImage(RefImage)
    header = nim.header
    lroi = ROI("myroi",header)
    lroi.from_position(np.array([0,0,0]),5.0)
    roiPath = os.path.join(WriteDir,"myroi.nii")
    lroi.make_image(roiPath)
    assert(os.path.isfile(roiPath))

def test_mroi1(verbose=0):
    nim =  nifti.NiftiImage(RefImage)
    header = nim.header
    mroi = MultipleROI(header=header)
    pos = 1.0*np.array([[10,10,10],[0,0,0],[20,0,20],[0,0,35]])
    rad = np.array([5.,6.,7.,8.0])
    mroi.as_multiple_balls(pos,rad)
    mroi.append_balls(np.array([[-10.,0.,10.]]),np.array([7.0]))
    roiPath = os.path.join(WriteDir,"mroi.nii")
    mroi.make_image(roiPath)
    assert(os.path.isfile(roiPath))
    
def test_mroi2(verbose=0):
    nim =  nifti.NiftiImage(RefImage)
    header = nim.header
    mroi = MultipleROI(header=header)
    pos = 1.0*np.array([[10,10,10],[0,0,0],[20,0,20],[0,0,35]])
    rad = np.array([5.,6.,7.,8.0])
    mroi.as_multiple_balls(pos,rad)
    mroi.append_balls(np.array([[-10.,0.,10.]]),np.array([7.0]))
    mroi.set_roi_feature_from_image('T1_signal',RefImage)
    avt1 = mroi.get_roi_feature('T1_signal')
    assert(np.size(avt1)==5)
    
if __name__ == "__main__":
    import nose
    nose.run(argv=['', __file__])

