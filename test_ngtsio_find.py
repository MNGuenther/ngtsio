# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:07:19 2016

@author:
Maximilian N. Guenther
Battcock Centre for Experimental Astrophysics,
Cavendish Laboratory,
JJ Thomson Avenue
Cambridge CB3 0HE
Email: mg719@cam.ac.uk
"""



import ngtsio

    
if __name__ == '__main__':  
#    ngtsio.find('03 05 00', '-11 55 00', ngts_version='all', search_radius=0.01)
#    ngtsio.find('03 05 00', '-11 55 00', ngts_version='TEST18', search_radius=0.01)
#    ngtsio.find('03 05 00', '-11 55 00', ngts_version='TEST18', search_radius=0.04)
#    ngtsio.find(0.82299971580505371, -0.17282542586326599, ngts_version='TEST18', unit='rad')

#    ngtsio.find_list('/Users/mx/Desktop/Astrometric_Binaries_coords.txt')
#    ngtsio.find_list('/Users/mx/Desktop/Planets.txt', usecols=(0,2))   
    ngtsio.find_list('/Users/mx/Desktop/Planets.txt', usecols=(0,2), outfname='/Users/mx/Desktop/output_ngtsio_find.txt')   

#    ngtsio.find('05 23 31.6', '-25 08 48.4', ngts_version='TEST18')