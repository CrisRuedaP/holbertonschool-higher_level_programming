#!/bin/bash
#Get the HTTP status code of a URL passed
curl -sI -o /dev/null -w "%{http_code}" "$1"
