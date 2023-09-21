s=str(input("строка"))
countsl=0
countdf=0
cnt1=0
reset=0
k=0
d=["а","у","о","ы","э","я","ю","ё","и","е"]
while s[k]!=" ":
    if s[k] in d:
        cnt1=cnt1+1
    k=k+1
for i in range(len(s)):  
    if s[i] in d:
        countsl=countsl+1
    if s[i]==" ":
        if cnt1!=countsl:
            reset=reset+1
        cnt1=countsl
        countsl=0
if i==len(s)-1:
    if cnt1!=countsl:
        reset=reset+1

        
if reset>=1:
    print("Пам парам")
if reset<1:
    print("Парам пам-пам")

    
    
       
