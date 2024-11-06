while True :
    num = int(input("\nnter here the length of the fibinocci series :-"));
    a = 0;
    b = 1; 
    print(a,);
    print(b,);
    for i in range(2,num):
        sum = a +b;
        a =b 
        b = sum 
        print(sum ,)
        
    