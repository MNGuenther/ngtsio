# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:16:48 2016

@author:
Maximilian N. Guenther
Battcock Centre for Experimental Astrophysics,
Cavendish Laboratory,
JJ Thomson Avenue
Cambridge CB3 0HE
Email: mg719@cam.ac.uk
"""



# Examples

import matplotlib.pyplot as plt
from ngtsio import ngtsio

# a) Get and plot the lightcurve for one object

dic = ngtsio.get( 'NG0304-1115', 'CYCLE1706', ['OBJ_ID','HJD','FLUX'], obj_id='00046' )
plt.figure()
plt.plot( dic['HJD'], dic['FLUX'], 'k.' )
plt.title( dic['OBJ_ID'] )

# b) Get and plot the mean locations of the first 100 listed objects on the CCD
#(note that 'CCD_X' denotes the mean location, while 'CCDX' is the location per exposure)

dic = ngtsio.get( 'NG0304-1115', 'CYCLE1706', ['CCD_X','CCD_Y'], obj_row=range(1,101) )
plt.figure()
plt.plot( dic['CCD_X'], dic['CCD_Y'], 'k.' )

# c) Get the BLS results of some candidates 
#(note that obj_id 11 is not a BLS candidate, and that obj_id 1337 does not exist at all)

dic = ngtsio.get( 'NG0304-1115', 'CYCLE1706', ['DEPTH','PERIOD','WIDTH'], obj_id=[11,46,49,54,1337] )
print dic

# d) Get and print a bunch of keys for various non-standard settings

dic = ngtsio.get( 'NG0304-1115', 'CYCLE1706', ['OBJ_ID','SYSREM_FLUX3','RA','DEC','HJD','FLUX','PERIOD','WIDTH'], obj_row=range(0,10), time_date='20151104', indexing='python', fitsreader='pyfits', simplify=False )
for key in dic:
    print '------------'
    print key, dic[key].shape
    print dic[key]
    print '------------'
