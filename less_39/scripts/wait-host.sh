#!/bin/bash
while [ ! -f /var/lib/cloud/instance/boot-finished ]; do
  echo "Waiting for host boot..."
  sleep 1
done
