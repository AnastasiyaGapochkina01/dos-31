#!/bin/bash

# ---> PARAMS <---
CONFIG_NAME="dvps-lessons"
LISTEN_PORT=80
SERVER_NAME="devops.less.fun"
SERVICE_NAME="devops.less.fun"
SSL_ENABLED=false
UPSTREAM_SERVER="localhost:5000"

declare -a LOCATIONS=(
  "api|api:8001"
	"lessons|localhost:8000"
)

TMPL="nginx_conf.tmpl"
CONF_NAME="dvps_less.conf"

template=$(cat $TMPL)

template=${template//config_name/$CONFIG_NAME}
template=${template//listen_port/$LISTEN_PORT}
template=${template//server_name/$SERVER_NAME}
template=${template//service_name/$SERVICE_NAME}
template=${template//upstream_server/$UPSTREAM_SERVER}


if [[ "$SSL_ENABLED" == false ]]; then
  template=$(echo "$template" | sed '/# BEGIN SSL BLOCK/,/# END SSL BLOCK/d')
else
  template=${template//{{ ssl_cert_path }}/${SSL_CERT_PATH}}
  template=${template//{{ ssl_key_path }}/${SSL_KEY_PATH}}
fi

locations_block=""
for location in "${LOCATIONS[@]}"; do
  FS='|' read -r path backend <<< "$location"
  locations_block+="    location $path {\n        proxy_pass http://$backend;\n    }\n"
done

template=$(echo "$template" | sed '/# BEGIN ADDITIONAL LOCATIONS/,/# END ADDITIONAL LOCATIONS/c\'"$locations_block")

echo "$template" > "$CONF_NAME"