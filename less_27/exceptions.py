def process_conf(file_name, conf_line="app1"):
    try:
        with open(file=file_name, mode='r') as f:
            data = f.read()
        print(data)
    except FileNotFoundError:
        print(f"File not found")
        data = conf_line
        with open(file=file_name, mode='w') as f:
            f.write(data)
    else:
        print("Process confs")
        processed = data.upper()
        print(processed)
        return processed
    finally:
        print("Default line")

locations = [
    "MSK",
    "NYC",
    "UNKNOWN",
    "NSK",
]

for location in locations:
    try:
        with open(file=location, mode='r') as loc:
            print(f"Processed location {location}")
    except(FileNotFoundError, PermissionError) as err:
        print(f"Skip {location} with {err}")
        continue

print("All location processed")


res = process_conf("app2.conf")
print(res)
