def fizzbuzz(num):
    for x in range(1, num):
        if x%3 ==0 and x%5==0:
            print('fizzbuzz')
        elif x%3==0:
            print('buzz')
        elif x%5 ==0:
            print('buzz')
        else:
            print(x)

fizzbuzz(55)