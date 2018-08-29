# HTML Uploader for Blogger
command line based HTML uploader for Google Blogger written by Python.

## Environment
* Python 3
* pip (Python module)
* Google Account

## Making ID (Rough)
* Blog ID:
 - When finished a Blog on Blogger, blogID displayed by Url Address bar.
* Client ID and Client Secret ID
 - Go to Google Developers Console, and create new project.
 - Enable Blogger api.
 - From Credentials page, click on "OAuth consent screen" tab. Then click on "Save" button
 - From Credentials page, click on "Create Credentials" dropdown and select "OAuth client ID"
 - From Create Client ID page, select "Other" and fill out "Name"
 - Finish by clicking create, console will provide client ID and Client Secrect
* Re-write script to get three IDs.
```
CLIENT_ID     = 'INPUT CLIENT ID'
CLIENT_SECRET = 'INPUT CLIENT SECRET'
BLOG_ID       = 'INPUT BLOG ID'
```

## Install python module
```
$ pip install google--api-python-client oauth2client
```

## Usage
At the first time, please "authirization" and "allow" on the browser.  
If successful, generated "upgger.dat" credential file.
* Basic type (-i option is required)
```
$ python3 upgger.py -i hello.html
```
In the above, title is filename(hello.html), label is none, status is LIVE.

* Add to -t or --title option
```
$ python3 upgger.py -i hello.html -t hello
```
In the above, title is "hello", label is none, status is LIVE.
```
$ python3 upgger.py -i hello.html -t "Hello World"
$ python3 upgger.py -i hello.html -t Hello\ World
```
In the above using double quote or backslash, title is "Hello World", label is none, status is LIVE.

* Add to -l or --label option
```
$ python3 upgger.py -i hello.html -l abc,def
```
In the above, title is filename, labels are "abc" and "def", status is LIVE.  
Delimitor is comma charactor.

* Add to -d or --draft option
```
$ python3 upgger.py - hello.html -d
```
In the above, title is filename, label is none, status is DRAFT.
 
## Limitation
* no upload image file
* no schedule
* no permalink

## Version
* v0.10 2018/08/30 new creation
