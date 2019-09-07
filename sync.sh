#!/bin/bash
git pull
make html
rm /home/haobo/website/* -rf
cp -r ./build/html/* /home/haobo/website/
