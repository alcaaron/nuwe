sum = 0
for num in range(1,2000000):
    if num > 1:
        cont = 0
        i = 2
        while i < num and cont==0:

            if num%i ==0:
                cont+=1
            i+=1
        
        if cont==0:
            sum+=num
            print(sum)  