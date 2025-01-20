drink_1 = str(input("If u wanna to drink? (Y|N): "))
if drink_1 == 'y':
    f = open("water01.txt","r")
    print(f.read())
    water_add = str(input('What do u want add option?: '))
    
    if water_add == 'y':
        water_add_1 = str(input("Tell me : "))
        f = open("water01.txt","a")
        f.write(f'\n{water_add_1}')
        f.close()
        f = open("water01.txt","r")
        print(f.read())
        f.close()
        print("bye !!!")
    else:
        print("bye !!!")
        
else:
    a1 = str(input("can u tell me why u dont want?: "))  
    f = open("abc","w")
    f.write(f'{a1}')
    f.close()
