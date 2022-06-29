# Gabbi Demo

This repository is intended for educational purposes on Gabbi 
a declareable HTTP API testing framework that allows you to write
tests with a declaritive YAML syntax

Gabbi can be found at the repository:
https://github.com/cdent/gabbi

### Overview

Gabbi is a tool for running HTTP tests where requests and responses are
expressed as declarations in YAML files:

```
tests:
- name: retrieve items
  GET: /items
```

### YAML Runner

Although Gabbi is written in python and uses `unittest` data structures
and processes but, there is no requirement that the host be a python
service.

This repository uses the Gabbi driver to build tests but there is no
need to do this if your test environment doesn't have the python
dependencies in place. A YAML Runner is provided and can be run like so:

```
gabbi-run http://localhost:3500 -- ./test/gabbits/dogs.yaml
```

### Test Format

Each YAML file represents an ordered list of HTTP requests along with
the expected responses. To support more complex APIs
[JSONPath](https://goessner.net/articles/JsonPath/) is used to query
response bodies and templating of test data to allow access to prior
HTTP responses in the current request. You can read more on the
access to prior HTTP responses and other magical variables
[here](https://gabbi.readthedocs.io/en/latest/format.html#substitution)