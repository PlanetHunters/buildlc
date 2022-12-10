#!/bin/bash

rm tests.log
rm dist* -r
rm -r .tox
rm -r .pytest_cache
rm -r build
rm -R lcbuilder-reqs
rm -R *egg-info
set -e
tox -r > tests.log
tests_results=$(cat tests.log | grep "congratulations")
if ! [[ -z ${tests_results} ]]; then
  echo "Building"
  set +e
  rm dist* -r
  rm -r .tox
  rm -r .pytest_cache
  rm -r build
  rm -R lcbuilder-reqs
  set -e
  python3.8 -m venv lcbuilder-reqs
  source lcbuilder-reqs/bin/activate
  python3.8 -m pip install pip -U
  python3.8 -m pip install numpy==1.22.4
  python3.8 setup.py install
  python3.8 -m pip list --format=freeze > requirements.txt
  deactivate
  git_tag=$1
  git pull
  sed -i '5s/.*/version = "'${git_tag}'"/' setup.py
  git add requirements.txt
  git add setup.py
  git commit -m "Preparing release ${git_tag}"
  git tag ${git_tag} -m "New release"
  git push && git push --tags
else
  echo "Failed tests"
fi
set +e
rm -R lcbuilder-reqs
rm dist* -r
rm -r .tox
rm -r .pytest_cache
rm -r build
rm -R *egg-info
set -e
