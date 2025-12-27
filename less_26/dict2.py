hosts_info = {
    "dev-compute-45": {
        "mem": 128,
        "vcpu": 64,
        "location": "NSK",
        "roles": ["frontend", "dev-server"],
        "is_active": True,
        "nets": {
            "priv_ip": "192.168.10.8",
            "pub_ip": "89.169.189.72"
        }
    },
    "prod-compute-1": {
        "mem": 128,
        "vcpu": 64,
        "location": "NSK",
        "roles": ["frontend", "dev-server"],
        "is_active": True,
        "nets": {
            "priv_ip": "192.168.10.8",
            "pub_ip": "89.169.189.72"
        }
    }
}

print(hosts_info["dev-compute-45"].get("location"))