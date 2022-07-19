NAME = lambda2color
VERSION=`python3 -c'import lambda2color; print(lambda2color.__version__)'`
PYTHON = python3
default: $(NAME).pdf

pypi_all: pypi_tags pypi_upload
# https://docs.python.org/2/distutils/packageindex.html
pypi_tags:
	git commit -am' tagging for PyPI '
	# in case you wish to delete tags, visit http://wptheming.com/2011/04/add-remove-github-tags/
	git tag $(VERSION) -m "Adds a tag so that we can put this on PyPI."
	git push --tags origin main

pypi_upload:
	$(PYTHON) setup.py sdist #upload
	twine upload dist/*

pypi_docs:
	#rm web.zip
	#ipython3 nbconvert --to html $(NAME).ipynb
	#mv $(NAME).html index.html
	#runipy $(NAME).ipynb  --html  index.html
	zip web.zip index.html
	open https://pypi.python.org/pypi?action=pkg_edit&name=$NAME

install_dev:
	pip3 uninstall -y $(NAME) ; pip3 install -e .
todo:
	grep -R * (^|#)[ ]*(TODO|FIXME|XXX|HINT|TIP)( |:)([^#]*)


# macros for tests
%.pdf: %.ipynb
	jupyter nbconvert --SphinxTransformer.author='Laurent Perrinet (INT, UMR7289)' --to pdf $<

# cleaning macros

clean:
	rm -fr figures/* *.pyc *.py~ build dist

.PHONY: clean
