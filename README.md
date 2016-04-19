# ngtsio
Wrapper for astropy and cfitsio readers for NGTS data files.
This readme contains:

1) Parameters

2) Examples 

3) Execution time comparison

4) List of all valid keys

## Docs

    ngtsio.get(fieldname, keys, obj_id=None, obj_row=None, time_index=None, time_date=None, time_hjd=None, time_actionid=None, simplify=True, indexing='fits', fnames=[], ngts_version='TEST10', fitsreader='pyfits'):

Return a dictionary with all requested data for an NGTS field.

### 1) Parameters

#####fieldname (string):
name of the NGTS-field, e.g. 

    'NG0304-1115'
    
#####keys (string / array of strings):
which parameters shall be read out from the fits files, e.g. 

    'RA', 'DEC', ...
    'HJD', 'FLUX', 'SYSREM_FLUX3', ...
    'DEPTH', 'PERIOD', 'WIDTH', ...
See below for other valid requests.

#####obj_id, obj_row (int / string / textfile / array of int / array of string)
identifier of the objects to be read out. Only either obj_id or obj_row can be chosen as input, not both. obj_id reads out objects by their object IDs. obj_row reads the requested rows from the fits file. Examples: 

    obj_id = 46,    obj_id = '046',    obj_id = '00046',    obj_id = [46,57,1337],    obj_id = range(1,100),    obj_id = 'object_ids.txt'
    obj_row = 1,    obj_row = [1,2,3,1337],     obj_row = range(1,100),     obj_row = 'object_rows.txt'

#####time_index, time_date, time_hjd, time_actionid (int / string / textfile / array of int / array of string)
identifier of the exposures to be read out. Only either of these can be chosen as input, not more than one. time_index reads out the requested columns from the fits file, and hence allows to read out as little as one exposure. time_date reads all exposures per given calendar date(s). time_hjd reads all exposures per given HJD-date (only HJD values given as integers are accepted). time_actionid reads all exposures per given action ID. Examples:

    time_index = 1,    time_index = [1,2,3,1337],    time_index = range(1,100),    time_index = 'time_indices.txt'
    time_date = 20151104,    time_date = '20151104',    time_date = '2015-11-04',    time_date = '2015/11/04',    time_date = 'dates.txt'
    time_hjd = 674,    time_hjd = [674,675,680],    time_hjd = 'hjds.txt'
    time_actionid = 108583,    time_actionid = [108583,133749],    time_actionid = 'actionids.txt'      

#####indexing (string)
following which format are the obj_rows and time_indices given (standard is 'fits')? 

        'fits': indexing rows from 1
        'python': indexing rows from 0    

#####fitsreader (string) 
'pyfits' or 'astropy': use the astropy.io.fits module.
'fitsio' or 'cfitsio': use the fitsio module (standard)
fitsio seems to perform best, see below for performance tests.

#####simplify (boolean)
if True and only one object is requested, it simplifies the dictionary entries into 1D nd.arrays (otherwise they will be 2D nd.arrays with an empty dimension). Standard is True.

#####fnames (dictionary)
Leave blank if you want to run it on NGTSHEAD/NGTS01/etc. This allows to manually pass a dictionary of filenames, if different than the directory structure on NGTSHEAD. Must contain the following three keys:

        fnames['nights']
        fnames['sysrem']
        fnames['bls']

#####ngtsversion (string)
From which directory shall the files be read? (Standard is 'TEST10'. Irrelevant if filenames are given manually.)




### 2) Examples

    import matplotlib.pyplot as plt
    import ngtsio

#### a) Get and plot the lightcurve for one object

    dic = ngtsio.get( 'NG0304-1115', ['OBJ_ID','HJD','FLUX'], obj_id='00046' )
    plt.figure()
    plt.plot( dic['HJD'], dic['FLUX'], 'k.' )
    plt.title( dic['OBJ_ID'] )

#### b) Get and plot the mean locations of the first 100 listed objects on the CCD

    dic = ngtsio.get( 'NG0304-1115', ['CCD_X','CCD_Y'], obj_row=range(1,101) )
    plt.figure()
    plt.plot( dic['CCD_X'], dic['CCD_Y'], 'k.' )

#### c) Get the BLS results of some candidates (note that obj_id 1337 does not exist)

    dic = ngtsio.get( 'NG0304-1115', ['DEPTH','PERIOD','WIDTH'], obj_id=[46,49,54,1337] )
    print dic




### 3) Execution time comparison, pyfits vs cfitsio:

#####all objects, all times
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], fitsreader='fitsio' )
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], fitsreader=‘pyfits’ )
    
    fitsio average time per run (out of 10 runs): 2.36079950333
    pyfits average time per run (out of 10 runs): 3.70509300232

#####1 object, all times
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], obj_row=1, fitsreader='fitsio’ )
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], obj_row=1, fitsreader='pyfits' )
    
    fitsio average time per run (out of 10 runs): 0.0335123062134
    pyfits average time per run (out of 10 runs): 0.368131780624

#####100 object, all times 
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], obj_row=range(1,3501,35), fitsreader='fitsio’ )
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], obj_row=range(1,3501,35), fitsreader='pyfits' )
    
    fitsio average time per run (out of 10 runs): 0.123349809647
    pyfits average time per run (out of 10 runs): 0.462261390686
    



### 4) List of all valid keys
####a) Nightly Summary Fits file
#####From 'CATALOGUE' (per object):

    ['OBJ_ID', 'RA', 'DEC', 'REF_FLUX', 'CLASS', 'CCD_X', 'CCD_Y', 'FLUX_MEAN', 'FLUX_RMS', 'MAG_MEAN', 'MAG_RMS', 'NPTS', 'NPTS_CLIPPED']

