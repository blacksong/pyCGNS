# cannot be used for CFD
import numpy
T=['CGNSTree',None,[
  ['CGNSLibraryVersion',numpy.array([3.200000047683716],dtype='f',order='C'),[],'CGNSLibraryVersion_t'],
  ['{Base#1}',numpy.array([3, 3],dtype='i',order='C'),[
    ['Interior',None,[
      ['FamilyBC',numpy.array(['B', 'C', 'F', 'a', 'r', 'f', 'i', 'e', 'l', 'd'],dtype='S',order='C'),[],'FamilyBC_t'],],'Family_t'],
    ['Exterior',None,[
      ['FamilyBC',numpy.array(['B', 'C', 'W', 'a', 'l', 'l'],dtype='S',order='C'),[],'FamilyBC_t'],],'Family_t'],
    ['{Zone-A}',numpy.array([[13, 12, 0], [61, 60, 0], [17, 16, 0]],dtype='l',order='F'),[
      ['ZoneType',numpy.array(['S', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'd'],dtype='S',order='C'),[],'ZoneType_t'],
      ['GridCoordinates',None,[
        ['CoordinateX',None,[],'DataArray_t'],
        ['CoordinateY',None,[],'DataArray_t'],
        ['CoordinateZ',None,[],'DataArray_t'],],'GridCoordinates_t'],
      ['ZoneBC',None,[
        ['{BC-2}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 13], [1, 1], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['I', 'n', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-1}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 13], [1, 61], [1, 1]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-4}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 13], [61, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-6}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 13], [1, 61], [17, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],],'ZoneBC_t'],
      ['ZoneGridConnectivity',None,[
        ['{CT-A-D}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'D', '}'],dtype='S',order='C'),[
          ['GridConnectivityType',numpy.array(['A', 'b', 'u', 't', 't', 'i', 'n', 'g'],dtype='S',order='C'),[],'GridConnectivityType_t'],
          ['ConnectivityKeyLocal',numpy.array(['A', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
          ['ConnectivityKeyDonor',numpy.array(['D', '_', 'A'],dtype='S',order='C'),[],'DataArray_t'],
          ['PointRange',numpy.array([[1, 1], [1, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['.Solver#Property',None,[
            ['globborder',numpy.array(['A', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
            ['globborderdonor',numpy.array(['D', '_', 'A'],dtype='S',order='C'),[],'DataArray_t'],
            ['jtype',numpy.array(['n', 'o', 'm', 'a', 't', 'c', 'h'],dtype='S',order='C'),[],'DataArray_t'],
            ['nomatch_special',numpy.array(['n', 'o', 'n', 'e'],dtype='S',order='C'),[],'DataArray_t'],
            ['type',numpy.array(['j', 'o', 'i', 'n'],dtype='S',order='C'),[],'DataArray_t'],],'UserDefinedData_t'],],'GridConnectivity_t'],
        ['{CT-A-B}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'B', '}'],dtype='S',order='C'),[
          ['Transform',numpy.array([1, 2, 3],dtype='i',order='C'),[],'"int[IndexDimension]"'],
          ['PointRange',numpy.array([[13, 13], [1, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['PointRangeDonor',numpy.array([[1, 1], [1, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],],'GridConnectivity1to1_t'],],'ZoneGridConnectivity_t'],
      ['FlowSolution#EndOfRun',None,[
        ['GridLocation',numpy.array(['C', 'e', 'l', 'l', 'C', 'e', 'n', 't', 'e', 'r'],dtype='S',order='C'),[],'GridLocation_t'],
        ['Density',None,[],'DataArray_t'],
        ['MomentumX',None,[],'DataArray_t'],
        ['MomentumY',None,[],'DataArray_t'],
        ['MomentumZ',None,[],'DataArray_t'],
        ['EnergyStagnationDensity',None,[],'DataArray_t'],],'FlowSolution_t'],],'Zone_t'],
    ['{Zone-B}',numpy.array([[31, 30, 0], [61, 60, 0], [17, 16, 0]],dtype='l',order='F'),[
      ['ZoneType',numpy.array(['S', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'd'],dtype='S',order='C'),[],'ZoneType_t'],
      ['GridCoordinates',None,[
        ['CoordinateX',None,[],'DataArray_t'],
        ['CoordinateY',None,[],'DataArray_t'],
        ['CoordinateZ',None,[],'DataArray_t'],],'GridCoordinates_t'],
      ['ZoneBC',None,[
        ['{BC-2}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 31], [1, 1], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['I', 'n', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-1}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 31], [1, 61], [1, 1]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-4}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 31], [61, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-6}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 31], [1, 61], [17, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],],'ZoneBC_t'],
      ['ZoneGridConnectivity',None,[
        ['{CT-B-A}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'A', '}'],dtype='S',order='C'),[
          ['Transform',numpy.array([1, 2, 3],dtype='i',order='C'),[],'"int[IndexDimension]"'],
          ['PointRange',numpy.array([[1, 1], [1, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['PointRangeDonor',numpy.array([[13, 13], [1, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],],'GridConnectivity1to1_t'],
        ['{CT-B-C}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'C', '}'],dtype='S',order='C'),[
          ['GridConnectivityType',numpy.array(['A', 'b', 'u', 't', 't', 'i', 'n', 'g'],dtype='S',order='C'),[],'GridConnectivityType_t'],
          ['ConnectivityKeyLocal',numpy.array(['B', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
          ['ConnectivityKeyDonor',numpy.array(['C', '_', 'B'],dtype='S',order='C'),[],'DataArray_t'],
          ['PointRange',numpy.array([[31, 31], [1, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['.Solver#Property',None,[
            ['globborder',numpy.array(['B', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
            ['globborderdonor',numpy.array(['C', '_', 'B'],dtype='S',order='C'),[],'DataArray_t'],
            ['jtype',numpy.array(['n', 'o', 'm', 'a', 't', 'c', 'h'],dtype='S',order='C'),[],'DataArray_t'],
            ['nomatch_special',numpy.array(['n', 'o', 'n', 'e'],dtype='S',order='C'),[],'DataArray_t'],
            ['type',numpy.array(['j', 'o', 'i', 'n'],dtype='S',order='C'),[],'DataArray_t'],],'UserDefinedData_t'],],'GridConnectivity_t'],],'ZoneGridConnectivity_t'],
      ['FlowSolution#EndOfRun',None,[
        ['GridLocation',numpy.array(['C', 'e', 'l', 'l', 'C', 'e', 'n', 't', 'e', 'r'],dtype='S',order='C'),[],'GridLocation_t'],
        ['Density',None,[],'DataArray_t'],
        ['MomentumX',None,[],'DataArray_t'],
        ['MomentumY',None,[],'DataArray_t'],
        ['MomentumZ',None,[],'DataArray_t'],
        ['EnergyStagnationDensity',None,[],'DataArray_t'],],'FlowSolution_t'],],'Zone_t'],
    ['{Zone-C1}',numpy.array([[27, 26, 0], [25, 24, 0], [17, 16, 0]],dtype='l',order='F'),[
      ['ZoneType',numpy.array(['S', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'd'],dtype='S',order='C'),[],'ZoneType_t'],
      ['GridCoordinates',None,[
        ['CoordinateX',None,[],'DataArray_t'],
        ['CoordinateY',None,[],'DataArray_t'],
        ['CoordinateZ',None,[],'DataArray_t'],],'GridCoordinates_t'],
      ['ZoneBC',None,[
        ['{BC-1}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 27], [1, 25], [1, 1]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-4}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 27], [25, 25], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-6}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 27], [1, 25], [17, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],],'ZoneBC_t'],
      ['ZoneGridConnectivity',None,[
        ['{CT-C1-C2}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'C', '2', '}'],dtype='S',order='C'),[
          ['Transform',numpy.array([1, 2, 3],dtype='i',order='C'),[],'"int[IndexDimension]"'],
          ['PointRange',numpy.array([[1, 27], [1, 1], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['PointRangeDonor',numpy.array([[1, 27], [37, 37], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],],'GridConnectivity1to1_t'],
        ['{CT-C1-B}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'B', '}'],dtype='S',order='C'),[
          ['GridConnectivityType',numpy.array(['A', 'b', 'u', 't', 't', 'i', 'n', 'g'],dtype='S',order='C'),[],'GridConnectivityType_t'],
          ['ConnectivityKeyLocal',numpy.array(['C', '_', 'B'],dtype='S',order='C'),[],'DataArray_t'],
          ['ConnectivityKeyDonor',numpy.array(['B', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
          ['PointRange',numpy.array([[1, 1], [1, 25], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['.Solver#Property',None,[
            ['globborder',numpy.array(['C', '_', 'B'],dtype='S',order='C'),[],'DataArray_t'],
            ['globborderdonor',numpy.array(['B', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
            ['jtype',numpy.array(['n', 'o', 'm', 'a', 't', 'c', 'h'],dtype='S',order='C'),[],'DataArray_t'],
            ['nomatch_special',numpy.array(['n', 'o', 'n', 'e'],dtype='S',order='C'),[],'DataArray_t'],
            ['type',numpy.array(['j', 'o', 'i', 'n'],dtype='S',order='C'),[],'DataArray_t'],],'UserDefinedData_t'],],'GridConnectivity_t'],
        ['{CT-C1-D}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'D', '}'],dtype='S',order='C'),[
          ['GridConnectivityType',numpy.array(['A', 'b', 'u', 't', 't', 'i', 'n', 'g'],dtype='S',order='C'),[],'GridConnectivityType_t'],
          ['ConnectivityKeyLocal',numpy.array(['C', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
          ['ConnectivityKeyDonor',numpy.array(['D', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
          ['PointRange',numpy.array([[27, 27], [1, 25], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['.Solver#Property',None,[
            ['globborder',numpy.array(['C', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
            ['globborderdonor',numpy.array(['D', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
            ['jtype',numpy.array(['n', 'o', 'm', 'a', 't', 'c', 'h'],dtype='S',order='C'),[],'DataArray_t'],
            ['nomatch_special',numpy.array(['n', 'o', 'n', 'e'],dtype='S',order='C'),[],'DataArray_t'],
            ['type',numpy.array(['j', 'o', 'i', 'n'],dtype='S',order='C'),[],'DataArray_t'],],'UserDefinedData_t'],],'GridConnectivity_t'],],'ZoneGridConnectivity_t'],
      ['FlowSolution#EndOfRun',None,[
        ['GridLocation',numpy.array(['C', 'e', 'l', 'l', 'C', 'e', 'n', 't', 'e', 'r'],dtype='S',order='C'),[],'GridLocation_t'],
        ['Density',None,[],'DataArray_t'],
        ['MomentumX',None,[],'DataArray_t'],
        ['MomentumY',None,[],'DataArray_t'],
        ['MomentumZ',None,[],'DataArray_t'],
        ['EnergyStagnationDensity',None,[],'DataArray_t'],],'FlowSolution_t'],],'Zone_t'],
    ['{Zone-C2}',numpy.array([[27, 26, 0], [37, 36, 0], [17, 16, 0]],dtype='l',order='F'),[
      ['ZoneType',numpy.array(['S', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'd'],dtype='S',order='C'),[],'ZoneType_t'],
      ['GridCoordinates',None,[
        ['CoordinateX',None,[],'DataArray_t'],
        ['CoordinateY',None,[],'DataArray_t'],
        ['CoordinateZ',None,[],'DataArray_t'],],'GridCoordinates_t'],
      ['ZoneBC',None,[
        ['{BC-2}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 27], [1, 1], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['I', 'n', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-1}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 27], [1, 37], [1, 1]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-6}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 27], [1, 37], [17, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],],'ZoneBC_t'],
      ['ZoneGridConnectivity',None,[
        ['{CT-C2-B}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'B', '}'],dtype='S',order='C'),[
          ['GridConnectivityType',numpy.array(['A', 'b', 'u', 't', 't', 'i', 'n', 'g'],dtype='S',order='C'),[],'GridConnectivityType_t'],
          ['ConnectivityKeyLocal',numpy.array(['C', '_', 'B'],dtype='S',order='C'),[],'DataArray_t'],
          ['ConnectivityKeyDonor',numpy.array(['B', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
          ['PointRange',numpy.array([[1, 1], [1, 37], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['.Solver#Property',None,[
            ['globborder',numpy.array(['C', '_', 'B'],dtype='S',order='C'),[],'DataArray_t'],
            ['globborderdonor',numpy.array(['B', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
            ['jtype',numpy.array(['n', 'o', 'm', 'a', 't', 'c', 'h'],dtype='S',order='C'),[],'DataArray_t'],
            ['nomatch_special',numpy.array(['n', 'o', 'n', 'e'],dtype='S',order='C'),[],'DataArray_t'],
            ['type',numpy.array(['j', 'o', 'i', 'n'],dtype='S',order='C'),[],'DataArray_t'],],'UserDefinedData_t'],],'GridConnectivity_t'],
        ['{CT-C2-D}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'D', '}'],dtype='S',order='C'),[
          ['GridConnectivityType',numpy.array(['A', 'b', 'u', 't', 't', 'i', 'n', 'g'],dtype='S',order='C'),[],'GridConnectivityType_t'],
          ['ConnectivityKeyLocal',numpy.array(['C', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
          ['ConnectivityKeyDonor',numpy.array(['D', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
          ['PointRange',numpy.array([[27, 27], [1, 37], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['.Solver#Property',None,[
            ['globborder',numpy.array(['C', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
            ['globborderdonor',numpy.array(['D', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
            ['jtype',numpy.array(['n', 'o', 'm', 'a', 't', 'c', 'h'],dtype='S',order='C'),[],'DataArray_t'],
            ['nomatch_special',numpy.array(['n', 'o', 'n', 'e'],dtype='S',order='C'),[],'DataArray_t'],
            ['type',numpy.array(['j', 'o', 'i', 'n'],dtype='S',order='C'),[],'DataArray_t'],],'UserDefinedData_t'],],'GridConnectivity_t'],
        ['{CT-C2-C1}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'C', '1', '}'],dtype='S',order='C'),[
          ['Transform',numpy.array([1, 2, 3],dtype='i',order='C'),[],'"int[IndexDimension]"'],
          ['PointRange',numpy.array([[1, 27], [37, 37], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['PointRangeDonor',numpy.array([[1, 27], [1, 1], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],],'GridConnectivity1to1_t'],],'ZoneGridConnectivity_t'],
      ['FlowSolution#EndOfRun',None,[
        ['GridLocation',numpy.array(['C', 'e', 'l', 'l', 'C', 'e', 'n', 't', 'e', 'r'],dtype='S',order='C'),[],'GridLocation_t'],
        ['Density',None,[],'DataArray_t'],
        ['MomentumX',None,[],'DataArray_t'],
        ['MomentumY',None,[],'DataArray_t'],
        ['MomentumZ',None,[],'DataArray_t'],
        ['EnergyStagnationDensity',None,[],'DataArray_t'],],'FlowSolution_t'],],'Zone_t'],
    ['{Zone-D1}',numpy.array([[41, 40, 0], [61, 60, 0], [17, 16, 0]],dtype='l',order='F'),[
      ['ZoneType',numpy.array(['S', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'd'],dtype='S',order='C'),[],'ZoneType_t'],
      ['GridCoordinates',None,[
        ['CoordinateX',None,[],'DataArray_t'],
        ['CoordinateY',None,[],'DataArray_t'],
        ['CoordinateZ',None,[],'DataArray_t'],],'GridCoordinates_t'],
      ['ZoneBC',None,[
        ['{BC-2}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 41], [1, 1], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['I', 'n', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-4}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 41], [61, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-6}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 41], [1, 61], [17, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],],'ZoneBC_t'],
      ['ZoneGridConnectivity',None,[
        ['{CT-D1-C}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'C', '}'],dtype='S',order='C'),[
          ['GridConnectivityType',numpy.array(['A', 'b', 'u', 't', 't', 'i', 'n', 'g'],dtype='S',order='C'),[],'GridConnectivityType_t'],
          ['ConnectivityKeyLocal',numpy.array(['D', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
          ['ConnectivityKeyDonor',numpy.array(['C', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
          ['PointRange',numpy.array([[1, 1], [1, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['.Solver#Property',None,[
            ['globborder',numpy.array(['D', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
            ['globborderdonor',numpy.array(['C', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
            ['jtype',numpy.array(['n', 'o', 'm', 'a', 't', 'c', 'h'],dtype='S',order='C'),[],'DataArray_t'],
            ['nomatch_special',numpy.array(['n', 'o', 'n', 'e'],dtype='S',order='C'),[],'DataArray_t'],
            ['type',numpy.array(['j', 'o', 'i', 'n'],dtype='S',order='C'),[],'DataArray_t'],],'UserDefinedData_t'],],'GridConnectivity_t'],
        ['{CT-D1-A}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'A', '}'],dtype='S',order='C'),[
          ['GridConnectivityType',numpy.array(['A', 'b', 'u', 't', 't', 'i', 'n', 'g'],dtype='S',order='C'),[],'GridConnectivityType_t'],
          ['ConnectivityKeyLocal',numpy.array(['D', '_', 'A'],dtype='S',order='C'),[],'DataArray_t'],
          ['ConnectivityKeyDonor',numpy.array(['A', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
          ['PointRange',numpy.array([[41, 41], [1, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['.Solver#Property',None,[
            ['globborder',numpy.array(['D', '_', 'A'],dtype='S',order='C'),[],'DataArray_t'],
            ['globborderdonor',numpy.array(['A', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
            ['jtype',numpy.array(['n', 'o', 'm', 'a', 't', 'c', 'h'],dtype='S',order='C'),[],'DataArray_t'],
            ['nomatch_special',numpy.array(['n', 'o', 'n', 'e'],dtype='S',order='C'),[],'DataArray_t'],
            ['type',numpy.array(['j', 'o', 'i', 'n'],dtype='S',order='C'),[],'DataArray_t'],],'UserDefinedData_t'],],'GridConnectivity_t'],
        ['{CT-D1-D2}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'D', '2', '}'],dtype='S',order='C'),[
          ['Transform',numpy.array([1, 2, 3],dtype='i',order='C'),[],'"int[IndexDimension]"'],
          ['PointRange',numpy.array([[1, 41], [1, 61], [1, 1]],dtype='i',order='F'),[],'IndexRange_t'],
          ['PointRangeDonor',numpy.array([[1, 41], [1, 61], [17, 17]],dtype='i',order='F'),[],'IndexRange_t'],],'GridConnectivity1to1_t'],],'ZoneGridConnectivity_t'],
      ['FlowSolution#EndOfRun',None,[
        ['GridLocation',numpy.array(['C', 'e', 'l', 'l', 'C', 'e', 'n', 't', 'e', 'r'],dtype='S',order='C'),[],'GridLocation_t'],
        ['Density',None,[],'DataArray_t'],
        ['MomentumX',None,[],'DataArray_t'],
        ['MomentumY',None,[],'DataArray_t'],
        ['MomentumZ',None,[],'DataArray_t'],
        ['EnergyStagnationDensity',None,[],'DataArray_t'],],'FlowSolution_t'],],'Zone_t'],
    ['{Zone-D2}',numpy.array([[41, 40, 0], [61, 60, 0], [17, 16, 0]],dtype='l',order='F'),[
      ['ZoneType',numpy.array(['S', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'd'],dtype='S',order='C'),[],'ZoneType_t'],
      ['GridCoordinates',None,[
        ['CoordinateX',None,[],'DataArray_t'],
        ['CoordinateY',None,[],'DataArray_t'],
        ['CoordinateZ',None,[],'DataArray_t'],],'GridCoordinates_t'],
      ['ZoneBC',None,[
        ['{BC-2}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 41], [1, 1], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['I', 'n', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-1}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 41], [1, 61], [1, 1]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],
        ['{BC-4}',numpy.array(['F', 'a', 'm', 'i', 'l', 'y', 'S', 'p', 'e', 'c', 'i', 'f', 'i', 'e', 'd'],dtype='S',order='C'),[
          ['PointRange',numpy.array([[1, 41], [61, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['FamilyName',numpy.array(['E', 'x', 't', 'e', 'r', 'i', 'o', 'r'],dtype='S',order='C'),[],'FamilyName_t'],],'BC_t'],],'ZoneBC_t'],
      ['ZoneGridConnectivity',None,[
        ['{CT-D2-C}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'C', '}'],dtype='S',order='C'),[
          ['GridConnectivityType',numpy.array(['A', 'b', 'u', 't', 't', 'i', 'n', 'g'],dtype='S',order='C'),[],'GridConnectivityType_t'],
          ['ConnectivityKeyLocal',numpy.array(['D', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
          ['ConnectivityKeyDonor',numpy.array(['C', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
          ['PointRange',numpy.array([[1, 1], [1, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['.Solver#Property',None,[
            ['globborder',numpy.array(['D', '_', 'C'],dtype='S',order='C'),[],'DataArray_t'],
            ['globborderdonor',numpy.array(['C', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
            ['jtype',numpy.array(['n', 'o', 'm', 'a', 't', 'c', 'h'],dtype='S',order='C'),[],'DataArray_t'],
            ['nomatch_special',numpy.array(['n', 'o', 'n', 'e'],dtype='S',order='C'),[],'DataArray_t'],
            ['type',numpy.array(['j', 'o', 'i', 'n'],dtype='S',order='C'),[],'DataArray_t'],],'UserDefinedData_t'],],'GridConnectivity_t'],
        ['{CT-D2-D1}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'D', '1', '}'],dtype='S',order='C'),[
          ['Transform',numpy.array([1, 2, 3],dtype='i',order='C'),[],'"int[IndexDimension]"'],
          ['PointRange',numpy.array([[1, 41], [1, 61], [17, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['PointRangeDonor',numpy.array([[1, 41], [1, 61], [1, 1]],dtype='i',order='F'),[],'IndexRange_t'],],'GridConnectivity1to1_t'],
        ['{CT-D2-A}',numpy.array(['{', 'Z', 'o', 'n', 'e', '-', 'A', '}'],dtype='S',order='C'),[
          ['GridConnectivityType',numpy.array(['A', 'b', 'u', 't', 't', 'i', 'n', 'g'],dtype='S',order='C'),[],'GridConnectivityType_t'],
          ['ConnectivityKeyLocal',numpy.array(['D', '_', 'A'],dtype='S',order='C'),[],'DataArray_t'],
          ['ConnectivityKeyDonor',numpy.array(['A', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
          ['PointRange',numpy.array([[41, 41], [1, 61], [1, 17]],dtype='i',order='F'),[],'IndexRange_t'],
          ['.Solver#Property',None,[
            ['globborder',numpy.array(['D', '_', 'A'],dtype='S',order='C'),[],'DataArray_t'],
            ['globborderdonor',numpy.array(['A', '_', 'D'],dtype='S',order='C'),[],'DataArray_t'],
            ['jtype',numpy.array(['n', 'o', 'm', 'a', 't', 'c', 'h'],dtype='S',order='C'),[],'DataArray_t'],
            ['nomatch_special',numpy.array(['n', 'o', 'n', 'e'],dtype='S',order='C'),[],'DataArray_t'],
            ['type',numpy.array(['j', 'o', 'i', 'n'],dtype='S',order='C'),[],'DataArray_t'],],'UserDefinedData_t'],],'GridConnectivity_t'],],'ZoneGridConnectivity_t'],
      ['FlowSolution#EndOfRun',None,[
        ['GridLocation',numpy.array(['C', 'e', 'l', 'l', 'C', 'e', 'n', 't', 'e', 'r'],dtype='S',order='C'),[],'GridLocation_t'],
        ['Density',None,[],'DataArray_t'],
        ['MomentumX',None,[],'DataArray_t'],
        ['MomentumY',None,[],'DataArray_t'],
        ['MomentumZ',None,[],'DataArray_t'],
        ['EnergyStagnationDensity',None,[],'DataArray_t'],],'FlowSolution_t'],],'Zone_t'],
    ['ReferenceState',None,[
      ['ReferenceStateDescription',numpy.array(['G', 'l', 'o', 'b', 'a', 'l', ' ', 'r', 'e', 'f', 'e', 'r', 'e', 'n', 'c', 'e', ' ', 's', 't', 'a', 't', 'e'],dtype='S',order='C'),[],'Descriptor_t'],
      ['AngleofAttack',numpy.array([7.0],dtype='d',order='C'),[],'DataArray_t'],
      ['BetaAngle',numpy.array([0.0],dtype='d',order='C'),[],'DataArray_t'],
      ['Coef_Area',numpy.array([0.25],dtype='d',order='C'),[],'DataArray_t'],
      ['Coef_PressureDynamic',numpy.array([2837.15315566],dtype='d',order='C'),[],'DataArray_t'],
      ['Density',numpy.array([1.22524863848],dtype='d',order='C'),[],'DataArray_t'],
      ['EnergyStagnationDensity',numpy.array([256154.399197],dtype='d',order='C'),[],'DataArray_t'],
      ['LengthReference',numpy.array([0.5],dtype='d',order='C'),[],'DataArray_t'],
      ['Mach',numpy.array([0.2],dtype='d',order='C'),[],'DataArray_t'],
      ['MomentumX',numpy.array([82.7597580354],dtype='d',order='C'),[],'DataArray_t'],
      ['MomentumY',numpy.array([0.0],dtype='d',order='C'),[],'DataArray_t'],
      ['MomentumZ',numpy.array([10.1616205508],dtype='d',order='C'),[],'DataArray_t'],
      ['Pressure',numpy.array([101326.898416],dtype='d',order='C'),[],'DataArray_t'],
      ['PressureStagnation',numpy.array([104192.536703],dtype='d',order='C'),[],'DataArray_t'],
      ['Reynolds',numpy.array([2330000.0],dtype='d',order='C'),[],'DataArray_t'],
      ['Temperature',numpy.array([288.15],dtype='d',order='C'),[],'DataArray_t'],
      ['TemperatureStagnation',numpy.array([290.4552],dtype='d',order='C'),[],'DataArray_t'],
      ['TurbulentSANuTilde',numpy.array([1.46035471482e-08],dtype='d',order='C'),[],'DataArray_t'],
      ['VelocityMagnitude',numpy.array([68.0525297105],dtype='d',order='C'),[],'DataArray_t'],],'ReferenceState_t'],
    ['.Solver#Compute',None,[
      ['artviscosity',numpy.array(['d', 'i', 's', 's', 'c', 'a'],dtype='S',order='C'),[],'DataArray_t'],
      ['avcoef_k2',numpy.array([1.0],dtype='d',order='C'),[],'DataArray_t'],
      ['avcoef_k4',numpy.array([0.032],dtype='d',order='C'),[],'DataArray_t'],
      ['avcoef_sigma',numpy.array([1.0],dtype='d',order='C'),[],'DataArray_t'],
      ['cfl',numpy.array([1.0],dtype='d',order='C'),[],'DataArray_t'],
      ['fluid',numpy.array(['I', 'd', 'e', 'a', 'l'],dtype='S',order='C'),[],'DataArray_t'],
      ['flux',numpy.array(['j', 'a', 'm', 'e', 's', 'o', 'n'],dtype='S',order='C'),[],'DataArray_t'],
      ['niter',numpy.array([1000],dtype='i',order='C'),[],'DataArray_t'],
      ['ode',numpy.array(['r', 'k', '4'],dtype='S',order='C'),[],'DataArray_t'],
      ['phymod',numpy.array(['N', 'S', 'T', 'u', 'r', 'b', 'u', 'l', 'e', 'n', 't'],dtype='S',order='C'),[],'DataArray_t'],
      ['t_cutvar1',numpy.array([1.78929762604e-08],dtype='d',order='C'),[],'DataArray_t'],
      ['t_harten',numpy.array([1e-24],dtype='d',order='C'),[],'DataArray_t'],
      ['time_algo',numpy.array(['s', 't', 'e', 'a', 'd', 'y'],dtype='S',order='C'),[],'DataArray_t'],
      ['turbmod',numpy.array([10],dtype='i',order='C'),[],'DataArray_t'],
      ['visclaw',numpy.array(['S', 'u', 't', 'h', 'e', 'r', 'l', 'a', 'n', 'd'],dtype='S',order='C'),[],'DataArray_t'],
      ['walldistcompute',numpy.array(['m', 'i', 'n', 'i', 'i', 'n', 't', 'e', 'r', 'f', '_', 'o', 'r', 't', 'h', 'o'],dtype='S',order='C'),[],'DataArray_t'],],'UserDefinedData_t'],],'CGNSBase_t'],],'CGNSTree_t']
