# Ordie: The Primordial Microcontroller Book

Ordie is a primordial microcontroller designed to showcase the current state-of-the-art of open silicon.

## Reading the Book

This book is available online at:

## Building the book

In order to build the book, you will need Python and Sphinx. It is recommended that you use a venv:

```sh
$ git clone ordie
$ cd ordie
$ python -mvenv .
$ . bin/activate # Bash shell
$ .\\Scripts\\activate.ps1 # Powershell
(book) $ pip install -r requirements.txt
```

To build the book, run `sphinx-build`:

```sh
(book) $ sphinx-build.exe -b html source build
Running Sphinx v5.3.0
making output directory... done
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 1 source files that are out of date
updating environment: [new config] 1 added, 0 changed, 0 removed
reading sources... [100%] index
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] index
generating indices... genindex done
writing additional pages... search done
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded.

The HTML pages are in build.
(book) $
```

You can then open the resulting book in your web browser:

_Firefox:_

```bash
$ firefox build/index.html                               # Linux
$ open -a "Firefox" build/index.html                     # OS X
$ Start-Process "firefox.exe"  "$(pwd)\build\index.html" # Windows (PowerShell)
$ start firefox.exe "%cd%\build\index.html"              # Windows (Cmd)
```

_Chrome:_

```bash
$ google-chrome build/index.html                        # Linux
$ open -a "Google Chrome" build/index.html              # OS X
$ Start-Process "chrome.exe"  "$(pwd)\build\index.html" # Windows (PowerShell)
$ start chrome.exe "%cd%\build\index.html"              # Windows (Cmd)
```