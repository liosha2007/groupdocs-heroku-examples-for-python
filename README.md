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
