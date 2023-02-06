
## Install the Flask Dependencies

```bash
pip install -r requirements.txt
```

## Creating the tables and database

```sql
CREATE DATABASE IF NOT EXISTS `flask_app_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `flask_app_db`;

DROP TABLE IF EXISTS `users`;

CREATE TABLE IF NOT EXISTS `users` (
	`user_id` int(11) NOT NULL AUTO_INCREMENT,
  	`first_name` varchar(50) NOT NULL,
  	`last_name` varchar(50) NOT NULL,
  	`email` varchar(100) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`admin` BOOLEAN NOT NULL DEFAULT false,
  	`created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  	`updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
    
INSERT INTO `users` (`first_name`, `last_name`, `email`, `password`, `admin`) 
    VALUES ('Admin', '', 'admin@flaskapp.com', 'admin', true);
```

## Update the configuration (config.py)

According to your database update the below properties.

```shell
DEBUG = True
SECRET_KEY = 'rangareddy-flask-app'
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DB = 'flask_app_db'
MYSQL_PORT = 3306
```

## Run the Application

```bash
python main.py
```

## References

1. https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html