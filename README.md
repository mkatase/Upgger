# Upgger - HTML Uploader for Blogger
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
	- From Credentials page, click on "Credentials" dropdown and select "OAuth client ID"
	- From Create Client ID page, select "Other" and fill out "Name"
	- From Credentials page, select "Credentials" tab and download "secret id" file on project.
	- Rename a download "secret id" file(json) to "secret_id.json"
	- Move "secret_id.json" file to ".upgger.conf" directory
* Re-write script to get BLOG ID.
	- Move to ".upgger.conf" directory and open "upgger.yaml"
	- blog_id displayed on URL address bar in Blogger edit screen
```
blog_id: 'INPUT BLOG ID'
```
* Please check ".upgger.conf" directory
```
$ ls -a .upgger.conf
. .. secret_id.json upgger.yaml
```

## Install python module
```
$ pip install google--api-python-client oauth2client PyYAML
```

## Usage
At the first time, please "authirization" and "allow" on the browser.  
If successful, generated "upgger.json" credential file.
```
$ ls -a .upgger.conf
. .. secret_id.json upgger.json upgger.yaml
```

* Basic type (-i option is required)
```
$ python3 upgger.py -i hello.html
```
In the above, title is filename(hello.html), label is none,
published date is none, status is LIVE.

* Add to -t or --title option
```
$ python3 upgger.py -i hello.html -t hello
```
In the above, title is "hello", label is none,
published date is none, status is LIVE.
```
$ python3 upgger.py -i hello.html -t "Hello World"
$ python3 upgger.py -i hello.html -t Hello\ World
```
In the above using double quote or backslash, title is "Hello World",
label is none, published date is none, status is LIVE.

* Add to -l or --label option
```
$ python3 upgger.py -i hello.html -l abc,def
```
In the above, title is filename, labels are "abc" and "def",
published date is none, status is LIVE.  
Delimitor is comma charactor.

* Add to -p or --pub option
```
$ python3 upgger.py -i hello.html -p 20XX-YY-ZZ
```
In the above, title is filename, label is none,
published date is "20XX-YY-ZZ", status is LIVE(no effect).

* Add to -d or --draft option
```
$ python3 upgger.py -i hello.html -d
```
In the above, title is filename, label is none,
published date is none, status is DRAFT.
 
## Limitation
*  ~~no upload image file~~
*  ~~no schedule~~
* no permalink

## Development Environment
* OS: Fedora 28 (4.17.19.200) on x86_64
* Python: 3.6.6
* google-api-python-client: 1.7.4
* oauth2client: 4.1.2

## Version
* v0.40 2018/09/02 add to published option(-p)
* v0.30 2018/09/01 delete kind/id in body and change flags
* v0.20 2018/08/31 add to read json and yaml
* v0.10 2018/08/30 new creation
