import os

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 10
def sample10(request):
    clientId = os.environ['GROUPDOCS_CID']
    privateKey = os.environ['GROUPDOCS_PKEY']
    #serviceUrl = os.environ['GROUPDOCS_URL']
    fileGuId = request.POST.get('fileId')
    email = request.POST.get('email')

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(fileGuId) == False or IsNotNull(email) == False:
        return render_to_response('__main__:templates/sample10.pt', { })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    api = StorageApi(apiClient)

    try:
        files = api.ListEntities(userId = clientId, path = '', pageIndex = 0)
        for item in files.result.files: #selecting file names
            if item.guid == fileGuId:
                fileGuId = item.id
        docApi = DocApi(apiClient)
        docApi.ShareDocument(clientId, fileGuId, body = [ email, ])
    except Exception, e:
        return render_to_response('__main__:templates/sample10.pt', 
                                  { 'errmsg' : str(e) })

    return render_to_response('__main__:templates/sample10.pt', 
                              { 'fileId' : fileGuId, 
                               'email' : email }, 
                              request=request)
