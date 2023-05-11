T = int(input())

decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          '0','1','2','3','4','5','6','7','8','9','+','/'
          ]

for i in range(T):
    S = list(input())
    L = len(S)

    num_data = []
    for j in range(L):
        num = decode.index(S[j])
        num_bin = str(bin(num)[2:])
        while len(num_bin) <= 5:
            num_bin = '0' + num_bin
        num_data += num_bin

    print("#"+str(i+1)+" ",end="")
    while num_data:
        str_data = ''.join(num_data[0:8])
        data = int(str_data, 2)
        data_chr = chr(data)
        print(data_chr, end="")
        del num_data[0:8]
    print("")




