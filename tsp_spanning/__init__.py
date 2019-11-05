"""
This is tsp_spanning module. Currently its only contains :py:func:`tsp` function

.. py:function:: tsp(np.ndarray[np.float64_t, ndim=2] distances, int end=-1)

    Function to calculate tsp path with spanning tree.
    Returned path always start with point with index 0.

    :param distances: distances matrix
    :type distances: np.ndarray[np.float64_t, ndim=2]
    :param end: point in which tsp path should end. -1 means not use
    :return: list of point in order
    :rtype: np.ndarray
"""

from .tsp_wrap import tsp