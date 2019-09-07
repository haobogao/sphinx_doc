#!bin/bash
cd /root/sphinx_doc
git pull
make html 
cp -r ./build/html/* /var/www/html
