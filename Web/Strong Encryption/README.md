
## Strong Encryption

![img](https://i.ibb.co/WBjQCMS/image.png)

## Solution:

In this challenge you have given a Flag which is encrypted by the encrypt function as you can see in the given PHP code. You have two ways to solve this challenge. Either you can manually reverse the encryption logic or you can write a code to do that.

## Decrypt.php
```php

function decrypt($str,$uenKey){

    $enKeyHash='';
    $strHex='';
    $Key='';
    $tmpKey='';
    $decTxt='';

    for($i=strlen($str)-64;$i<strlen($str);$i++){
        $enKeyHash.=$str[$i];
    }    

    $rKeyHex=$str[-66].$str[-65];
    $rKey=hexdec($rKeyHex);

    for($i=0;$i<strlen($str)-66;$i++){
        $strHex.=$str[$i];
    }  

    for($i=0;$i<strlen($uenKey);$i++){
        $Key.=ord($uenKey[$i])+$rKey;
        $tmpKey.=chr(ord($uenKey[$i])+$rKey);
    } 
    
    for ($i=0, $j=0; $i < strlen($str)-66; $i+=2, $j++){
        if($j==strlen($Key)){
                $j=0;
        }    
          $decTxt.=chr(hexdec($str[$i].$str[$i+1])-$Key[$j]);
    }
    return $decTxt;
  
}

$encTxt="576e78697e65445c4a7c8033766770357c3960377460357360703a6f6982452f12f4712f4c769a75b33cb995fa169056168939a8b0b28eafe0d724f18dc4a7";
$decTxt = decrypt($encTxt, "VishwaCTF");
echo $decTxt;

```


## Output:

VishwaCTF{y0u_h4v3_4n_0p_m1nd} 
