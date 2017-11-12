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
import sys
import timeit

import ngtsio

keys =  [
        'OBJ_ID', 'RA', 'DEC', 'REF_FLUX', 'CLASS', 'CCD_X', 'CCD_Y', 'FLUX_MEAN', 'FLUX_RMS', 'MAG_MEAN', 'MAG_RMS', 'NPTS', 'NPTS_CLIPPED',
        'ACQUMODE', 'ACTIONID', 'ACTSTART', 'ADU_DEV', 'ADU_MAX', 'ADU_MEAN', 'ADU_MED', 'AFSTATUS', 'AGREFIMG', 'AGSTATUS', 'AG_APPLY', 'AG_CORRX', 'AG_CORRY', 'AG_DELTX', 'AG_DELTY', 'AG_ERRX', 'AG_ERRY', 'AIRMASS', 'BIASMEAN', 'BIASOVER', 'BIASPRE', 'BIAS_ID', 'BKG_MEAN', 'BKG_RMS', 'CAMERAID', 'CAMPAIGN', 'CCDTEMP', 'CCDTEMPX', 'CHSTEMP', 'CMD_DEC', 'CMD_DMS', 'CMD_HMS', 'CMD_RA', 'COOLSTAT', 'CROWDED', 'CTS_DEV', 'CTS_MAX', 'CTS_MEAN', 'CTS_MED', 'DARK_ID', 'DATE-OBS', 'DATE', 'DITHER', 'EXPOSURE', 'FCSR_ENC', 'FCSR_PHY', 'FCSR_TMP', 'FIELD', 'FILTFWHM', 'FLAT_ID', 'FLDNICK', 'GAIN', 'GAINFACT', 'HSS_MHZ', 'HTMEDXF', 'HTRMSXF', 'HTXFLAGD', 'HTXNFLAG', 'HTXRAD1', 'HTXSIG1', 'HTXTHTA1', 'HTXVAL1', 'IMAGE_ID', 'IMGCLASS', 'IMGTYPE', 'LST', 'MINPIX', 'MJD', 'MOONDIST', 'MOONFRAC', 'MOONPHSE', 'MOON_ALT', 'MOON_AZ', 'MOON_DEC', 'MOON_RA', 'NBSIZE', 'NIGHT', 'NUMBRMS', 'NXOUT', 'NYOUT', 'OBJECT', 'OBSSTART', 'PROD_ID', 'PSFSHAPE', 'RCORE', 'READMODE', 'READTIME', 'ROOFSTAT', 'SATN_ADU', 'SEEING', 'SKYLEVEL', 'SKYNOISE', 'STDCRMS', 'SUNDIST', 'SUN_ALT', 'SUN_AZ', 'SUN_DEC', 'SUN_RA', 'TC3_3', 'TC3_6', 'TC6_3', 'TC6_6', 'TCRPX2', 'TCRPX5', 'TCRVL2', 'TCRVL5', 'TEL_ALT', 'TEL_AZ', 'TEL_DEC', 'TEL_HA', 'TEL_POSA', 'TEL_RA', 'THRESHOL', 'TIME-OBS', 'TV6_1', 'TV6_3', 'TV6_5', 'TV6_7', 'VI_MINUS', 'VI_PLUS', 'VSS_USEC', 'WCSPASS', 'WCS_ID', 'WXDEWPNT', 'WXHUMID', 'WXPRES', 'WXTEMP', 'WXWNDDIR', 'WXWNDSPD', 'XENCPOS0', 'XENCPOS1', 'YENCPOS0', 'YENCPOS1', 'TMID',
        'HJD',
        'FLUX',
        'FLUX_ERR',
        'FLAGS',
        'CCDX',
        'CCDY',
        'CENTDX_ERR',
        'CENTDX',
        'CENTDY_ERR',
        'CENTDY',
        'SKYBKG',
        'SYSREM_FLUX3',
        'BMAG', 'VMAG', 'RMAG', 'JMAG', 'HMAG', 'KMAG', 'MU_RA', 'MU_RA_ERR', 'MU_DEC', 'MU_DEC_ERR', 'DILUTION_V', 'DILUTION_R', 'MAG_MEAN', 'NUM_CANDS', 'NPTS_TOT', 'NPTS_USED', 'OBJ_FLAGS', 'SIGMA_XS', 'TEFF_VK', 'TEFF_JH', 'RSTAR_VK', 'RSTAR_JH', 'RPMJ', 'RPMJ_DIFF', 'GIANT_FLG', 'CAT_FLG',
        'RANK', 'FLAGS', 'PERIOD', 'WIDTH', 'DEPTH', 'EPOCH', 'DELTA_CHISQ', 'CHISQ', 'NPTS_TRANSIT', 'NUM_TRANSITS', 'NBOUND_IN_TRANS', 'AMP_ELLIPSE', 'SN_ELLIPSE', 'GAP_RATIO', 'SN_ANTI', 'SN_RED', 'SDE', 'MCMC_PERIOD', 'MCMC_EPOCH', 'MCMC_WIDTH', 'MCMC_DEPTH', 'MCMC_IMPACT', 'MCMC_RSTAR', 'MCMC_MSTAR', 'MCMC_RPLANET', 'MCMC_PRP', 'MCMC_PRS', 'MCMC_PRB', 'MCMC_CHISQ_CONS', 'MCMC_CHISQ_UNC', 'MCMC_DCHISQ_MR', 'MCMC_PERIOD_ERR', 'MCMC_EPOCH_ERR', 'MCMC_WIDTH_ERR', 'MCMC_DEPTH_ERR', 'MCMC_RPLANET_ERR', 'MCMC_RSTAR_ERR', 'MCMC_MSTAR_ERR', 'MCMC_CHSMIN', 'CLUMP_INDX', 'CAT_IDX', 'PG_IDX', 'LC_IDX',
        ]

