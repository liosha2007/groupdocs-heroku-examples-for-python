import os

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 5
def sample5(request):
    clientId = os.environ['GROUPDOCS_CID']
    privateKey = os.environ['GROUPDOCS_PKEY']
    #serviceUrl = os.environ['GROUPDOCS_URL']
    srcPath = request.POST.get('srcPath')
    dstPath = request.POST.get('dstPath')
    action = request.POST.get('action')


    if IsNotNull(action) == False or IsNotNull(srcPath) == False or IsNotNull(dstPath) == False:
        return render_to_response('__main__:templates/sample5.pt', { })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    api = StorageApi(apiClient)

    try:
        docApi = DocApi(apiClient)
        srcFile = docApi.GetDocumentMetadataByPath(clientId, srcPath)
        
        fileID = int(srcFile.result.last_view.document.id)

        if action == 'copy':
            newfile = api.MoveFile(clientId, dstPath, Groupdocs_Copy = fileID)

        if action == 'move':
            newfile = api.MoveFile(clientId, dstPath, Groupdocs_Move = fileID)
    except Exception, e:
        return render_to_response('__main__:templates/sample5.pt', 
                                  { 'errmsg' : str(e) })

    return render_to_response('__main__:templates/sample5.pt', 
                              { 'dstPath' : dstPath, 
                               'srcPath' : srcPath,
                               'newfile' : newfile }, 
                              request=request)
