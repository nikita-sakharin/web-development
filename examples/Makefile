all: python

install:
	apt install nginx pycodestyle python3 python3-pip python3-venv

nginx:
	cp -r static /var/www
	/etc/init.d/nginx start -c nginx/nginx.conf

python:
	python3 -m venv .venv
	source .venv/bin/activate
	pip3 install -r requirements.txt
