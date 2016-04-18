# ngtsio
Wrapper for astropy and cfitsio readers for NGTS data files.

## Docs

    ngtsio.get(fieldname, keys, obj_id=None, obj_row=None, time_index=None, time_date=None, time_hjd=None, time_actionid=None, simplify=True, indexing='fits', fnames=[], ngts_version='TEST10', fitsreader='pyfits'):
Return a dictionary with all requested data for an NGTS field.


## Execution time comparison, pyfits vs cfitsio:

### all objects, all times
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], fitsreader='fitsio' )
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], fitsreader=‘pyfits’ )
    
    fitsio average time per run (out of 10 runs): 2.36079950333
    pyfits average time per run (out of 10 runs): 3.70509300232

### 1 object, all times
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], obj_row=1, fitsreader='fitsio’ )
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], obj_row=1, fitsreader='pyfits' )
    
    fitsio average time per run (out of 10 runs): 0.0335123062134
    pyfits average time per run (out of 10 runs): 0.368131780624

###  100 object, all times 
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], obj_row=range(1,3501,35), fitsreader='fitsio’ )
    dic = get( 'NG0304-1115', ['OBJ_ID','RA','DEC','HJD','FLUX'], obj_row=range(1,3501,35), fitsreader='pyfits' )
    
    fitsio average time per run (out of 10 runs): 0.123349809647
    pyfits average time per run (out of 10 runs): 0.462261390686
