#!/usr/bin/env bash
# build docs
git checkout gh-pages
git pull
rm -rf *
touch .nojekyll
git checkout master
cd docs
make clean
make html
cd ..
mv docs/build/html/* ./
rm -rf docs
git add -A
git commit -m "Publish updated docs"
git push origin gh-pages
# switch back
git checkout master