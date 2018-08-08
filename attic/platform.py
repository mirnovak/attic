import os
import subprocess
import io
import sys


if sys.platform.startswith('linux'):
    from attic.platform_linux import acl_get, acl_set, API_VERSION
elif sys.platform.startswith('freebsd'):
    from attic.platform_freebsd import acl_get, acl_set, API_VERSION
elif sys.platform == 'darwin':
    from attic.platform_darwin import acl_get, acl_set, API_VERSION
elif platform.startswith('CYGWIN'):
    API_VERSION = 2

    def acl_get(path, item, st, numeric_owner=False):
        return
        #try:
            ## Using non-numeric names, i.e., group names, has caused problems.
            ## Hence the -n option
            #ACL_text = subprocess.check_output(['getfacl.exe', '-n', path])
            #item[b'acl_access'] = ACL_text
        #except:
            #pass

    def acl_set(path, item, numeric_owner=False):
        return
        #try:
            #ACL_Access = item[b'acl_access']
        #except:
            #return 
        
        #buf = io.StringIO(ACL_Access.decode('utf-8'))

        #for line in buf:
            #if len(line.strip()) > 0 and (not line.strip().startswith('#')):
                #param = ['setfacl.exe', '-m', line.rstrip(), path]
                #retVal = subprocess.call(param)
                #if retVal != 0:
                    #raise Exception('ACLs not set successfully')
                                      
else:
    API_VERSION = 2

    def acl_get(path, item, st, numeric_owner=False):
        pass
    def acl_set(path, item, numeric_owner=False):
        pass
