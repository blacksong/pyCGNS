#  -------------------------------------------------------------------------
#  pyCGNS.VAL - Python package for CFD General Notation System - VALidater
#  See license.txt file in the root directory of this Python module source  
#  -------------------------------------------------------------------------
#
import CGNS.PAT.cgnslib as CGL
import CGNS.PAT.cgnsutils as CGU
import CGNS.PAT.cgnskeywords as CGK
import numpy as NPY

TESTS=[]

#  -------------------------------------------------------------------------
tag='indexarray'
diag=True
def makeCorrectTree(vertexsize,cellsize):
  T=CGL.newCGNSTree()
  b=CGL.newBase(T,'Base',3,3)
  s=NPY.array([[vertexsize,cellsize,0]],dtype='i',order='F')
  z=CGL.newZone(b,'Zone',s,CGK.Unstructured_s)
  g=CGL.newGridCoordinates(z,'GridCoordinates')
  d=CGL.newDataArray(g,CGK.CoordinateX_s,NPY.ones((vertexsize),dtype='d',order='F'))
  d=CGL.newDataArray(g,CGK.CoordinateY_s,NPY.ones((vertexsize),dtype='d',order='F'))
  d=CGL.newDataArray(g,CGK.CoordinateZ_s,NPY.ones((vertexsize),dtype='d',order='F'))
  quads=CGL.newElements(z,'QUADS',CGK.QUAD_4_s,NPY.ones((cellsize*4),dtype='i'),NPY.array([[1,cellsize]],'i',order='F'))
  zbc=CGL.newZoneBC(z)
  return (T,b,z,zbc)
vertexsize = 20
cellsize   = 7
(T,b,z,zbc)=makeCorrectTree(vertexsize,cellsize)
n=CGL.newBoundary(zbc,'BC',range(1,cellsize+1),btype=CGK.Null_s,family=None,pttype=CGK.PointList_s)
g=CGL.newGridLocation(n,value=CGK.CellCenter_s)
TESTS.append((tag,T,diag))

#  -------------------------------------------------------------------------
tag='indexarray bad parent'
diag=False
(T,b,z,zbc)=makeCorrectTree(vertexsize,cellsize)
n=CGL.newBoundary(zbc,'BC',range(1,cellsize+1),btype=CGK.Null_s,family=None,pttype=CGK.PointList_s)  
g=CGL.newGridLocation(n,value=CGK.CellCenter_s)
i = n[2][0]
z[2].append(CGU.copyNode(i,'PointList')) # unauthorized parent node
TESTS.append((tag,T,diag))

#  -------------------------------------------------------------------------
tag='indexarray bad name'
diag=False
(T,b,z,zbc)=makeCorrectTree(vertexsize,cellsize)
n=CGL.newBoundary(zbc,'BC',range(1,cellsize+1),btype=CGK.Null_s,family=None,pttype=CGK.PointList_s)  
g=CGL.newGridLocation(n,value=CGK.CellCenter_s)
i = n[2][0]
i[0] = 'ElementList' # unauthorized name
TESTS.append((tag,T,diag))

#  -------------------------------------------------------------------------
tag='indexarray bad data type'
diag=False
(T,b,z,zbc)=makeCorrectTree(vertexsize,cellsize)
n=CGL.newBoundary(zbc,'BC',range(1,cellsize+1),btype=CGK.Null_s,family=None,pttype=CGK.PointList_s)  
g=CGL.newGridLocation(n,value=CGK.CellCenter_s)
i = n[2][0]
i[1] = NPY.ones((5,0,0),dtype='d',order='F') # unauthorized data type
TESTS.append((tag,T,diag))

#  -------------------------------------------------------------------------
tag='indexarray bad child'
diag=False
(T,b,z,zbc)=makeCorrectTree(vertexsize,cellsize)
n=CGL.newBoundary(zbc,'BC',range(1,cellsize+1),btype=CGK.Null_s,family=None,pttype=CGK.PointList_s)  
g=CGL.newGridLocation(n,value=CGK.CellCenter_s)
i = n[2][0]
CGL.newDataArray(i,'{DataArray}') # unauthorized child
TESTS.append((tag,T,diag))

#  -------------------------------------------------------------------------
tag='indexarray element index out of range'
diag=False
(T,b,z,zbc)=makeCorrectTree(vertexsize,cellsize)
n=CGL.newBoundary(zbc,'BC',range(2,cellsize+2),btype=CGK.Null_s,family=None,pttype=CGK.PointList_s) # element index out of range
g=CGL.newGridLocation(n,value=CGK.CellCenter_s)
TESTS.append((tag,T,diag))