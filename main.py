#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,y
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
# Enter your code here. Read input from STDIN. Print output to STDOUT


spain_language = u'í ó é á ñ ú'.split(" ")

german_language = u"ä ß ö".split(" ")

french_language = u"é à è ê ç ô ù â û î œ ï ë æ ñ".split(" ")

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('This API is POST only ')

    def options(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE'
    def post(self):
        input_str = self.request.POST['text']
        feq = {"Spanish": 0, "German": 0, "French": 0}
        for i in spain_language:
            feq["Spanish"] += input_str.count(i)
        for i in german_language:
            feq["German"] += input_str.count(i)
        for i in french_language:
            feq["French"] += input_str.count(i)
        sorted_feq = sorted(feq, key=feq.get)
        if feq[sorted_feq[-1]] == 0:
            self.response.write("English")
        else:
            self.response.write(sorted_feq[-1])

app = webapp2.WSGIApplication([
    ('/api', MainHandler)
], debug=False)
