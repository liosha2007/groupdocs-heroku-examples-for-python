import os
import shutil
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 4
def sample4(request):
    clientId = os.environ['GROUPDOCS_CID']
    privateKey = os.environ['GROUPDOCS_PKEY']
    #serviceUrl = os.environ['GROUPDOCS_URL']
    file_id = request.POST.get('fileId')

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(file_id) == False:
        return render_to_response('__main__:templates/sample4.pt', { })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    api = StorageApi(apiClient)
               
    try:
        
        files = api.ListEntities(userId = clientId, path = '', pageIndex = 0)
        for item in files.result.files: #selecting file names
            if item.guid == file_id:
                fileName = item.name
               
        currentDir = os.path.dirname(os.path.realpath(__file__))
        
        newpath = currentDir + "/../tmp/"
        if not os.path.exists(newpath):
            os.makedirs(newpath)   
         
        fs = api.GetFile(clientId, file_id);

        if fs:
            #~ import pdb;  pdb.set_trace()
            filePath = newpath + fileName
        
            with open(filePath, 'wb') as fp:
                shutil.copyfileobj(fs.inputStream, fp)
        else:
            raise Exception('Wrong file ID!')
    except Exception, e:
        return render_to_response('__main__:templates/sample4.pt', 
                                  { 'errmsg' : str(e) })

    return render_to_response('__main__:templates/sample4.pt', 
                              { 'file_Id' : file_id, 
                               'filePath' : filePath }, 
                              request=request)
