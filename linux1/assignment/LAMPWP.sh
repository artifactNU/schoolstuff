#!/bin/bash

# Update the package repository and upgrade existing packages
sudo apt update
sudo apt upgrade -y

# Install necessary packages
sudo apt install apache2 ghostscript libapache2-mod-php mysql-server php php-bcmath php-curl php-imagick php-intl php-json php-mbstring php-mysql php-xml php-zip -y

# Configure firewall to allow HTTP traffic
sudo ufw allow in "Apache Full"

# Download and install WordPress
cd /var/www/html || exit 1
sudo wget https://wordpress.org/latest.tar.gz
sudo tar -xzvf latest.tar.gz
sudo mv wordpress/* .
sudo rmdir wordpress
sudo rm latest.tar.gz

# Configure database for WordPress
mysql -u root -p <<MYSQL_SCRIPT
CREATE DATABASE wordpress;
CREATE USER 'wordpress'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress'@'localhost';
FLUSH PRIVILEGES;
MYSQL_SCRIPT

# Configure WordPress
sudo cp wp-config-sample.php wp-config.php
sudo sed -i 's/database_name_here/wordpress/' wp-config.php
sudo sed -i 's/username_here/wordpress/' wp-config.php
sudo sed -i 's/password_here/your_password/' wp-config.php

# Set proper permissions
sudo chown -R www-data:www-data /var/www/html
sudo find /var/www/html/ -type d -exec chmod 755 {} \;
sudo find /var/www/html/ -type f -exec chmod 644 {} \;

# Enable Apache modules and restart
sudo a2enmod rewrite
sudo systemctl restart apache2

# Clean up
sudo apt autoremove -y

# Create a simple WordPress site for testing
echo "<?php phpinfo(); ?>" > /var/www/html/info.php

echo "LAMP stack with WordPress and additional packages is now installed and configured."
echo "You can test your WordPress site by visiting http://your_server_ip/"
