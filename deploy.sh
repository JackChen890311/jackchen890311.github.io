#!/usr/bin/env zsh
set -e

hexo g -d
git add .

if [[ -n "$1" ]]; then
  git commit -m "$1"
else
  git commit    # opens $EDITOR
fi

git push