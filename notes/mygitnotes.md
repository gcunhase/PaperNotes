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
```
java -jar bfg.jar --delelte-folders data
```

### Helping open source projects
* [CodeMontage](http://www.codemontage.com/): open source, social good projects that benefit organizations making a difference in the world.
* [CodeTriage](https://www.codetriage.com/): get one issue from your favorite repo per day to help you dig deeper, learn more, and stay involved with the code you rely on.
* [issuehub.io](http://issuehub.io/): Contribute to Open Source. Search issue labels to find the right project for you!
* [Open Source Friday](https://opensourcefriday.com/)
* [Pull Request Roulette](http://www.pullrequestroulette.com/): Find open source pull requests that need a reviewer before merging.

### Personal Website
* [Jekyll](https://jekyllrb.com/docs/): "simple, blog-aware, static site generator for personal, project, or organization sites"
```
sudo apt-get install ruby ruby-dev build-essential
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME=$HOME/gems' >> ~/.bashrc
echo 'export PATH=$HOME/gems/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
gem install jekyll bundler
```
