
all: build

build:
	python site_builder.py
	jekyll
