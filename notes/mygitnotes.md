## My Git Notes

TLDR; Important notes related to Git

### Remove *.pyc* files trace
  ```
  find . -name "*.pyc" -exec git rm -f "{}" \;
  ```
### Remove folder from git
  ```
  git rm -r --cached myFolder
  ```
