#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

readonly WORKERS=4

function main() {
  if ! gunicorn --workers ${WORKERS} myapp:app ; then
    echo "Failed to run gunicorn..."
    return 1
  fi
}

main $@
