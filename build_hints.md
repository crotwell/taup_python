
# regen python bindings:

cd ../TauP &&  ./gradlew iD genPythonBindings && mv build/python/*.py ../taup_python/src/taup/.

# Build/publish

Hints on publish:
https://packaging.python.org/en/latest/tutorials/packaging-projects/

```
conda activate taupy
python3 -m pip install --upgrade hatch
# make sure no extra files as anything in dir that is not gitignore will be
# in distribution
git status

hatch clean && hatch build
pytest
# update release/version in docs/source/conf.py
cd docs/source ; pip install -r requirements.txt; cd ../..
cd docs ; make html && open build/html/index.html ; cd ..
git status
hatch publish -u __token__ --auth <token>
```
