sudo apt update
sudo apt install -y python3.5
sudo apt install -y python3.5-dev
sudo rm /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install gunicorn
sudo pip3 install django==2.1
<<<<<<< HEAD
sudo pip3 install mysqlclient==1.3.7
=======
sudo pip3 install mysqlclient
>>>>>>> 4b3a0c56b401019befe5d7f5d28896d97d02372f
sudo apt install mysql-server-5.6