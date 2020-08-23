# -*- coding:utf-8 -*-
#
# Copyright © 2020 cGIfl300
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the “Software”),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from configuration import *
import os
import codecs
from pathlib import Path
import configparser


class SR:
    """ Save and Restaure class
    Permits to save the download queue on the hard drive and to restaure it.
    Usage:
    SR.save(dllist)
    SR.restaure(dllist)
    """

    def __init__(self, local_queue):
        self.dllist = local_queue

    def save(self):
        # Save queue
        fname = Path(f"{repertoire_script}data{os.sep}dl.ini")
        if not fname.is_file():
            # if no queue folder found, then we create it
            try:
                os.mkdir(f"{repertoire_script}data")
            except:
                pass

        # We always erase the old queue
        configfile = codecs.open(f"{repertoire_script}data{os.sep}dl.ini", "w", "utf-8")

        configfile.close()

    def run(self):
        print("Running!")
