#!/bin/bash
# filename run
if [ -f "$1/$2.py" ];then
	python "$1/$2.py"
else
	echo "not found files, dir: $1, file: $2"
fi