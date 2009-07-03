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
data=C.newBCData(None,'{BCData}')
C.newDescriptor(data,'{Descriptor}')
C.newDataArray(data,'{DataLocal}')
C.newDataArray(data,'{DataGlobal}')
C.newDataClass(data)
C.newDimensionalUnits(data)
C.newUserDefinedData(data,'{UserDefinedData}')
#
status='9.5'
comment='Full SIDS with all optionals'
pattern=[data, status, comment]
#
