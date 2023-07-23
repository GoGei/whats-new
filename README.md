# whats-new
## Pet project to create website that provide news

# Installation
## Requirements
* Python 3.8
* PostgreSQL 12
* Redis

## Local setup
### clone
```bash
git clone git@github.com:GoGei/whats-new.git
```
### Add hosts
* Ubuntu: /etc/hosts
* Windows: c:\Windows\System32\Drivers\etc\hosts
* MacOS: /private/etc/hosts
```bash
127.0.0.1           whats-new.local
127.0.0.1       api.whats-new.local
127.0.0.1     admin.whats-new.local
```

### Add database
```postgresql
CREATE USER whatsnew WITH ENCRYPTED PASSWORD 'whatsnew-password' SUPERUSER CREATEDB;
CREATE DATABASE whatsnew WITH OWNER whatsnew ENCODING 'UTF8';
```

### Setup environment
Create virtual environment
```bash
cd whats-new/
python3.8 -m venv env
source env/bin/activate
pip install -r requirements.txt
./manage.py migrate
```

Copy settings
```bash
cp config/settings_example.py config/settings.py
```
