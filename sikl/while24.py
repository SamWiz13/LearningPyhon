n = int(input("n ="))
f0 =0; f1 =1; fi =0
while fi< n:
    fi =f0 +f1
    f0 =f1
    f1 =fi
if  fi ==n:
    print("Fibonanchi soni ")
else:
    print("Fibonanchi soni emas")