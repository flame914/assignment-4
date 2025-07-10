try:
    x=input("Enter text to write to the file: ")
    f=open("output.txt","w")
    f1=f.write(x)
    print("data written succesfully.")

    y=input("enter additional text to append: ")
    f=open("output.txt","a")
    f1=f.write("\n" + y)
    print("data appended succesfully.")

    print("\nfinal content of output.txt: ")
    print("-------")
    f=open("output.txt",'r')
    f1=f.read()
    print(f1)

except IOError as e:
    print(f"file opperation error: {e}")
except Exception as e:
    print(f"an unexpected error occured : {e}")
       
