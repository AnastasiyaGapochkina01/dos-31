#!/bin/bash
sudo apt-get update -y
sudo apt-get install -y nginx
echo "Hello from $(hostname)" | sudo tee /var/www/html/index.html
sudo systemctl enable nginx
│sudo systemctl restart nginx