quickkeys = [ 
        'OBJ_ID', 'RA', 'DEC',
        'ACQUMODE', 'ACTIONID', 
        'HJD',
        'FLUX',
        'SYSREM_FLUX3',
        'BMAG', 
        'RANK'
        ]

def waitbar(i, N, increment=None, extra='' ):
    if increment is None: increment = int(N/20.)
    if increment < 1: increment = 1
        
    if( (i % increment) == 0):
        sys.stdout.write( "\r"+"               [" + "=" * (i / increment) +  " " * ((N - i)/ increment) + "]" +  str( int(100. * i / N) ) + "%" )
#        sys.stdout.flush()
#        sleep(0.01)   
        
    if(i == N-1):
        i += 1
        sys.stdout.write( "\r"+"               [" + "=" * (i / increment) +  " " * ((N - i)/ increment) + "]" +  str( int(100. * i / N) ) + "%" )
        
    sys.stdout.write("\r" + "               ")
    sys.stdout.write("\r" + extra)
    sys.stdout.flush()



def compare_dic(dic1, dic2):
    for key in dic1.viewkeys() & dic2.viewkeys():
        if key not in dic1: print 'WARNING: Key', key, 'missing in dic1.'
        elif key not in dic2: print 'WARNING: Key', key, 'missing in dic1.'
        else:
            bool_mask = (dic1[key]==dic2[key])
            if isinstance( bool_mask, (bool,np.bool_) ): bool_mask = [bool_mask]
                
            if False in bool_mask:
                if not isinstance( dic1[key], np.ndarray ) and not isinstance( dic2[key], np.ndarray ):
                    if np.isnan( dic1[key] )==False and np.isnan( dic2[key] )==False:
                        print 'WARNING: Dictionaries do not match for key', key
                        print dic1
                        print dic2
                        print dic1[key]
                        print dic2[key]
                        print '-------------'                        
                else:
                    ind = np.where(dic1[key]!=dic2[key])
                    if False in np.isnan( dic1[key][ind] ) and False in np.isnan( dic2[key][ind] ):
                        print 'WARNING: Dictionaries do not match for key', key
                        print dic1
                        print dic2
                        print dic1[key][ind]
                        print dic2[key][ind]
                        print '-------------'
                

def test1(keys):
    print '\n'
    N = len(keys)
    for i,key in enumerate(keys):
        waitbar(i, N, extra=key)
    #    print key
        dic_astropy = ngtsio.get( 'NG0304-1115', 'CYCLE1706', [key], fitsreader='astropy', silent=True )
        dic_fitsio = ngtsio.get( 'NG0304-1115', 'CYCLE1706', [key], fitsreader='fitsio', silent=True )
        compare_dic(dic_astropy, dic_fitsio)
    print '\nTest 1 succesful.'



