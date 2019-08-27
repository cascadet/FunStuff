###################################################
##          Code to apply a function to 
##          sub directories in parallel
##
##          The example below loops through dirs
##          with .tif files, pulls the year of the 
##          .tif file and adds it to a list, then 
##          writes out the as .csv
##        
##          Work in progress :-)
##
##          by Cascade Tuholske 2019-08-27
##
###################################################

# Dependencies
from glob import glob
from multiprocessing import Pool, Queue, Process
import time 
import os
import multiprocessing as mp
import pandas as pd

# Set path to dir to loop through sub dirs
 CHIRT_DIR = '/Users/cascade/Github/UrbanHeat/data/test_in/'
 DATA_OUT = '/Users/cascade/Github/UrbanHeat/data/test_out/' 

# Make dir list of sub dirs
dir_list= glob(CHIRT_DIR+'*/')
dir_list

# Function 
def test_mp(dir_nm):

    """ Loops through a dir with .tif files, isolates the year
    adds it to a list and then writes out the list

    Args: 
        dir_nm = dir name to start the process
    """
    
    # print current process
    print(mp.current_process())
    
    dir_year = dir_nm.split(CHIRT_DIR)[1].split('/')[0]
    fn_list = []
    for fn in os.listdir(dir_nm):
        
        # find all the tif files
        if fn.endswith('.tif'):
                # Get the date of each chirt file
                date = (fn.split('CHIRTSmax.')[1].split('.tif')[0])
                
                print(dir_year)
                print(date)
                
                fn_list.append(date)
    print(fn_list)
    
    # Save it out
    out_df = pd.DataFrame(fn_list)
    out_df.to_csv(DATA_OUT+dir_year+'.csv')
    print('DONE ! ! !')

# Start Clock
start = time.time()

# make a pool of CPUS, note with mp.cpu_count() will fire on all your machine's CPUs
pool = Pool(mp.cpu_count())

# Start Routine
pool.map_async(test_mp, dir_list)
pool.close()

# Clock 
end = time.time()
print(end-start)