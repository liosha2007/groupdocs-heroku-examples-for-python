import os
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.FileStream import FileStream
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 3
def sample3(request):
    clientId = os.environ['GROUPDOCS_CID']
    privateKey = os.environ['GROUPDOCS_PKEY']
    #serviceUrl = os.environ['GROUPDOCS_URL']
    inputFile = request.POST.get('fileData')


    if inputFile == None:
        return render_to_response('__main__:templates/sample3.pt', { })
    elif IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample3.pt', { 'errmsg' : 'User id or Private key not found!' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    api = StorageApi(apiClient)

    try:
        # a hack to get uploaded file size
        inputFile.file.seek(0, 2)
        fileSize = inputFile.file.tell()
        inputFile.file.seek(0)

        fs = FileStream.fromStream(inputFile.file, fileSize)
        response = api.Upload(clientId, inputFile.filename, fs)
    except Exception, e:
        return render_to_response('__main__:templates/sample3.pt', 
                                  { 'error' : str(e) })

    return render_to_response('__main__:templates/sample3.pt', 
                              { 'guid' : response.result.guid, 'filename' : inputFile.filename }, 
                              request=request)
