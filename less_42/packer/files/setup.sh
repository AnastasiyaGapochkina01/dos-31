#!/bin/bash

timedatectl set-timezone Europe/Moscow

apt-add-repository -y universe
apt-add-repository -y main
apt-add-repository -y restricted
apt-add-repository -y multivers

apt-get update
DEBIAN_FRONTEND=noninteractive \
SUDO_FORCE_REMOVE=yes \
apt-get install -y \
  atop
  git \
  gnupg2 \
  iftop \
  iotop \
  jq \
  screen

useradd -G root -s /bin/bash -m ansible
cp -r home/ansible/.ssh /home/ssh
chown -R ansible:ansible /home/ansible
chmod 700 /home/ansible/.ssh
chmod 600 /home/ansible/.ssh/*
cp etc/sudoers.d/ansible /etc/sudoers.d