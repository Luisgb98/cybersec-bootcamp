#!/usr/bin/env bash
python3 setup.py sdist bdist_wheel

pip3 install ./dist/my_minipack-1.0.0.tar.gz