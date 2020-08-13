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
        
        parametres = [[_('Langue'),'language','lang','char'],
                      [_('Couleur de fond texte'),'interface','couleur_fond','char'],
                      [_('Couleur du texte'),'interface','couleur_fond_texte','char'],
                      [_('Couleur de fond saisie'),'interface','couleur_fond_saisie','char'],
                      [_('Couleur du texte saisie'),'interface','couleur_texte_saisie','char'],
                      [_('Commande youtube-dl'),'youtube-dl','path','char'],
                      [_('Départ téléchargements (heure)'),'active','from','digit'],
                      [_('Fin des téléchargements (heure)'),'active','to','digit'],
                      [_('Dossier destination des mp3'),'path','mp3','char'],
                      [_('Dossier destination des vidéos'),'path','videos','char'],
                      ]
        self.composants = []
        
        for ligne in parametres:
            temporaire = []
            temporaire.append(Label(self.panel_002, text=ligne[0], bg=couleur_fond, fg=couleur_texte))
            temporaire.append(Entry(self.panel_002, bg=couleur_fond_saisie, fg=couleur_texte_saisie))
            self.composants.append(temporaire)
        
        """ Implantation des composants
        """
        self.panel_001.pack(expand=True, fill=BOTH)
        self.panel_002.pack(expand=True, fill=BOTH)
        self.panel_003.pack(expand=True, fill=BOTH)
        curseur = 0
        for element in self.composants:
            element[0].grid(row = curseur, column = 0)
            element[1].grid(row = curseur, column = 1)
            curseur +=1
        
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
