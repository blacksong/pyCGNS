#  -------------------------------------------------------------------------
#  pyCGNS.VAL - Python package for CFD General Notation System - NAVigater
#  See license.txt file in the root directory of this Python module source  
#  -------------------------------------------------------------------------
#  $Release$
#  -------------------------------------------------------------------------

import CGNS.VAL.grammars.SIDSbase
import CGNS.VAL.parse.messages as CGM
import CGNS.VAL.parse.findgrammar

def listuserkeys(trace):
    s=''
    dk=CGNS.VAL.parse.findgrammar.findAllUserGrammars(trace)
    for key in dk:
        s+='%-16s: %s\n'%(key,dk[key])
    return s

def getParser(trace,user):
    if (user is not None):
        mod=CGNS.VAL.parse.findgrammar.importUserGrammars(user)
        if (mod is None):
            parser=CGNS.VAL.grammars.SIDSbase.SIDSbase(None)
        else:
            parser=mod.CGNS_VAL_USER_Checks(None)
    else:
        parser=CGNS.VAL.grammars.SIDSbase.SIDSbase(None)
    return parser

def listdiags(trace,userlist):
    ld=[]
    for user in userlist:
        parser=getParser(trace,user)
        mlist=parser.listDiagnostics()
        ld+=mlist.keys()
    ld.sort()
    s=''
    for d in ld:
        s+="%s\n"%(str(mlist[d]))
    return s

def run(T,trace,userlist):
    diag=CGM.DiagnosticLog()
    for user in userlist:
        parser=getParser(trace,user)
        parser.checkTree(T,trace)
        diag.merge(parser.log)
    return diag

def showDiag(diag,idlist,bypath=True):
    ok=True
    if (bypath):
      for p in diag:
          if (not diag.hasOnlyKey(p,idlist)):
            print '\n%s\n%s'%('-'*75,p)
            for (s,sp) in diag.diagnosticsByPath(p):
                if ((diag.status(s)!=CGM.CHECK_GOOD)
                    and (diag.key(s) not in idlist)):
                    print diag.message(s)
                    if (diag.status(s)==CGM.CHECK_FAIL): ok=False
      print '\n%s\n'%('-'*75)
    else:
      for m in diag.allMessageKeys():
        if (m not in idlist):
          first=True
          ctxt=diag.noContextMessage(m)
          if (ctxt is not None): print '\n%s\n[%s] %s'%('-'*75,m,ctxt)
          else: print '\n%s\n[%s]'%('-'*75,m)
          for (d,dp) in diag.diagnosticsByMessage(m):
              if (diag.status(d)!=CGM.CHECK_GOOD):
                  if (ctxt is None):
                      if (not first): skip='\n'
                      else: skip=''
                      print '%s  %s\n  > %s'%(skip,dp,d[1])
                  else: print '  %s'%(dp)
                  first=False
                  if (diag.status(d)==CGM.CHECK_FAIL): ok=False
      print '\n%s'%('-'*75)
    if (ok): print '### CGNS/Python tree Compliant'
    else:    print '### CGNS/Python tree *NOT* Compliant'
    