## Para instalar
```
apt install python3
pip3 install -r requirements.txt

```

```
cat >/lib/systemd/system/flask.service <<EOL
[Unit]
Description=Flask
[Install]
WantedBy=multi-user.target
[Service]
Type=simple
User=root
PermissionsStartOnly=true
ExecStart=/usr/bin/python3 /root/flask/app.py
Restart=on-failure
TimeoutSec=600
EOL
```

### Reiniciar o daemon

```
systemctl daemon-reload
systemctl start flask
systemctl status flask
```

<hr/>

### Flask Version
Flask 2.0.2
Requests 2.22.0
### Python3 --version
Python 3.10.4
