# CFD General Notation System - CGNS lib wrapper
# ONERA/DSNA/ELSA - poinot@onera.fr
# pyCGNS - $Rev: 47 $ $Date: 2008-01-24 12:00:02 +0100 (Thu, 24 Jan 2008) $
# See file COPYING in the root directory of this Python module source 
# tree for license information. 
#
import CGNS.cgnslib      as C
import CGNS.cgnserrors   as E
import CGNS.cgnskeywords as K
import numpy             as N
#
data=C.newBCProperty(None)
C.newDescriptor(data,'{Descriptor}')
C.newUserDefinedData(data,'{UserDefinedData}')
for n in data[2]:
  if (n[0] == K.Area_s):
    C.newDescriptor(n,'{Descriptor}')
    C.newDataArray(n,K.SurfaceArea_s,0)
    C.newDataArray(n,K.RegionName_s,"")
    C.newUserDefinedData(n,'{UserDefinedData}')
  if (n[0] == K.WallFunction_s):
    C.newDescriptor(n,'{Descriptor}')
    C.newUserDefinedData(n,'{UserDefinedData}')
#    #
status='9.6'
comment='Full SIDS with all optionals'
pattern=[data, status, comment]
#
