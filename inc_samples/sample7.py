import os, base64, shutil

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 7
def sample7(request):
    clientId = os.environ['GROUPDOCS_CID']
    privateKey = os.environ['GROUPDOCS_PKEY']
    #serviceUrl = os.environ['GROUPDOCS_URL']
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample7.pt', 
                                  { 'error' : 'You do not enter you User id or Private key' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    api = StorageApi(apiClient)
    try:
        files = api.ListEntities(clientId, "", extended = True); # geting all Entities from curent user
    except Exception, e:
        return render_to_response('__main__:templates/sample7.pt', 
                                  { 'error' : str(e) })

    pathToThDir = 'static/img/'
    if os.path.exists(pathToThDir):
        shutil.rmtree(pathToThDir)
    os.mkdir(pathToThDir)
    thumbnails = {};
    for i in range(len(files.result.files)):
        if files.result.files[i].thumbnail != None:
            fp = open(pathToThDir + 'thumbnail' + str(i) + '.jpg', 'wb')
            fp.write(base64.b64decode(files.result.files[i].thumbnail))
            fp.close()
            thumbnails['static/img/thumbnail' + str(i) + '.jpg'] = files.result.files[i].name

    return render_to_response('__main__:templates/sample7.pt', 
                              { 'thumbnails' : thumbnails }, 
                              request=request)
