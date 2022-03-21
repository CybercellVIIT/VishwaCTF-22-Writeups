
## Request Me FLAG

![img](https://i.ibb.co/17qwNqG/image.png)

## Solution:

The challenge name itself contains the hint. `Request Me FLAG` means just change Request method `GET` to `FLAG` using burpsuite or curl.

```
$ curl -I https://r3qu35t-m3-fl4g.vishwactf.com -X FLAG
```
```
HTTP/1.1 200 OK
date: Mon, 21 Mar 2022 09:55:32 GMT
server: Apache/2.4.37 (Red Hat Enterprise Linux) OpenSSL/1.1.1k
flag: VishwaCTF{404_1s_ju57_4n_i11u5ion}
content-length: 0
content-type: text/html; charset=UTF-8
```
