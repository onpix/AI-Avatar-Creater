#!/usr/bin/bash
NGROK_BASE_DOMAIN="avatarmaker.dns-cloud.net"

# Generate new ssl
openssl genrsa -out base.key 2048

openssl req -new -x509 -nodes -key base.key -days 10000 -subj "/CN=$NGROK_BASE_DOMAIN" -out base.pem

openssl genrsa -out server.key 2048

openssl req -new -key server.key -subj "/CN=$NGROK_BASE_DOMAIN" -out server.csr

openssl x509 -req -in server.csr -CA base.pem -CAkey base.key -CAcreateserial -days 10000 -out server.crt
