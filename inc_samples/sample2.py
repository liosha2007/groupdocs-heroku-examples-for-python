import os

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 2
def sample2(request):
    clientId = os.environ['GROUPDOCS_CID']
    privateKey = os.environ['GROUPDOCS_PKEY']
    #serviceUrl = os.environ['GROUPDOCS_URL']
    
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample2.pt', { 'errmsg' : 'User id or Private key not found!' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    api = StorageApi(apiClient)

    try:
        files = api.ListEntities(userId = clientId, path = '', pageIndex = 0)
        names = []
        for item in files.result.files: #selecting file names
            names.append(item.name)
        #~ import pdb; pdb.set_trace()
    except Exception, e:
        return render_to_response('__main__:templates/sample2.pt', 
                                  { 'errmsg' : str(e) })

    return render_to_response('__main__:templates/sample2.pt', 
                              { 'names' : names }, 
                              request=request)
