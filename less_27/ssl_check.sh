#!/bin/bash

export $(grep -v '^#' .env | xargs)

send_msg() {
  msg="$1"
  curl -s -X POST "https://api.telegram.org/bot${TG_BOT_TOKEN}/sendMessage" \
    -d chat_id="${TG_CHAT_ID}" \
    -d text="${msg}" > /dev/null
}

FOLDER_ID="b1gdge57rslfb323otnm"

CERTS=$(yc certificate-manager certificate list --folder-id b1gdge57rslfb323otnm --format json)

jq -c '.[]' <<< "$CERTS" | while read -r cert; do
  NAME=$(yc certificate-manager certificate list --folder-id $FOLDER_ID --format json | jq -r '.[] | .name')
  NOT_AFTER=$(yc certificate-manager certificate list --folder-id b1gdge57rslfb323otnm --format json | jq -r '.[] | .not_after')


  EXP_S=$(date -d "$NOT_AFTER" +%s 2>/dev/null || date -d "$NOT_AFTER" +%s)
  NOW_S=$(date +%s)
  DAYS_LEFT=$(( (EXP_S - NOW_S) / 86400 ))

  if (( DAYS_LEFT <= 400 )) ; then
    MSG="🚨 Cert ${NAME} expired in ${DAYS_LEFT}"
    send_msg "$MSG"
  fi
done