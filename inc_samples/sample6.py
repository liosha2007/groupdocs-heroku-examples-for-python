import os, json

from pyramid.renderers import render_to_response
from pyramid.response import Response

from groupdocs.ApiClient import ApiClient
from groupdocs.SignatureApi import SignatureApi
from groupdocs.models.SignatureSignDocumentSettings import SignatureSignDocumentSettings
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 6
def sample6(request):
    clientId = os.environ['GROUPDOCS_CID']
    privateKey = os.environ['GROUPDOCS_PKEY']
    #serviceUrl = os.environ['GROUPDOCS_URL']
    if request.content_type != 'application/json':
        return render_to_response('__main__:templates/sample6.pt', { 'clientId' : clientId, 'privateKey' : privateKey })

    jsonPostData = request.json_body
    # get parameters
    documents = jsonPostData.get('documents')
    signers = jsonPostData.get('signers')
    # checking parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(documents) == False or IsNotNull(signers) == False:
        return render_to_response('__main__:templates/sample6.pt', { })

    for signer in signers:
        signer['placeSingatureOn'] = ''

    # create signer
    signerReq = GroupDocsRequestSigner(privateKey)
    # create ApiClient
    apiClient = ApiClient(signerReq)
    # create signsture API object
    signatureApi = SignatureApi(apiClient)
    # create setting variable for signature SignDocument method
    settings = SignatureSignDocumentSettings()
    settings.documents = documents
    settings.signers = signers
    # request to sign document
    response = signatureApi.SignDocument(clientId, body = settings)
    # request successful
    if response.status == 'Ok':
        return_data = json.dumps({ 'responseCode' : 200, 'documentId' : response.result.documentId })
        return Response(body = return_data, content_type = 'application/json')
    
    return render_to_response('__main__:templates/sample6.pt', 
                          { 'errmsg' : response.error_message })
