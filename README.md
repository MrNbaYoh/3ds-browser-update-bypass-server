# 3DS Browser Update Bypass
 This server can be used with [SSLoth](https://github.com/MrNbaYoh/3ds-ssloth) to spoof the `cbvc.cdn.nintendo.net` endpoint and bypass the browser update check that prevents using the browsers on firmware versions < 11.14.

 ## Public server

 A public server is available. To bypass the update check, you need to edit your 3DS network settings and set your DNS to `54.38.133.70`.


 ## How does it work?

 When you open the browsers, they send a GET request to `cbvc.cdn.nintendo.net` to check whether an update is available or not. If the response is not `0` (usually they reply with `99999` when an update is needed), the browser pops a message up saying you need to update. With [SSLoth](https://github.com/MrNbaYoh/3ds-ssloth) we can spoof the server and always send `0` as a response. Thus, we bypass the update requirement.
