log_line = "2025-12-27 ERROR [db] Connection to db01:5432 refused"
items = log_line.split()
print(items)
severity = input("Enter log_level: ")
if severity.upper() in items:
    print(f"{severity} found")

envs = """
APP_IMG=anestesia01/tag
DB_HOST=postgres
DB_USER=appuser
"""
prod_envs = envs.replace("tag", "prod:latest")
print(prod_envs)

registry = "anestesia01"
app_name = "simple-app"
version = "v.1.0.2"
creds = "1234"


config = f"""
APP_IMG={registry}/{app_name}:{version}
PASS={creds}

"""

print(config)