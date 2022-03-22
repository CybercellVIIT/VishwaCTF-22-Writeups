## Keep Your Secrets

![img](https://i.imgur.com/C3CWimb.png)

## Solution:

This is a simple JWT hacking challenge.We need to generate a JWT token having an admin role instead of having a user.

#

Step 1:

Get the JWT token by making a GET request

![img](https://i.imgur.com/KCgULci.png)

#

Step 2:

Using tools like jwt-cracker, you can easily find out the secret by brute-forcing it. After bruteforcing it you will get the secret(owasp).

#

Step 3:

Go to [JWT.io](https://jwt.io), change role from 'user' to 'admin' and enter your secret. After doing this make sure you copy your newly forged token.

#

Step 4:

Using Postman(or any other tool for that matter) make a post request on `/api/login/user` and put your token in header as 'token'.

![img](https://i.imgur.com/8M9sO8i.png)

and from here you get the Flag.

`vishwactf{w3@k_$ecr3t$}`
