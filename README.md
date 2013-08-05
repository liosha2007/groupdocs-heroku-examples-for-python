This quickstart will get you going with the GroupDocs Python sample app on Heroku.

## Prerequisites

* A Heroku user account with [Heroku toolbelt](https://toolbelt.heroku.com/) installed on the local workstation.
* Add GroupDocs addon to your app.

## Add GroupDocs Add-on to your app

	:::term
    $ heroku addons:add groupdocs
    -----> Adding groupdocs to sharp-mountain-4007... done

## Clone the sample repository to your local folder

	:::term
	$ git clone git://github.com/groupdocs/groupdocs-heroku-examples-for-python.git

## Store Your App in Git

    :::term
	$ cd groupdocs-heroku-examples-for-python
    $ git init
    $ git add .
    $ git commit -m "init"

## Deploy to Heroku/Cedar

Create the app on the Cedar stack:

    :::term
    $ heroku create --stack cedar
    Creating stark-sword-397... done, stack is cedar
    http://stark-sword-397.herokuapp.com/ | git@heroku.com:stark-sword-397.git
    Git remote heroku added

Deploy your code:

    :::term
    $ git push heroku master

## Live running app
This sample app is also running live on Heroku. To view and try, please open [http://groupdocs-heroku-python-exmpls.herokuapp.com/](http://groupdocs-heroku-python-exmpls.herokuapp.com/).

###[Sign, Manage, Annotate, Assemble, Compare and Convert Documents with GroupDocs](http://groupdocs.com)
1. [Sign documents online with GroupDocs Signature](http://groupdocs.com/apps/signature)
2. [PDF, Word and Image Annotation with GroupDocs Annotation](http://groupdocs.com/apps/annotation)
3. [Online DOC, DOCX, PPT Document Comparison with GroupDocs Comparison](http://groupdocs.com/apps/comparison)
4. [Online Document Management with GroupDocs Dashboard](http://groupdocs.com/apps/dashboard)
5. [Doc to PDF, Doc to Docx, PPT to PDF, and other Document Conversions with GroupDocs Viewer](http://groupdocs.com/apps/viewer)
6. [Online Document Automation with GroupDocs Assembly](http://groupdocs.com/apps/assembly)

###Created by [GroupDocs Marketplace Team]( http://groupdocs.com/marketplace/ ).