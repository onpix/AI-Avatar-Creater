#!/usr/bin/sh

./ngrokd -tlsKey=server.key -tlsCrt=server.crt -domain="avatarmaker.dns-cloud.net" -httpAddr=":80" -httpsAddr=":443" -tunnelAddr=":23333"
