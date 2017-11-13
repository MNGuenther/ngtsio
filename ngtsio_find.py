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

import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord
import os
import ngtsio_get


def find(RA, DEC, ngts_version='all', unit='hmsdms', frame='icrs', 
         give_obj_id=True, search_radius=0.0014, field_radius=2.,
         outfname=None):
    
    '''
    find the obj_id of a given RA and Dec
    
    Parameters
    ----------
    RA : str
       in h m s as space seperated string
    DEC : str
        in d m s as space seperated string
    unit : str
        'hmsdms', 'deg', 'rad'
    frame : str
        'icrs' or others that astropy accepts
    ngts_version : str
        'all' or e.g. 'CYCLE1706'
    give_obj_id : bool
        also retrieve the obj_id
    search_radius : float
        0.0014 degree = 4.97 arcsec = 1 NGTS pixel
    field_radius : float
        1.92 degree, from center to the corner for square 7.4 sq deg FoV
    ''' 
    
    #list of NGTS fields, lying in the same directory
    fname_fieldlist = os.path.join( os.path.dirname(os.path.realpath(__file__)), 'List_of_observed_NGTS_fields.txt' )
    
    
    #outfile
#    if not os.path.exists(outfname): os.makedirs(outfname)
    
    
    #convert RA and DEC from string into skycoords
    RA_input  = str(RA)
    DEC_input = str(DEC)
    if unit=='hmsdms':
        c   = SkyCoord(RA+' '+DEC, frame=frame, unit=(u.hourangle, u.deg))
        RA  = c.ra.deg
        DEC = c.dec.deg
    elif unit=='deg':
        pass
    elif unit=='rad':
        RA  = RA*180./np.pi
        DEC = DEC*180./np.pi
    
    
    
    #read list of observed NGTS fields from opis (needs to be manually updated)
    d = np.genfromtxt(fname_fieldlist, usecols=[0,3], dtype=None)
    fieldnames    = d[:,0]
    ngts_versions = d[:,1]
    
    
    
    #fc = field_center
    RA_DEC_fc = [ x[2:4]+' '+x[4:6]+' 00' + ' ' + x[6:9]+' '+x[9:11]+' 00' for x in fieldnames ] 
    c_fc      = [ SkyCoord(x, frame='icrs', unit=(u.hourangle, u.deg)) for x in RA_DEC_fc ] 
    RA_fc     = np.array([ x.ra.deg for x in c_fc ])
    DEC_fc    = np.array([ x.dec.deg for x in c_fc ])
    
    
    
    #indices where the searched RA / DEC may be covered in an NGTS field (upper limit)
    if ngts_version == 'all':
        ind_field = np.where( (np.abs(RA_fc - RA) < field_radius) 
                      & (np.abs(DEC_fc - DEC) < field_radius) )[0]
    else:
        ind_field = np.where( (np.abs(RA_fc - RA) < field_radius) 
                      & (np.abs(DEC_fc - DEC) < field_radius) 
                      & (ngts_versions == ngts_version) )[0]
    
    

    #retrieve object ids via ngtsio_get   
    if (give_obj_id is True):
        obj_id = ['None']*len(fieldnames)
        for i in ind_field:
            
            dic = ngtsio_get.get(fieldnames[i][0:11], ['RA','DEC'], ngts_version=ngts_versions[i], silent=True) 
            
            if dic is not None:  
                #RA and DEC come out in degree
                RA_objs = dic['RA']
                DEC_objs = dic['DEC']
                
                ind_obj = np.where( (np.abs(RA_objs - RA) < search_radius) 
                                  & (np.abs(DEC_objs - DEC) < search_radius) )[0]
                                 
                if len(ind_obj) > 0:
                    obj_id[i] = dic['OBJ_ID'][ind_obj]
            
            else:
                obj_id[i] = 'fits_not_available'
    else:
        obj_id = ['']*len(fieldnames)
        
        
        
    #output
    def printer(outfile):
        if len(ind_field) == 0:
            line = RA_input +'\t'+ DEC_input +'\t'+ 'no match'
            print line
            if outfile is not None: outfile.write(line+'\n')
        else:
    #        print RA, DEC, 'in fields:'
            for i in ind_field:
    #            print list(obj_id[i])
                if (obj_id[i] is not 'None') & (obj_id[i] is not 'fits_not_available'):
                    obj_id_str = '\t'.join( list(obj_id[i]) )
                else:
                    obj_id_str = obj_id[i]
                line = RA_input +'\t'+ DEC_input +'\t'+ fieldnames[i][0:11] +'\t'+ ngts_versions[i] +'\t'+ obj_id_str
                print line
                if outfile is not None: outfile.write(line+'\n')
                
    
    if outfname is not None:            
        with open(outfname, 'a') as outfile:
            printer(outfile)
    else:
        printer(None)
        
            
    
if __name__ == '__main__':
    pass