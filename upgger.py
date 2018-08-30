#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  v0.10 2018/08/30 new creation
  v0.20 2018/08/31 add to json and yaml

  uploader for blogger

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
__version__ = '0.20'

from sys import *
from string import *
from argparse import ArgumentParser
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client        import tools,file
import httplib2
import os
import yaml

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

    def checkdir(self):
        s_dir = os.path.abspath( os.path.dirname( __file__ ) )
        self.c_dir = os.path.join( s_dir, ".upgger.conf" )

        if not os.path.exists( self.c_dir ):
            os.mkdir( self.c_dir )

    def checkstorage(self):
        flags         = '--auth_host_name localhost --logging_level INFO'
        scope         = 'https://www.googleapis.com/auth/blogger'

        c_path = os.path.join( self.c_dir, "upgger.json" )
        s_path = os.path.join( self.c_dir, "secret_id.json" )
        storage     = file.Storage( c_path )
        credentials = storage.get()

        if not credentials or credentials.invalid:
            flags = tools.argparser.parse_args(flags.split())
            flow  = flow_from_clientsecrets(s_path, scope)
            credentials = tools.run_flow(flow, storage, flags)

        return credentials

    def createbody(self):
        body = {}
        body['kind']       = 'blogger#post'
        body['id']         = self.b_id
        body['title']      = self.title
        body['content']    = self.content
        if self.label is not None: 
            body['labels'] = self.label.split(',')
        return body

    def getyaml(self):
        b_path = os.path.join( self.c_dir, "upgger.yaml" )
        with open(b_path) as fp:
            data = yaml.load(fp)
        self.b_id = data['blog_id']

    def uploadfile(self, cr):
        http = cr.authorize(http = httplib2.Http())
        service = build('blogger', 'v3', http=http)
        posts   = service.posts()

        self.getyaml()
        insert = posts.insert(blogId=self.b_id, isDraft=self.draft,
                              body=self.createbody())
        insert.execute()

    def start(self):
        self.checkfile()
        self.checkdir()
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
