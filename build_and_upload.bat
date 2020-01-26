rem https://blog.csdn.net/chroming/article/details/82057399
rmdir /s/q build
rmdir /s/q dist
python setup.py clean
python setup.py sdist
python setup.py bdist_wheel --universal
twine upload dist/*