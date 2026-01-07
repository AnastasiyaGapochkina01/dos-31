from jinja2 import Template, Environment, FileSystemLoader

conf_data = {
    "config_name": "dvps-lessons",
    "listen_port": 80,
    "server_name": "devops.less.fun",
    "service_name": "devops.less.fun",
    "ssl_enabled": False,
    "upstream_server": "localhost:5000",
    "locations": [
        {"path": "api", "backend": "api:8001"},
        {"path": "lessons", "backend": "localhost:8000"}
    ]
}

tmpl_name = "nginx.conf.j2"
conf_name = "dvps_less.conf"

env = Environment(loader=FileSystemLoader('.'))
tmpl = env.get_template(tmpl_name)

dvps_less_conf = tmpl.render(**conf_data)
with open(file=conf_name, mode='w') as conf:
    conf.write(dvps_less_conf)

