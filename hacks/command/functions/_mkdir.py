# coding: utf-8

import os
import errno


def _mkdir(abspath):
    try:
        os.makedirs(abspath)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else: raise
