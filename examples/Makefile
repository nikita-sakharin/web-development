all: python

install:
	apt install nginx pycodestyle python3 python3-pip python3-venv

python:
	python3 -m venv .venv
	. .venv/bin/activate
	pip3 install -r requirements.txt

start-nginx:
	cp -r static /var/www
	nginx -s reload -c $(shell pwd)/nginx/nginx.conf
