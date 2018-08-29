#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  v0.10 2018/08/31 new creation

  uploader for blogger by python3

  Usage:
    $ python3 upgger.py -i hoge.html
  When this is the case, title is filename, label is none, status is LIVE.
    $ python3 upgger.py -t moge -i hoge.html
  When this is the case, title is "moge", label is none, status is LIVE.
    $ python3 upgger.py -t "hoge hoge" -i hoge.html
    or
    $ python3 upgger.py -t hoge\ hoge -i hoge.html
  When this is the case, title is "hoge hoge", label is none, status is LIVE.
    $ python3 upgger.py -l aaa -i hoge.html
  When this is the case, title is filename, label is "aaa", status is LIVE.
    $ python3 upgger.py -l aaa,bbb -i hoge.html
  When this is the case, title is filename, labels are "aaa" and "bbb",
  status is LIVE.
    $ python3 upgger.py -i hoge.html -d
  When this is the case, title is filename, label is none, status is DRAFT.
"""

__author__  = 'mkatase (michimoto.katase@gmail.com'
__version__ = '0.10'

CLIENT_ID     = 'INPUT CLIENT ID'
CLIENT_SECRET = 'INPUT CLIENT SECRET'
BLOG_ID       = 'INPUT BLOG ID'

from sys import *
from string import *
from argparse import ArgumentParser
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
from oauth2client        import tools,file
import httplib2
import os

class Upgger:
    def __init__(self, opts):
        self.ifile = opts.file
        self.label = opts.label
        self.title = opts.title
        self.draft = opts.draft

    def checkfile(self):
        if os.path.isfile(self.ifile):
            with open(self.ifile) as fp:
                self.content = fp.read()
                if self.title is None:
                    n = self.ifile.rfind('/')
                    self.title = self.ifile[n+1:]
        else:
            print('Input File Not Found...')
            exit()

    def checkstorage(self):
        flags         = '--auth_host_name localhost --logging_level INFO'
        scope         = 'https://www.googleapis.com/auth/blogger'
        redirect_uri  = 'urn:ietf:wg:oauth:2.0:oob'
        flow          = OAuth2WebServerFlow(client_id=CLIENT_ID,
                                            client_secret=CLIENT_SECRET,
                                            scope=scope,
                                            redirect_uri=redirect_uri)

        storage     = file.Storage( __file__ + '.dat' )
        credentials = storage.get()

        if credentials is None or credentials.invalid:
            flags = tools.argparser.parse_args(flags.split())
            credentials = tools.run_flow(flow, storage, flags)
        #else:
        #    print('Storage file not found or Credentials invalid...')
        #    exit()

        return credentials

    def createbody(self):
        body = {}
        body['kind']       = 'blogger#post'
        body['id']         = BLOG_ID
        body['title']      = self.title
        body['content']    = self.content
        if self.label is not None: 
            body['labels'] = self.label.split(',')
        return body

    def uploadfile(self, cr):
        http = cr.authorize(http = httplib2.Http())
        service = build('blogger', 'v3', http=http)
        posts   = service.posts()

        insert = posts.insert(blogId=BLOG_ID, isDraft=self.draft,
                              body=self.createbody())
        #if self.draft:
        #    insert = posts.insert(blogId=BLOG_ID, isDraft=self.draft,
        #    #insert = posts.insert(blogId=BLOG_ID, isDraft="true",
        #                          body=self.createbody())
        #else:
        #    insert = posts.insert(blogId=BLOG_ID,
        #                          body=self.createbody())
        insert.execute()

    def start(self):
        self.checkfile()
        self.uploadfile( self.checkstorage() )

if __name__ == '__main__':

    U = '{} [-t|--title] <Title> [-l|--label] <Labels> '.format(__file__)
    U = U + '[-i|--in] <Input HTML> [-d|--draft]'
    p = ArgumentParser(usage=U)

    p.add_argument("-t", "--title", dest="title",
        help="Input Title (default is Input HTML filename")
    p.add_argument("-l", "--label", dest="label", default=None,
        help="Input Labels (comma separated)")
    p.add_argument("-i", "--in", dest="file",
        help="Input HTML file")
    p.add_argument("-d", "--draft", dest="draft", default=None,
        action="store_true", help="Input Status flag")
    p.add_argument('--version', action='version', version=__version__)
 
    args = p.parse_args()

    if len(argv) == 1:
        p.print_help()
        exit()

    if args.file is None:
        print('Input HTML file ([-i|--in] <HTML file>)')
        exit()

    Upgger(args).start()

# end of Upgger script
