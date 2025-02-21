#/bin/sh

ruff check jrequests
mypy jrequests --strict