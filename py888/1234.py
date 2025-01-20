#try:
    #f = open('water01.txt','a')
    #try:
        #f.write('hello')
        #f.write("\n")
    #except:
        #print('เขียนไฟล์ไม่ได้')
    #finally:
       # f.close()
#except:
    #print('เปิกไฟล์ไม่ได้')
    
x = 10
if not type(x) is int:
    raise TypeError('only integers are allowed')
else:
    print('True')