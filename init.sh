sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart


sudo ln -sf /home/box/web/etc/gunicorn.conf.py /etc/gunicorn.d/test
sudo gunicorn -c /etc/gunicorn.d/test hello


sudo ln -sf /home/box/web/etc/gunicorn-django.conf.py /etc/gunicorn.d/ask
sudo gunicorn -c /etc/gunicorn.d/ask ask.wsgi