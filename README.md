# Cashew
Prototype of Functions for Instagram Automation

Cashew is an open source collection of scripts to help Instagram Managers / Community Managers to have automated functions acros the platform.

#### Requirements

1. Python 3
1. MySQL / MyISAM Engine
1. async-generator==1.10
1. attrs==21.4.0
1. certifi==2021.10.8
1. cffi==1.15.0
1. charset-normalizer==2.0.12
1. cryptography==37.0.2
1. h11==0.13.0
1. idna==3.3
1. mysql-connector==2.2.9
1. outcome==1.1.0
1. pycparser==2.21
1. pyOpenSSL==22.0.0
1. PySocks==1.7.1
1. requests==2.27.1
1. selenium==4.1.5
1. sniffio==1.2.0
1. sortedcontainers==2.4.0
1. trio==0.20.0
1. trio-websocket==0.9.2
1. urllib3==1.26.9
1. webdriver-manager==3.5.4
1. wsproto==1.1.0

Once you have Python 3, pip3 and MySQL installed in your computer, make sure you create a virtual environment for the project and install requiriments.txt using pip3.

You will also need to create a MySQL database with the tables that contain in the file `mysql_tables.sql`.

And finaly create a file called `config.py` with the variables below:

##### MySQL Configurations

host = "localhost"

database = "your-database"

myuser = "your-user"

mypass = "your-password"