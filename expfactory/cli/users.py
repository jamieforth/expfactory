'''

Copyright (c) 2017, Vanessa Sochat
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''

from expfactory.logger import bot
from expfactory.server import app
from expfactory.defaults import EXPFACTORY_DATABASE
import sys
import os


def main(args,parser,subparser):
  
    # Only filesystem database has FOLDER
    header = 'TOKEN'
    if EXPFACTORY_DATABASE == "filesystem":
        header = 'FOLDER\tTOKEN' 
    print(header)

    # The user wants to list active subjects
    if args.list is True:
        tokens = app.list_users() # returns token or folder\ttoken
        for token in tokens:
            print(token)
        sys.exit(0)

    # The user wants to add new subjects
    number = args.new
    if number is not None:
        for i in range(number):
            user = app.generate_user()
            token = os.path.basename(user)
            if EXPFACTORY_DATABASE == "filesystem":
                print('%s\t%s' %(user,token))
            else:
                print(token)
    else:
        print('Specify number of new users:\n\texpfactory users --new 1')
