import os
import sys
import numpy as np
import pytest
from pypheno.mask import InputArrayEmpty, scl_to_mask

current_file_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(
                current_file_dir, '..')))

def test_scl_to_mask():
    test_array = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
    mask_values = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
    test_values = np.repeat(False, test_array.size)
    assert np.all(scl_to_mask(test_array, mask_values)==test_values)

    test_array = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
    mask_values = np.array([0,1,2,3,4])
    test_values = np.hstack((np.repeat(False, mask_values.size),
                             np.repeat(True, 8)))
    assert np.all(scl_to_mask(test_array, mask_values)==test_values)

    with pytest.raises(ValueError):
        _ = scl_to_mask("Wrong data type")

    with pytest.raises(InputArrayEmpty):
        _ = scl_to_mask(np.array([]))
