# micropython-dashboard

# Micropython Config
## `wifi_config.json`
```
{
    "essid": "<wifi essid>",
    "password": "<wifi password>",
    "static": {
        "ip": "<IP address>",
        "subnet": "<netmask, e.g. 255.255.255.0>",
        "gateway": "<gateway>",
        "dns": "<dns>"
    }
}
```

## `server_config.json`
```
{
    "Authorization": "<server password>"
}
```

# Server library
- https://github.com/jczic/MicroWebSrv
- https://github.com/jczic/MicroWebSrv2