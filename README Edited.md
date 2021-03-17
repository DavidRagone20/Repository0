Dockerized development tools
===============
readme with commit
# David's Repository is the Best Repository

Files in this directory can be used to spin up JupyterLab and Jupyter Notebook environments for rapid testing.

Ideally run this in an iso
| Grids and | lines of words |
|and letters |and sentences|
| If you don't have graph's on yours repository | I feel bad for you |
lated Python 3.7 environment, with `pyppeteer` installed.
Docker and docker-compose are also required for these tools to work.

- `build-and-screenshot.sh` creates screenshots of the current state of the containers
- `snap.py` creates screenshots of the current state of the test.ipynb file
- `docker-compose up -d` will run two containerized Jupyter environments,
   one with JupyterLab and another with Jupyter Notebook, and install a specified build of pydeck.
   The `PYDECK_VERSION` and `PYPI_INSTALL_URL` can be used to specify the version of pydeck to download and test.
- `docker-compose down` will stop the containers this directory starts

An example use case would be testing a version of pydeck published to test.pypi.com.

This tool is only for local development.
