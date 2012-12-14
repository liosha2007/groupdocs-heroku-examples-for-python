import os
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.MgmtApi import MgmtApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 1
def sample1(request):
    clientId = os.environ['GROUPDOCS_CID']
    privateKey = os.environ['GROUPDOCS_PKEY']
    #serviceUrl = os.environ['GROUPDOCS_URL']

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample1.pt', { 'errmsg' : 'User id or Private key not found!' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    api = MgmtApi(apiClient)

    try:
        userInfo = api.GetUserProfile(clientId)
        
    except Exception, e:
        return render_to_response('__main__:templates/sample1.pt', 
                                  { 'errmsg' : str(e) })

    return render_to_response('__main__:templates/sample1.pt', 
                              { 'userInfo' : userInfo.result.user }, 
                              request=request)
