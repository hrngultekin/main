#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt 

from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = ["/usr/lib"]

def setup():
	autotools.autoreconf("-vfi")
	autotools.configure("--disable-static \
		                 --without-portaudiocpp")

	
def build():
	
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" %get.installDIR())
	
	pisitools.dodoc("LICENSE", "README.md")

