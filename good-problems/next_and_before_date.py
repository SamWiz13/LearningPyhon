#1 kun keyin
D,M,Y=int(input('d=')),int(input('m=')),int(input('y='))
if M==1 and D+1<31: print(D+1,'.',M,'.',Y)
if M==1 and D==31: print('1','.',M+1,'.',Y)
if M==2 and D+1<28: print(D+1,'.',M,'.',Y)
if M==2 and D==28 and Y%100==0 and Y%400==0: print(D+1,'.',M,'.',Y)
if M==2 and D==28 and Y%100!=0 and Y%4==0: print(D+1,'.',M,'.',Y)
if (Y%100!=0 and Y%400!=0 and Y%4!=0) and M==2 and D==28: print('1','.',M+1,'.',Y)
if M==2 and D==29 and (Y%100==0 and Y%400==0 or Y%100!=0 and Y%4==0): print('1','.',M+1,'.',Y)
if M==3 and D+1<31: print(D+1,'.',M,'.',Y)
if M==3 and D==31: print('1','.',M+1,'.',Y)
if M==4 and D+1<30: print(D+1,'.',M,'.',Y)
if M==4 and D==30: print('1','.',M+1,'.',Y)
if M==5 and D+1<31: print(D+1,'.',M,'.',Y)
if M==5 and D==31: print('1','.',M+1,'.',Y)
if M==6 and D+1<30: print(D+1,'.',M,'.',Y)
if M==6 and D==30: print('1','.',M+1,'.',Y)
if M==7 and D+1<31: print(D+1,'.',M,'.',Y)
if M==7 and D==31: print('1','.',M+1,'.',Y)
if M==8 and D+1<31: print(D+1,'.',M,'.',Y)
if M==8 and D==31: print('1','.',M+1,'.',Y)
if M==9 and D+1<30: print(D+1,'.',M,'.',Y)
if M==9 and D==30: print('1','.',M+1,'.',Y)
if M==10 and D+1<31: print(D+1,'.',M,'.',Y)
if M==10 and D==31: print('1','.',M+1,'.',Y)
if M==11 and D+1<30: print(D+1,'.',M,'.',Y)
if M==11 and D==30: print('1','.',M+1,'.',Y)
if M==12 and D+1<31: print(D+1,'.',M,'.',Y)
if M==12 and D==31: print('1','.','1','.',Y+1)
############################################################################################################
#1kun oldin
if M==1 and 31>=D>1: print(D-1,'.',M,'.',Y)
if M==1 and D==1: print('31','.','12','.',Y-1)
if M==2 and 28>D>1: print(D-1,'.',M,'.',Y)
if M==2 and D==29 and Y%100==0 and Y%400==0: print(D-1,'.',M,'.',Y)
if M==2 and D==29 and Y%100!=0 and Y%4==0: print(D-1,'.',M,'.',Y)
if M==2 and D==28: print(D-1,'.',M,'.',Y)
if M==2 and D==1: print('31','.',M-1,'.',Y)
if M==3 and 31>=D>1: print(D-1,'.',M,'.',Y)
if M==3 and D==1 and Y%100==0 and Y%400==0: print('29','.',M-1,'.',Y)
if M==3 and D==1 and Y%100!=0 and Y%4==0: print('29','.',M-1,'.',Y)
if M==3 and D==1 and Y%100!=0 and Y%400!=0 and Y%4!=0: print('28','.',M-1,'.',Y)
if M==4 and 1<D<=30: print(D-1,'.',M,'.',Y)
if M==4 and D==1: print('31','.',M-1,'.',Y)
if M==5 and 1<D<=31: print(D-1,'.',M,'.',Y)
if M==5 and D==1: print('30','.',M-1,'.',Y)
if M==6 and 1<D<=30: print(D-1,'.',M,'.',Y)
if M==6 and D==1: print('31','.',M-1,'.',Y)
if M==7 and 1<D<=31: print(D-1,'.',M,'.',Y)
if M==7 and D==1: print('30','.',M-1,'.',Y)
if M==8 and 1<D<=31: print(D-1,'.',M,'.',Y)
if M==8 and D==1: print('31','.',M-1,'.',Y)
if M==9 and 1<D<=30: print(D-1,'.',M,'.',Y)
if M==9 and D==1: print('31','.',M-1,'.',Y)
if M==10 and 1<D<=31: print(D-1,'.',M,'.',Y)
if M==10 and D==1: print('30','.',M-1,'.',Y)
if M==11 and 1<D<=30: print(D-1,'.',M,'.',Y)
if M==11 and D==1: print('31','.',M-1,'.',Y)
if M==12 and 1<D<=31: print(D-1,'.',M,'.',Y)
if M==12 and D==1: print('30','.',M-1,'.',Y)
