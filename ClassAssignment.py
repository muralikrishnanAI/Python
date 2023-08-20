class Multifunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        List=['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for temp in List:
            print(temp)
    
    def OddEven():
        Num=int(input("Enter the number:"))
        if (Num%2)==1:
            print(Num, end=" is Odd Number")
        else:
            print(Num, end=" is Even Number")
    
    def Elegible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if (Gender=='Male'):
            if(Age >=21):
                print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')
        elif(gender=='Female'):
            if(Age >18):
                print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')
        else:
            print('INVALID INPUT DATA')
            
    def percentage():
        Subject1=int(input("Subject1= "))
        Subject2=int(input("Subject2= "))
        Subject3=int(input("Subject3= "))
        Subject4=int(input("Subject4= "))
        Subject5=int(input("Subject5= "))
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        Percentage=(Total/500)*100
        print("Total= ",Total)
        print("Percentage= ",Percentage)
        
    def triangle():
        Height=int(input("Height= "))
        Breadth=int(input("Breath= "))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:",(Height*Breadth)/2)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",Height1+Height2+Breadth)