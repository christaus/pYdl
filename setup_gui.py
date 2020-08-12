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

from tkinter import *
import gettext
from configuration import *
from image_set import image_set

fr = gettext.translation("base", localedir=repertoire_script + "locales", languages=[langue_appli], fallback=False)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext


class Setup_GUI(Toplevel):
    """ Setup Graphical User Interface ...
    """

    def __init__(self, debug=False):
        Toplevel.__init__(self)
        self.debug = debug

    def interface(self):
        """ Interface itself
        """
        self.title(_("Configuration pYdl"))
        self.iconphoto(False, PhotoImage(file=f"{repertoire_script}images{os.sep}icone.png"))
        
        self.panel_001 = Label(self, bg=couleur_fond)
        self.panel_002 = Label(self, bg=couleur_fond)
        self.panel_003 = Label(self, bg=couleur_fond)
        
        self.entete = image_set(self.panel_001, f"images{os.sep}logo-small")
        
        """ Implantation des composants
        """
        self.panel_001.pack(expand=True, fill=BOTH)
        self.panel_002.pack(expand=True, fill=BOTH)
        self.panel_003.pack(expand=True, fill=BOTH)
        
    def apply_setup(self):
        """ Records setup on hard drive
        """

    def run(self):
        self.interface()


if __name__ == "__main__":
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state("icon")
    App = Setup_GUI()
    App.run()
    w.mainloop()
