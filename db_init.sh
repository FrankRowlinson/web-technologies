sudo /etc/init.d/mysql start

mysql -uroot -e "CREATE DATABASE web;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON web.* TO 'box'@'localhost' WITH GRANT OPTION;"

cd ~/web/ask
python3 manage.py makemigrations
python3 manage.py migrate

cd ..