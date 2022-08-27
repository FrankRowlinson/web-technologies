sudo apt update
sudo apt install -y python3.5
sudo apt install -y python3.5-dev
sudo rm /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install gunicorn
sudo pip3 install django==2.1.5
sudo pip3 install mysqlclient==1.3.7
sudo pip3 install mysqlclient
sudo apt install -y mysql-server-5.6