Hard_Reload
===========

`hard_reload` is a Maya Qt widget for reloading python packages, useful for develoment!  
Type in the module name you want to reload, and press enter.

![image](https://github.com/csaez/hard_reload/assets/3758308/f9c244e9-3f9e-4b59-994f-1fd35a62a128)


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
