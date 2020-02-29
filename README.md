# Sclera Platform Administration Tool

A tool to install [Sclera](https://github.com/scleradb/sclera) command line, and add/remove add-on packages.

## Usage

```
       scleradmin [-h] [--install] [--add package [package ...]]
                  [--remove package [package ...]] [--update] [--root rootdir]
                  [--overwrite]

Sclera Platform Administration

optional arguments:
  -h, --help            show this help message and exit
  --install             install Sclera in the root directory
  --add package [package ...]
                        add packages
  --remove package [package ...]
                        remove packages
  --update              update the installed packages to the latest version
  --root rootdir        root directory location (if not specified, will use
                        $SCLERA_ROOT if present, otherwise ~/sclera)
  --overwrite           overwrite root directory if present

In --add and --remove above, 'package' has the format 'org:name:version',
where 'org:' and ':version' are optional. When not specified, 'org' defaults
to 'com.scleradb' and 'version' defaults to the latest integration version.

Sclera requires Java version 8 or higher.
```
