# Copyright (C) 2013 S. Daniel Francis <francis@sugarlabs.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

import os

from sys import argv
from pyrp.core import macros
from pyrp.core import log

usage = """
Usage:
    %s FILE -- Execute a PyRP file.
""" % argv[0]

helpmsg = """Options:
  --version    show program's version number and exit
  -h, --help   show this help message and exit
  -u, --usage  show program's usage message and exit
"""


def showhelp(name=True, usagemsg=True, options=True, code=0):
    if name:
        print macros.full_name
    if usagemsg:
        print usage
    if options:
        print helpmsg
    exit(code)

if len(argv) <= 1:
    showhelp(code=1)

argument = argv[1]

if argument == '--help':
    showhelp()
elif argument == '--usage':
    showhelp(name=False, options=False)
elif argument == '--version':
    showhelp(usagemsg=False, options=False)
elif argument[:2] == '--':
    log.error('Unknown argument')
    showhelp(code=1)

if not os.path.exists(argument) or not os.path.isfile(argument):
    log.error("%s: file not found" % argument)
else:
    filepath = argument