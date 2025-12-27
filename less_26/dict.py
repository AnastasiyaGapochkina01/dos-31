host_info = {
    "mem": 128,
    "vcpu": 64,
    "hostname": "dev-compute-45",
    "location": "NSK",
    "roles": ["frontend", "dev-server"],
    "is_active": True,
    "nets": {
        "priv_ip": "192.168.10.8",
        "pub_ip": "89.169.189.72"
    }
}

print(host_info)
print(host_info["location"])

if "is_active" in host_info:
    print(host_info["is_active"])

print(host_info.get("locations", "Unknown key"))
host_info["os"] = "Ubuntu 24.04"
host_info["is_active"] = False
print(host_info)

for key in host_info:
    print(f"{key}: {host_info[key]}")
print("\n")

for key,val in host_info.items():
    print(f"{key}: {val}")
#host_info.pop("location")
#print(host_info)