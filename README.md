Hard_Reload
===========

`hard_reload` is a simple qt menu for flushing python packages from memory on
the fly, it features autocompletion and should be used within Autodesk Maya
(it's quite useful for develoment!).


Installation
------------

Copy or symlink `hard_reload.py` to your maya/scripts directory __or__ clone
this repo and install the package by typing in a terminal:

```bash
python setup.py install
```

> Last method might require root access

Usage
-----

Once installed you can launch `hard_reload` by typing:

```python
import hard_reload
hard_reload.show()
```
