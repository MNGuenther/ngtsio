# ngtsio
Wrapper for astropy and cfitsio readers for NGTS data files 

Execution time comparison, pyfits vs cfitsio:

All objects, all times (/exposures):

    #pyfits
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], obj_row=None, time_date=None, fitsreader='pyfits' )    
    17.1447739601

    #fitsio
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], obj_row=None, time_date=None, fitsreader='fitsio' )  
    7.28385996819 s
