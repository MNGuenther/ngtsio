# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:22:11 2016

@author:
Maximilian N. Guenther
Battcock Centre for Experimental Astrophysics,
Cavendish Laboratory,
JJ Thomson Avenue
Cambridge CB3 0HE
Email: mg719@cam.ac.uk
"""


import numpy as np
import ngtsio_find
import ngtsio_get



###############################################################################
# Define version
###############################################################################
__version__ = '1.3.0'



###############################################################################
# Finder (Main Program)
###############################################################################
def find(RA, DEC):
    print '#RA\tDEC\fieldname\tngts_version\obj_id'
    ngtsio_find.find(RA, DEC)
    
    
    
def find_list(fname):
    print '#RA\tDEC\fieldname\tngts_version\obj_id'
    RAs, DECs = np.genfromtxt(fname)
    for i in range(len(RAs)):
        ngtsio_find.find(RAs[i], DECs[i])



###############################################################################
# Getter (Main Program)
###############################################################################

def get(fieldname, keys, obj_id=None, obj_row=None, 
        time_index=None, time_date=None, time_hjd=None, time_actionid=None, 
        bls_rank=1, indexing='fits', fitsreader='fitsio', simplify=True, 
        fnames=None, root=None, roots=None, silent=False, ngts_version='TEST18', 
        set_nan=False):

    dic = ngtsio_get.get(fieldname, keys, obj_id=obj_id, obj_row=obj_row, 
        time_index=time_index, time_date=time_date, time_hjd=time_hjd, time_actionid=time_actionid, 
        bls_rank=bls_rank, indexing=indexing, fitsreader=fitsreader, simplify=simplify, 
        fnames=fnames, root=root, roots=roots, silent=silent, ngts_version=ngts_version, 
        set_nan=set_nan)
        
    return dic
 
 