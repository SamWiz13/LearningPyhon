n = int(input("n ="))
f0 =0; f1 =1; fi =0
sana =2
while fi< n:
    fi =f0 +f1
    f0 =f1
    f1 =fi
    sana +=1
if  fi ==n:
 print(sana)
