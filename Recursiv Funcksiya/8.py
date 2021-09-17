def RootK(X,K,N):
    if N==0:
        return 1
    else:
        return RootK(X,K,N-1) - (RootK(X,K,N-1) - X/RootK(X,K,N-1)**(K-1))/K
print(RootK(int(input('X = ')),int(input('K = ')),int(input('N = '))))