def test2(keys):
    j = 0
    for obj_row in [100, '100', [100,102], ['100','102']]:
        for time_hjd in [700, '700', [700,702], ['700','702']]:
            print '\nRunning Test 2.'+str(j)
            N = len(keys)
            for i,key in enumerate(keys):
                waitbar(i, N, extra=key)
#                print key
                dic_astropy = ngtsio.get( 'NG0304-1115', 'CYCLE1706', [key], obj_row=obj_row, time_hjd=time_hjd, fitsreader='astropy', silent=True )
                dic_fitsio = ngtsio.get( 'NG0304-1115', 'CYCLE1706', [key], obj_row=obj_row, time_hjd=time_hjd, fitsreader='fitsio', silent=True )
                compare_dic(dic_astropy, dic_fitsio)
            print '\nTest 2-'+str(j)+' succesful.'
            j += 1
    
    
    
def test3(keys):
    j = 0
    for obj_id in [46, '046', [46,11,2], ['046','11','2']]:
        for time_date in [20151115, '2015-11-15', '2015/11/15', [20151115,20151127,20170101], ['2015-11-15','2015-11-04','2017-01-01']]:
            print '\nRunning Test 3.'+str(j)+': obj_id='+str(obj_id)+', time_date='+str(time_date)
            N = len(keys)
            for i,key in enumerate(keys):
                waitbar(i, N, extra=key)
#                    print key
                dic_astropy = ngtsio.get( 'NG0304-1115', 'CYCLE1706', [key], obj_id=obj_id, time_date=time_date, fitsreader='astropy', silent=True )
                dic_fitsio = ngtsio.get( 'NG0304-1115', 'CYCLE1706', [key], obj_id=obj_id, time_date=time_date, fitsreader='fitsio', silent=True )
                compare_dic(dic_astropy, dic_fitsio)
            print '\nTest 3.'+str(j)+' succesful.'
            j += 1
    
    
    
def test4(keys):
    j = 0
    for time_actionid in [108583, '108583', [108583,109754], ['108583','109754']]:
        print '\nRunning Test 4.'+str(j)+': obj_id=bls, time_actionid='+str(time_actionid)
        N = len(keys)
        for i,key in enumerate(keys):
            waitbar(i, N, extra=key)
        #    print key
            dic_astropy = ngtsio.get( 'NG0304-1115', 'CYCLE1706', [key], obj_id='bls', time_actionid=time_actionid, fitsreader='astropy', silent=True )
            dic_fitsio = ngtsio.get( 'NG0304-1115', 'CYCLE1706', [key], obj_id='bls', time_actionid=time_actionid, fitsreader='fitsio', silent=True )
            compare_dic(dic_astropy, dic_fitsio)
        print '\nTest 4.'+str(j)+' succesful.'
        j += 1
    
    
    
 
def test(keys):   
    test1(keys)
    test2(keys)
    test3(keys)
    test4(keys)
 



def compare_fitsreader_speed():
    
    def test_pyfits_all():
        ngtsio.get('NG0304-1115', 'CYCLE1706', ['FLUX_MEAN','RA','DEC'], fitsreader='pyfits')
        
    def test_fitsio_all():
        ngtsio.get('NG0304-1115', 'CYCLE1706', ['FLUX_MEAN','RA','DEC'], fitsreader='fitsio')
        
    def test_pyfits():
        ngtsio.get('NG0304-1115', 'CYCLE1706', ['FLUX','CENTDX','CENTDY'], fitsreader='pyfits', obj_id=12118)
        
    def test_fitsio():
        ngtsio.get('NG0304-1115', 'CYCLE1706', ['FLUX','CENTDX','CENTDY'], fitsreader='fitsio', obj_id=12118)
        
        
    print 'pyfits', timeit.timeit(test_pyfits, number=5)
    print 'fitsio', timeit.timeit(test_fitsio, number=5)
    print 'pyfits (all)', timeit.timeit(test_pyfits_all, number=5)
    print 'fitsio (all)', timeit.timeit(test_fitsio_all, number=5)
        
        
        
    
if __name__ == '__main__':    
#    test(quickkeys)
    pass
