try:
    f=open('sample.txt','r')
    f1=f.readline()
    print("file contains:",f1)
    for line in f:
        print(line,end='')
except FileNotFoundError:
    print("error:the file 'sample.txt' does not exist")
except expection as e:
    print(f"an unexpected error occured:{e}")
    f.close()
