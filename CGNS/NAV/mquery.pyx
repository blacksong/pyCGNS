#  -------------------------------------------------------------------------
#  pyCGNS - Python package for CFD General Notation System - 
#  See license.txt file in the root directory of this Python module source  
#  -------------------------------------------------------------------------
# 
import sys
import numpy

from PySide.QtCore    import *
from PySide.QtGui     import *

from CGNS.NAV.moption import Q7OptionContext as OCTXT
import CGNS.NAV.moption as OCST

import CGNS.PAT.cgnsutils as CGU
import CGNS.PAT.cgnskeywords as CGK
import CGNS.PAT.cgnslib as CGL

SCRIPT_PATTERN="""#!/usr/bin/env python
#  -------------------------------------------------------------------------
#  pyCGNS.NAV - Python package for CFD General Notation System - NAVigater
#  See license.txt file in the root directory of this Python module source  
#  -------------------------------------------------------------------------
#  CGNS.NAV - GENERATED FILE - %(Q_VAR_DATE)s
#  query: %(Q_VAR_QUERYNAME)s
# -----------------------------------------------------------------
import CGNS.MAP as CGM

FILE='%(Q_VAR_TREE_FILE)s'
SCRIPT=\"\"\"%(Q_VAR_QUERY_SCRIPT)s\"\"\"
ARGS=\"\"\"%(Q_VAR_QUERY_ARGS)s\"\"\"
SELECTED=\"\"\"%(Q_VAR_SELECTED)s\"\"\"

# -----------------------------------------------------------------
SCRIPT_PRE=\"\"\"%(Q_VAR_SCRIPT_PRE)s\"\"\"
SCRIPT_POST=\"\"\"%(Q_VAR_SCRIPT_POST)s\"\"\"
# -----------------------------------------------------------------
def evalScript(node,parent,tree,links,skips,path,val,args,selected):
    l=locals()
    l['%(Q_VAR_RESULT_LIST)s']=[False]
    l['%(Q_VAR_PARENT)s']=parent
    l['%(Q_VAR_NAME)s']=node[0]
    l['%(Q_VAR_VALUE)s']=node[1]
    l['%(Q_VAR_CGNSTYPE)s']=node[3]
    l['%(Q_VAR_CHILDREN)s']=node[2]
    l['%(Q_VAR_TREE)s']=tree
    l['%(Q_VAR_LINKS)s']=links
    l['%(Q_VAR_SKIPS)s']=skips
    l['%(Q_VAR_SELECTED)s']=selected
    l['%(Q_VAR_PATH)s']=path
    if (args is None): args=()
    l['%(Q_VAR_USER)s']=args
    l['%(Q_VAR_NODE)s']=node
    pre=SCRIPT_PRE+val+SCRIPT_POST
    try:
      eval(compile(pre,'<string>','exec'),globals(),l)
    except Exception:
      l[OCST.Q_VAR_RESULT_LIST][0]=False
    RESULT=l['%(Q_VAR_RESULT_LIST)s'][0]
    return RESULT
# -----------------------------------------------------------------
def parseAndSelect(tree,node,parent,links,skips,path,script,args,selected,
                   result):
    path=path+'/'+node[0]
    Q=evalScript(node,parent,tree,links,skips,path,script,args,selected)
    R=[]
    if (Q):
        if (result):
            R=[Q]
        else:
            R=[path]
    for C in node[2]:
        R+=parseAndSelect(tree,C,node,links,skips,path,script,args,selected,
                          result)
    return R

# -----------------------------------------------------------------
def run(tree,links,skips,mode,args,script,selected):
    v=None
    try:
        if (args): v=eval(args)
        if ((v is not None) and (type(v)!=tuple)): v=(v,)
    except NameError:
        v=(str(args),)
    except:
        pass
    _args=v
    result=parseAndSelect(tree,tree,[None,None,[],None],links,skip,'',
                          script,_args,selected,mode)
    return result
# -----------------------------------------------------------------
(t,l,p)=CGM.load(FILE)
print run(t,l,p,True,ARGS,SCRIPT,SELECTED)

# -----------------------------------------------------------------
"""

# -----------------------------------------------------------------
def sameVal(n,v):
    if (n is None):
        if (v is None): return True
        return False
    if (n.dtype.char in ['S','c']): return (n.tostring() == v)
    if (n.dtype.char in ['d','f','i','l']): return (n.flat[0] == v)
    if (n==v): return True
    return False
# -----------------------------------------------------------------
def sameValType(n,v):
    if (type(n)!=numpy.ndarray): return False
    if (n.dtype.char==v): return True
    return False
