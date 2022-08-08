sudo apt update
sudo apt install -y python3.5
sudo rm /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install -y gunicorn
sudo pip3 install -y django==2.1