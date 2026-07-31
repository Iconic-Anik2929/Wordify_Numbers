# Wordify_Numbers
num=input("Enter number: ").strip()
ones=["", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"]
tens=["", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"]
s= ["", "Thousand", "Lakh", "Crore"]
if num == "0":
    print("zero")
else:
    r= []
    l= int(num[-3:]) if len(num) >= 3 else int(num)
    num = num[:-3]
    word = ""
    n = l
    if n >= 100:
        word += ones[n // 100] + " hundred "
        n %= 100
    if n >= 20: 
        word += tens[n // 10] + " "
        n %= 10
    if n > 0:
        word += ones[n] + " "
    r.append(word.strip())
    _= 1
    while num:
        group = int(num[-2:])
        num = num[:-2]
        if group != 0:
            word = ""
            n = group
            if n >= 20:
                word += tens[n // 10] + " "
                n %= 10
            if n > 0:
                word += ones[n] + " "
            if _< len(s):
                word += s[_] + " "
            else:
                word += "10^" + str(_*2+1) + " "
            r.append(word.strip())
        _+= 1
    if word == '':
        print('zero')    
    else:
        print(" ".join(reversed(r)).strip())
