# CFD General Notation System - CGNS lib wrapper
# ONERA/DSNA/ELSA - poinot@onera.fr
# pyCGNS - $Rev: 58 $ $Date: 2008-08-20 15:55:47 +0200 (Wed, 20 Aug 2008) $
# See file COPYING in the root directory of this Python module source 
# tree for license information. 
#
import CGNS.cgnslib      as C
import CGNS.cgnskeywords as K
import CGNS.cgnserrors   as E
import numpy             as N
#
#
data=C.newArbitraryGridMotion(None,'{ArbitraryGridMotion}')
C.newRind(data,N.array([0,0,0,0,1,1]))
C.newGridLocation(data)
C.newDataArray(data,K.GridVelocityX_s)
C.newDataArray(data,K.GridVelocityY_s)
C.newDataArray(data,K.GridVelocityZ_s)
C.newDataClass(data)
C.newDimensionalUnits(data)
C.newUserDefinedData(data,'{UserDefinedData}')
C.newDescriptor(data,'{Descriptor}')
#
status='11.3'
comment='Full SIDS with all optionals'
pattern=[data, status, comment]
#