# -----------------------------------------------------------------
def evalScript(node,parent,tree,links,skips,path,val,args,selected):
    l=locals()
    l[OCST.Q_VAR_RESULT_LIST]=[False]
    l[OCST.Q_VAR_PARENT]=parent
    l[OCST.Q_VAR_NAME]=node[0]
    l[OCST.Q_VAR_VALUE]=node[1]
    l[OCST.Q_VAR_CGNSTYPE]=node[3]
    l[OCST.Q_VAR_CHILDREN]=node[2]
    l[OCST.Q_VAR_TREE]=tree
    l[OCST.Q_VAR_LINKS]=links
    l[OCST.Q_VAR_SKIPS]=skips
    l[OCST.Q_VAR_PATH]=path
    l[OCST.Q_VAR_SELECTED]=selected
    if (args is None): args=()
    l[OCST.Q_VAR_USER]=args
    l[OCST.Q_VAR_NODE]=node
    pre=OCST.Q_SCRIPT_PRE+val+OCST.Q_SCRIPT_POST
    try:
      eval(compile(pre,'<string>','exec'),globals(),l)
    except Exception:
      l[OCST.Q_VAR_RESULT_LIST][0]=False
    RESULT=l[OCST.Q_VAR_RESULT_LIST][0]
    return RESULT
# -----------------------------------------------------------------
def parseAndSelect(tree,node,parent,links,skips,path,script,args,selected,
                   result):
    path=path+'/'+node[0]
    Q=evalScript(node,parent,tree,links,skips,path,script,args,selected)
    R=[]
    if (Q):
        if (result):
            R=[Q]
        else:
            R=[path]
    for C in node[2]:
        R+=parseAndSelect(tree,C,node,links,skips,path,script,args,selected,
                          result)
    return R

# -----------------------------------------------------------------
class Q7QueryEntry(object):
    def __init__(self,name,group=None,script='',doc='',update=False):
        self._name=name
        self._group=group
        self._script=script
        self._doc=doc
        self._update=update
    @property
    def name(self):
        return self._name
    @property
    def group(self):
        return self._group
    @property
    def doc(self):
        return self._doc
    @property
    def script(self):
        return self._script
    def requireTreeUpdate(self):
        return self._update
    def setRequireTreeUpdate(self,value):
        self._update=value
    def setScript(self,value):
        self._script=value
    def setDoc(self,value):
        self._doc=value
    def __str__(self):
        s='("%s","%s","%s","""%s""",%s)'%\
        (self.name,self.group,self._script,self._doc,self._update)
        return s
    def run(self,tree,links,skips,mode,args,selected=[]):
        v=None
        try:
            if (args): v=eval(args)
            if ((v is not None) and (type(v)!=tuple)): v=(v,)
        except NameError,e:
            v=(str(args),)
        except Exception,e:
            print e
        self._args=v
        result=parseAndSelect(tree,tree,[None,None,[],None],links,skips,'',
                              self._script,self._args,selected,mode)
        print result
        return result
    def getFullScript(self,filename,text,args):
        datadict={}
        datadict['Q_VAR_DATE']='00/00/00'
        datadict['Q_VAR_QUERYNAME']='%s/%s'%(self._group,self._name)
        datadict['Q_VAR_SCRIPT_PRE']=OCST.Q_SCRIPT_PRE
        datadict['Q_VAR_SCRIPT_POST']=OCST.Q_SCRIPT_POST
        datadict['Q_VAR_RESULT_LIST']=OCST.Q_VAR_RESULT_LIST
        datadict['Q_VAR_PARENT']=OCST.Q_VAR_PARENT
        datadict['Q_VAR_NAME']=OCST.Q_VAR_NAME
        datadict['Q_VAR_VALUE']=OCST.Q_VAR_VALUE
        datadict['Q_VAR_CGNSTYPE']=OCST.Q_VAR_CGNSTYPE
        datadict['Q_VAR_CHILDREN']=OCST.Q_VAR_CHILDREN
        datadict['Q_VAR_TREE']=OCST.Q_VAR_TREE
        datadict['Q_VAR_PATH']=OCST.Q_VAR_PATH
        datadict['Q_VAR_LINKS']=OCST.Q_VAR_LINKS
        datadict['Q_VAR_SKIPS']=OCST.Q_VAR_SKIPS
        datadict['Q_VAR_USER']=OCST.Q_VAR_USER
        datadict['Q_VAR_NODE']=OCST.Q_VAR_NODE
        datadict['Q_VAR_SELECTED']=OCST.Q_VAR_SELECTED
        datadict['Q_VAR_QUERY_SCRIPT']=text
        datadict['Q_VAR_QUERY_ARGS']=args
        datadict['Q_VAR_TREE_FILE']=filename
        script=SCRIPT_PATTERN%datadict
        return script
    
# -----------------------------------------------------------------