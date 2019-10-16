# Code to pull files from an FTP and Open them in memory

# Dependencies
from rasterio
import os
from ftplib import FTP

#Open ftp connection to Climate Hazard's Group
ftp = FTP('ftp.chg.ucsb.edu', 'anonymous', 'cascade@ucsb.edu') # change email 
ftp.dir()

# Switch file paths
ftp.cwd('pub/org/chg/products/Tmax_monthly/CHIRTSmax.CDR/')

# Open write file to local disk 
from io import StringIO
r = StringIO()
type(r)

#ftp.retrbinary('RETR %s'.format('CHIRTSmax.1984.03.tif'), r.read)
ftp.retrbinary('RETR CHIRTSmax.1984.03.tif', open('CHIRTSmax.1984.03.tif', 'wb').write)

# Open .tif into memory
file = rasterio.open('CHIRTSmax.1984.03.tif')

# Remove file from local disk, but keep it in memory
os.remove("CHIRTSmax.1984.03.tif")
# Show that file is in memory
file 