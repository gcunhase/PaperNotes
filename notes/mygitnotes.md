## My Git Notes

TLDR; Important notes related to Git

### Remove *.pyc* files trace
  ```
  find . -name "*.pyc" -exec git rm -f "{}" \;
  ```
