import numpy as np

class InputArrayEmpty(Exception):
    """Exception class for empty input"""

def scl_to_mask(scl, mask_values=[0,1,2,3,8,9,10,11]):
    """Sentinel-2 scene classification to boolean mask
       0: Nodata, 1: defective, 8/9/10: cld medium/high/cirrus
       2: dark area, 3: cloud shadows
       11: snow

    Parameters
    ----------
    scl : np.array
        Arbitrary number of dimensions
    mask_values : np.array/list
        Which values should be masked

    Returns
    -------
    np.array
        Boolean array, same shape as scl.
        True corresponds to unmasked/valid values

    """
    if not isinstance(scl, np.ndarray):
        raise ValueError
    if scl.size==0:
        raise InputArrayEmpty
    return np.isin(scl, mask_values, invert=True)
