Hard_Reload
===========
Minimal GUI tool (qt based) used to hard reload python packages, it features
autocompletion and might be compatible with softimage (through pyqtforsoftimage)
and maya.

Dependencies
-------------
- [wishlib](http://github.com/csaez/wishlib)

Installation
------------
Clone the repo and type in a terminal:

    python setup.py install

Ussage (within softimage/maya)
------------------------------

    from wishlib import anchor
    from hard_reload import HardReload

    HardReload.exec_(anchor)
