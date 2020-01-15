# Difference calculator
[![Maintainability](https://api.codeclimate.com/v1/badges/6b2f4cd0c3a10513153b/maintainability)](https://codeclimate.com/github/GeVhoo/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6b2f4cd0c3a10513153b/test_coverage)](https://codeclimate.com/github/GeVhoo/python-project-lvl2/test_coverage)
[![Build Status](https://travis-ci.org/GeVhoo/python-project-lvl2.svg?branch=master)](https://travis-ci.org/GeVhoo/python-project-lvl2)

Hello World!

This is my second project that i do in Hexlet course.
In this project I made a utility to find differences in configuration files.

Hope you enjoy it!
##

### Direct install:

```bash
pip install -i https://test.pypi.org/simple/ gevhoo-diff-calc --extra-index-url https://pypi.org/simple/
```

[![asciicast](https://asciinema.org/a/QTk6TTBUwEtkOdQV9O0hIVnOC.svg)](https://asciinema.org/a/QTk6TTBUwEtkOdQV9O0hIVnOC)

### Comparing two flat JSON files

```bash
gendiff before.json after.json
```

[![asciicast](https://asciinema.org/a/KkYNMPMIVYn4GDrHjiEss9lpv.svg)](https://asciinema.org/a/KkYNMPMIVYn4GDrHjiEss9lpv)


### Comparing two flat YAML files

```bash
gendiff before.yml after.yml
```

[![asciicast](https://asciinema.org/a/PYfu2UyDgeF6s39auRYYhPAU5.svg)](https://asciinema.org/a/PYfu2UyDgeF6s39auRYYhPAU5)

### Comparing two files with nested structures

```bash
gendiff before_complex.json after_complex.json
```

[![asciicast](https://asciinema.org/a/OAlOi8JZo6BYHHhTL98XYbiIF.svg)](https://asciinema.org/a/OAlOi8JZo6BYHHhTL98XYbiIF)

### Comparison output of two files in plain format

```bash
gendiff -f plain before_complex.json after_complex.json
```

[![asciicast](https://asciinema.org/a/3BGNBtWnNdnOZmvM0z7ZmLaxw.svg)](https://asciinema.org/a/3BGNBtWnNdnOZmvM0z7ZmLaxw)

### Comparison output of two files in JSON format

```bash
gendiff -f json before_complex.json after_complex.json
```

[![asciicast](https://asciinema.org/a/LmL9mwiHxHrfi97PNsDFJEga7.svg)](https://asciinema.org/a/LmL9mwiHxHrfi97PNsDFJEga7)


### Links

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [Flake8](https://flake8.pycqa.org/)                                         | "Linter"                                                |
| [CodeClimate](https://codeclimate.com/)                                     | "Verifying code quality in automatic mode"              |
| [Travis-ci](https://travis-ci.org/)                                         | "Continuous Integration"                                |
| [pytest](https://pypi.org/project/pytest/)                                  | "For test coverage"                                     |

