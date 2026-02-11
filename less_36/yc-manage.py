#!/usr/bin/python3

import argparse
import os
import json
import requests

YC_TOKEN = os.getenv('YC_TOKEN')
FOLDER_ID = os.getenv('YC_FOLDER_ID')

url = f"https://compute.api.cloud.yandex.net/compute/v1/instances?folderId={FOLDER_ID}"
headers = {
    'Authorization': f"Bearer {YC_TOKEN}",
}

parser = argparse.ArgumentParser(description="YC actions")
parser.add_argument(
    "--action",
    type=str
)
parser.add_argument(
    "--list",
    action='store_true'
)
parser.add_argument(
    "--host",
    type=str
)
parser.add_argument(
    "--get-ip",
    action='store_true',
    help="Get public IP address of the host"
)

args = parser.parse_args()

response = requests.get(url, headers=headers, timeout=10)

if args.list:
    if response.status_code == 200:
        instances = response.json().get('instances', [])
        for instance in instances:
            print(f"NAME: {instance.get('name')} STATE - {instance.get('status')}")

if args.host is not None:
    if response.status_code != 200:
        print(f"API request failed with status {response.status_code}")
        sys.exit(1)

    instances = response.json().get('instances', [])
    target_instance = None

    for instance in instances:
        if instance.get('name') == args.host:
            target_instance = instance
            break

    if not target_instance:
        print(f"Instance '{args.host}' not found")
        sys.exit(1)

    target_id = target_instance.get('id')
    target_name = target_instance.get('name')

    if args.get_ip:
        try:
            network_interface = target_instance.get('networkInterfaces', [{}])[0]
            ipv4_address = network_interface.get('primaryV4Address', {})
            public_ip = ipv4_address.get('oneToOneNat', {}).get('address', None)

            if public_ip:
                print(public_ip)
            else:
                print(f"Instance '{target_name}' has no public IP assigned")
                sys.exit(1)

        except (IndexError, KeyError, TypeError) as e:
            print(f"Error retrieving IP for '{target_name}': {str(e)}")
            sys.exit(1)

    if args.action == "start":
        start_url = f"https://compute.api.cloud.yandex.net/compute/v1/instances/{target_id}:start"
        response = requests.post(start_url, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"Instance {target_name} starting...")
        else:
            print(f"Failed to start instance. Status code: {response.status_code}")

    elif args.action == "stop":
        stop_url = f"https://compute.api.cloud.yandex.net/compute/v1/instances/{target_id}:stop"
        response = requests.post(stop_url, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"Instance {target_name} stopping...")
        else:
            print(f"Failed to stop instance. Status code: {response.status_code}")
