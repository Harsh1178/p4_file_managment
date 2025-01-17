import os
print("FILE MANGMENT APP")
def file(cs):
    match cs:
        case 1:
            print("You requested to create the file")
            a=input("Enter the file name to be created")
            if not os.path.exists(a):
                with open(a,"w") as f:
                    f.write("")
                    print(f"File {a} successfully created")
                
            else:
                print("File already exists")
                file(1)
                
                

        case 2:
            print("You requested to update file")
            g=os.listdir()
            print("Files in directries are :")
            o=1
            for i in g:
                print(f"{o}.",i)
                o+=1
            k=input("Enter the file name to update")
            if os.path.exists(k):
                with open(k,"w") as f:
                    c=input("Enter the new content :")
                    f.write(c)
                print(f"Successfully updated file {k}")
                
            else:
                print("The file does not exists")
                print("Enter a existing file")
                file(2)
        case 3:
            print("You requested to edit the file")
            g=os.listdir()
            print("Files in directries are :")
            c=1
            for i in g:
                print(f"{c}.",i)
                c+=1
            k=input("Enter the file name to edit")
            if os.path.exists(k):
                with open(k,"r") as f:
                    d=f.read()
                    r=input("Enter the word to be replaced")
                    rn=input("Enter the replacing word")
                    dn=d.replace(r,rn)
                with open(k,"w") as f:
                    f.write(dn)
                print(f"Successfully edited file {k}")
                
            else:
                print("File does not exists")
                print("Enter a existing file")
                file(3)

        case 4:
            
            k=input("Enter the file to be removed")
            
            if os.path.exists(k):
                os.remove(k)
                print(f"Successfully removed file {k}")
                
            else:
                print("File does not exists")
                print("Enter a existing file")
                file(4)
def main():
    print("Enter the number you need to perform actions on file")
    print("1 : Create a file")
    print("2 : update a file")
    print("3 : edit a file")
    print("4 : remove a file")
    print()
    valid_integers=[1,2,3,4]

    
    while True:
        try:
            user_input = int(input(f"Enter a number from {valid_integers}: "))
            if user_input in valid_integers:
                file(user_input)
                
        
            else:
                print(f"Invalid input! Please choose one of the following: {valid_integers}")
                
            # break
        except ValueError:
            print("Invalid input! Please enter an integer.")
        finally:
            break
        
    
main()

        
    
    
        
        
