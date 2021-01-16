#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

cp nginx/nginx.conf /etc/nginx
cp -r static /var/www
/etc/init.d/nginx stop
/etc/init.d/nginx start
