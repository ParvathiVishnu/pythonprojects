import os

while True:

    def store_name(file,n):
        try:
            with open(file,'a') as g:
                g.write(f'{n}\n')
        except IOError:
            print("Error could not create file",file)
  
    def retrieve_name(file):
        try:
            with open(file,'r') as f:
                content = f.read()
                print(content)

        except IOError:
            print("Error could not read file",file)
    def remove_name(file):
        try:
            with open(file,'r') as f:
                content = f.readlines()
                rname = input("Enter the name ")
                updated_list=[i for i in content if rname not in i]
             
                with open("new_sample.txt",'w') as w :
                    w.writelines(updated_list)
                print(f'{rname} has been successfully deleted from the file')
               
        except IOError:
            print("Error could not read file",file)

    if __name__ == '__main__':

        print('To store and retrieve the full names from a text file')
        print('------------------------------------------------------')

        filename='sample.txt'

        print('''
              1.To store a list of  names
              2.Retrieve the list of  names
              3.Delete a name from the text file
              ''')
        print('')
        i = input("Enter the option : ")
        print('')
        if i == '1':
                fname = input("Enter the first name : ")
                lname = input("Enter the last name : ")
                full_name = fname+' '+lname
                store_name(filename,full_name)
        elif i == '2':
            retrieve_name(filename)
        
        elif i == '3':
            remove_name(filename)
        else:
            print("Invaild option")

    c = input("Do you want to continue y/n : ").lower()
    if c == 'n':
        break
    