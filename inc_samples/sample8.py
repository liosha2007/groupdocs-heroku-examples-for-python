import os

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 8
def sample8(request):
    clientId = os.environ['GROUPDOCS_CID']
    privateKey = os.environ['GROUPDOCS_PKEY']
    #serviceUrl = os.environ['GROUPDOCS_URL']
    fileGuId = request.POST.get('fileId')
    dimension = request.POST.get('dimension') or '600x750'
    pageNumber = request.POST.get('pageNumber') or 0
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(fileGuId) == False:
        return render_to_response('__main__:templates/sample8.pt', 
                                  { 'errmsg' : 'You do not enter all parameters' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    docApi = DocApi(apiClient)
    try:
        url = docApi.GetDocumentPagesImageUrls(clientId, fileGuId, firstPage = int(pageNumber), pageCount = 1, dimension = dimension)
    except Exception, e:
        return render_to_response('__main__:templates/sample8.pt', 
                                  { 'errmsg' : str(e) })

    return render_to_response('__main__:templates/sample8.pt', 
                              { 'thumbnailUrls' : url.result.url, 
                               'fileId' : fileGuId, 
                               'pageNumber' : pageNumber }, 
                              request=request)
