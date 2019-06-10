# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:03:50 2019

@author: student
"""

import sys

def get_env():
    sp = sys.path[1].split("/")
    if "envs" in sp:
        return sp[sp.index("envs") + 1]
    else:
        return ""