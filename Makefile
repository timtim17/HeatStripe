package-mac:
	rm -r dist
	rm -r build
	python setup.py py2app