#####From 'IMAGELIST' (per image):

    ['ACQUMODE', 'ACTIONID', 'ACTSTART', 'ADU_DEV', 'ADU_MAX', 'ADU_MEAN', 'ADU_MED', 'AFSTATUS', 'AGREFIMG', 'AGSTATUS', 'AG_APPLY', 'AG_CORRX', 'AG_CORRY', 'AG_DELTX', 'AG_DELTY', 'AG_ERRX', 'AG_ERRY', 'AIRMASS', 'BIASMEAN', 'BIASOVER', 'BIASPRE', 'BIAS_ID', 'BKG_MEAN', 'BKG_RMS', 'CAMERAID', 'CAMPAIGN', 'CCDTEMP', 'CCDTEMPX', 'CHSTEMP', 'CMD_DEC', 'CMD_DMS', 'CMD_HMS', 'CMD_RA', 'COOLSTAT', 'CROWDED', 'CTS_DEV', 'CTS_MAX', 'CTS_MEAN', 'CTS_MED', 'DARK_ID', 'DATE-OBS', 'DATE', 'DITHER', 'EXPOSURE', 'FCSR_ENC', 'FCSR_PHY', 'FCSR_TMP', 'FIELD', 'FILTFWHM', 'FLAT_ID', 'FLDNICK', 'GAIN', 'GAINFACT', 'HSS_MHZ', 'HTMEDXF', 'HTRMSXF', 'HTXFLAGD', 'HTXNFLAG', 'HTXRAD1', 'HTXSIG1', 'HTXTHTA1', 'HTXVAL1', 'IMAGE_ID', 'IMGCLASS', 'IMGTYPE', 'LST', 'MINPIX', 'MJD', 'MOONDIST', 'MOONFRAC', 'MOONPHSE', 'MOON_ALT', 'MOON_AZ', 'MOON_DEC', 'MOON_RA', 'NBSIZE', 'NIGHT', 'NUMBRMS', 'NXOUT', 'NYOUT', 'OBJECT', 'OBSSTART', 'PROD_ID', 'PSFSHAPE', 'RCORE', 'READMODE', 'READTIME', 'ROOFSTAT', 'SATN_ADU', 'SEEING', 'SKYLEVEL', 'SKYNOISE', 'STDCRMS', 'SUNDIST', 'SUN_ALT', 'SUN_AZ', 'SUN_DEC', 'SUN_RA', 'TC3_3', 'TC3_6', 'TC6_3', 'TC6_6', 'TCRPX2', 'TCRPX5', 'TCRVL2', 'TCRVL5', 'TEL_ALT', 'TEL_AZ', 'TEL_DEC', 'TEL_HA', 'TEL_POSA', 'TEL_RA', 'THRESHOL', 'TIME-OBS', 'TV6_1', 'TV6_3', 'TV6_5', 'TV6_7', 'VI_MINUS', 'VI_PLUS', 'VSS_USEC', 'WCSPASS', 'WCS_ID', 'WXDEWPNT', 'WXHUMID', 'WXPRES', 'WXTEMP', 'WXWNDDIR', 'WXWNDSPD', 'XENCPOS0', 'XENCPOS1', 'YENCPOS0', 'YENCPOS1', 'TMID']

##### From image data (per object and per image):

    HJD
    FLUX
    FLUX_ERR
    FLAGS
    CCDX
    CCDY
    CENTDX_ERR
    CENTDX
    CENTDY_ERR
    CENTDY
    SKYBKG


#### b) Sysrem Fits File

#####Sysrem flux data (per object and per image):

    SYSREM_FLUX3


####c) BLS Fits File

#####From 'CATALOGUE' (for all objects):

    ['OBJ_ID', 'BMAG', 'VMAG', 'RMAG', 'JMAG', 'HMAG', 'KMAG', 'MU_RA', 'MU_RA_ERR', 'MU_DEC', 'MU_DEC_ERR', 'DILUTION_V', 'DILUTION_R', 'MAG_MEAN', 'NUM_CANDS', 'NPTS_TOT', 'NPTS_USED', 'OBJ_FLAGS', 'SIGMA_XS', 'TEFF_VK', 'TEFF_JH', 'RSTAR_VK', 'RSTAR_JH', 'RPMJ', 'RPMJ_DIFF', 'GIANT_FLG', 'CAT_FLG']

#####From 'CANDIDATE' data (only for candidates):

    ['OBJ_ID', 'RANK', 'FLAGS', 'PERIOD', 'WIDTH', 'DEPTH', 'EPOCH', 'DELTA_CHISQ', 'CHISQ', 'NPTS_TRANSIT', 'NUM_TRANSITS', 'NBOUND_IN_TRANS', 'AMP_ELLIPSE', 'SN_ELLIPSE', 'GAP_RATIO', 'SN_ANTI', 'SN_RED', 'SDE', 'MCMC_PERIOD', 'MCMC_EPOCH', 'MCMC_WIDTH', 'MCMC_DEPTH', 'MCMC_IMPACT', 'MCMC_RSTAR', 'MCMC_MSTAR', 'MCMC_RPLANET', 'MCMC_PRP', 'MCMC_PRS', 'MCMC_PRB', 'MCMC_CHISQ_CONS', 'MCMC_CHISQ_UNC', 'MCMC_DCHISQ_MR', 'MCMC_PERIOD_ERR', 'MCMC_EPOCH_ERR', 'MCMC_WIDTH_ERR', 'MCMC_DEPTH_ERR', 'MCMC_RPLANET_ERR', 'MCMC_RSTAR_ERR', 'MCMC_MSTAR_ERR', 'MCMC_CHSMIN', 'CLUMP_INDX', 'CAT_IDX', 'PG_IDX', 'LC_IDX']

