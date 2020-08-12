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

import os
from pathlib import Path
import configparser
import codecs

chemin_script = os.path.abspath(__file__)
repertoire_script = chemin_script[: next(i for i in reversed(range(len(chemin_script))) if chemin_script[i] == os.path.sep) + 1]

class configuration():
    def __init__(self):
        # Chechink if a configuration file already exist
        fname = Path(f"{repertoire_script}data{os.sep}setup.ini")
        if not fname.is_file():
            # if no setup file is found, then, create it with default values
            try:
                os.mkdir(f"{repertoire_script}data")
            except:
                pass
            
            configfile = codecs.open(f"{repertoire_script}data{os.sep}setup.ini", "w", "utf-8")
            configfile.write("""[language]
lang = fr

[interface]
couleur_fond = black
couleur_texte = green
couleur_fond_saisie = black
couleur_texte_saisie = green

[youtube-dl]
path = youtube-dl

[active]
from = 0
to = 23

; [path]
; mp3 = /home/error
; videos = /home/error""")
            configfile.close()
            
        config = configparser.ConfigParser()
        config.read(f"{repertoire_script}data{os.sep}setup.ini")
        self.langue_appli = config['language']['lang']
        self.couleur_fond = config['interface']['couleur_fond']
        self.couleur_texte = config['interface']['couleur_texte']
        self.couleur_fond_saisie = config['interface']['couleur_fond_saisie']
        self.couleur_texte_saisie = config['interface']['couleur_texte_saisie']
        self.youtubedl_path = config['youtube-dl']['path']
        self.activefrom = config['active']['from']
        self.activeto = config['active']['to']
        try:
            self.mp3 = config['path']['mp3']
        except:
            self.mp3 = repertoire_script + f"data{os.sep}"
        try:
            self.videos = config['path']['videos']
        except:
            self.videos = repertoire_script + f"data{os.sep}"
        

app = configuration()
couleur_fond = app.couleur_fond
couleur_texte = app.couleur_texte
couleur_fond_saisie = app.couleur_fond_saisie
couleur_texte_saisie = app.couleur_texte_saisie
couleur_activebackground = couleur_texte_saisie
couleur_activeforeground = couleur_fond_saisie
debug = True
langue_appli = app.langue_appli

path_youtubedl = app.youtubedl_path
path_mp3 = app.mp3
path_videos = app.videos

h_dep = app.activefrom
h_fin = app.activeto
