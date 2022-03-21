
## Stock Bot

![img](https://i.ibb.co/TPcg0PG/Screenshot-from-2022-03-21-16-21-30.png)

## Solution:

This challenge includes LFI (Local File Inclusion) vulnerability. It fetch the data related to stock available of particular product. Also the location where the flag is present is given in the script as comment. There might be other ways to get the flag but I am injecting payload in the URL which looks like URL given below.

```
https://st0ck-b0t.vishwactf.com/Products/check.php?product=file:///opt/app-root/src/Products/Flag
```

### Output

![img](https://i.ibb.co/HP59t4p/image1.png)
