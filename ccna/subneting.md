## Rango de direcciones privadas
El organismo Internet Assigned Numbers Authority (IANA) asignó varios rangos de direcciones que no son asignables a internet. Solo trabajan en redes privadas.

Las primeras y últimas IP son reservadas

n.n.n.255 -> broadcast

||Range|Subnet Mask|
|---|---|---|
|A|10.0.0.0 - 10.255.255.255|255.0.0.0|
|Selftest|127.0.0.0|Loopback addresses|
|B|172.16.0.0 - 172.31.255.255|255.240.0.0|
|C|192.168.0.0 - 192.168.255.255|255.255.0.0|
|D|224.0.0.0 - 239.255.255|Multicast|
|E|240.0.0.0 - 255.255.255.255|Experimental|