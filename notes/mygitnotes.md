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

### [Git Large File Storage](https://git-lfs.github.com/)
```
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
```
### Removing big or sensitive files from history: [bfg](https://rtyley.github.io/bfg-repo-cleaner/)
