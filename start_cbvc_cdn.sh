#!/bin/sh

if [ $# != 2 ]
then
  echo "Usage: "$0" <listen_addr> <listen_port>"
  exit 1
fi

gunicorn -c gunicorn.conf.py cbvc_cdn:app -b $1:$2
