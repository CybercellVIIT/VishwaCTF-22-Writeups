# Run the Cat
# Auther:- (Ankit Kumar and Sanjivan Pal) 

## Category
Reversing-(medium)

## Question
>My friend sent me some Python code, but something tells me he loves cat. Do you think you can put your reverse engineering skills to use and get it to output the flag?

### Hint(not to be given)
>Just try to debug or brute force.

## Solution


The script cat.py with a lot hard-to-read names, takes a string contains 9 characters as input, CAt takes two strings to output a final one, which should match C20a73t0294t0ac2194.
``
isDigit = str.isdigit
def mulBy3(cat):
    return str(int(cat)*3)

def CAt(cat, cats):
    print(cat, cats)
    cat1 = 0
    cat2 = 0
    catcat = 0
    cAt = ""
    while cat1 < len(cat) and cat2 < len(cats):
        if catcat%3 == 2//4:
            cAt += cats[cat2]
            cat2 += 1
        else:
            cAt += cat[cat1]
            cat1 += 1
        catcat += 1
    return cAt

def reverse(cat):
    return cat[::3-4]

def caT(cat):
    return mulBy3(cat[:3]) + reverse(cat)

def Cat(answer):
    if len(answer) == 9:
        if isDigit(answer[:3]) and isDigit(answer[len(answer)-3+1:]): # answer = ABC-def-GHI Caps are digits
                catcat = CAt(caT(answer), "Cat9"+reverse(answer)[:3]) #Cat9'IHG'
                if catcat == "C20a73t0294t0ac2194":
                    flag = "runner_" + answer
                    print("So here you are!! VishwaCTF{",flag,"}")
                else:
                    print("You are using right format, but answer is not correct\n>>", catcat)
        else:
            print("You are not using correct format :(\
            \n(A small help from out side, Format should be like 123xyz789)")
    else:
        print("Wrong answer, check length :(")

print("What'S tHe aNsWer")
answer = input()
CATCATCAT = 3
CATCATCATCAT = 4
CATCATCATCATCAT = 2
Cat(answer)
``

We know that the expected ouput of CAt, we could reverse calculate to find out the two input strings. The first string, let's say s1, is composed with str(int(eat[:3])*3) and cat[::-1], the first part is number contains three digits, result of multiply 3 could be the 3-digit number or 4-digit number, the second part is reverse of input string, so we could setup two cases, ---_________ and ----_________, placeholder - for digits and _ for letters. The second strings2 is "Cat" + '9' + cat[:3], so the placeholder for s2 is Cat9_________.


catcat = CAt(caT(cat), Rat(rAT(catt(cat))))
if catcat == "C20a73t0294t0ac2194":
      flag = "runner_" + cat
      print("So here you are!! VishwaCTF{",flag,"}")

By adding the part check, there is only one output.
Case1: 691cat420


Input the result from case1 to cat.py the flag is printed.

>>python3 cat.py
What'S tHe aNsWer
691cat420
2073024tac196 Cat9024
So here you are!! VishwaCTF{ runner_691cat420 }


### Flag
VishwaCTF{ runner_691cat420 }
