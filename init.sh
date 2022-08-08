sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart


sudo ln -sf /home/box/web/etc/gunicorn.conf.py /etc/gunicorn.d/test.py
sudo gunicorn -c /etc/gunicorn.d/test.py hello


sudo ln -sf /home/box/web/etc/gunicorn-django.conf.py /etc/gunicorn.d/ask.py
sudo gunicorn -c /etc/gunicorn.d/ask.py ask.wsgi