#!/usr/bin/env python
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
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from Caesar import encrypt

rot_form = """
<form method="post" action="/">
<h2>Enter some text to rotate</h2>
<input type="text" name="rotate" value="{rotate:s}"/>
<br>
<h3>How much do you want to rotate it by?</h3>
<br>
<input type="text" name="rot_amt" value="{rot_amt:d}"/>
<input type="submit" value="Rotate it!"/>

</form>

"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.write_form()

    def post(self):
        text_to_rotate = self.request.get("rotate")
        amt_to_rotate = int(self.request.get("rot_amt"))
        rotated_text = encrypt(text_to_rotate, amt_to_rotate)
        print "Rotated Text:", rotated_text
        self.write_form(rotated_text, amt_to_rotate)

    def write_form(self, rotate="", rot_amt=0):

        self.response.out.write(rot_form.format(
            rotate=rotate,
            rot_amt=rot_amt,
        ))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
