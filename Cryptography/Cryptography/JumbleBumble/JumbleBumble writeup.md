Title: JumbleBumble

Flag: VishwaCTF{c4yp70gr2phy_1s_n07_e25y}

The  ciphertext is short and e=4 is also small. Brute Forcing c + k *n for each positive integer k. Getting the perfect root which is just the plaintext we can find the flag.

```
from Crypto.Util.number import inverse, long_to_bytes
from sympy import integer_nthroot


file = open("output.txt", "rb")

while True:
    n = int(file.readline().strip())
    c = int(file.readline().strip())
    dis = file.readline()
    while True:
        ans = integer_nthroot(c, 4)
        if ans[1]:
            m = ans[0]
            break

    plaintext = long_to_bytes(m).decode()
    print(plaintext)

```