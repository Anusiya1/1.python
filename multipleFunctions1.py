class Functions():

    def BMI():
      BMI=int(input("Enter the BMI:"))
      if(BMI<18.5):
        print("underweight")
      elif(BMI<25):
        print("nomal")
      elif(BMI<30):
        print("over weight")
      else:
        print("very over weight")


    def AgeCategory():
      a=input("Enter the Gender:")
      age=int(input("Enter the Age:"))
      if(a=="male"and age<20):
        print(" ELIGIBLE")
        Cate=" ELIGIBLE"
      elif(a=="female" and age<25):
        print(" ELIGIBLE")
        Cate=" ELIGIBLE" 
      else:
        print("NOT ELIGIBLE")
        Cate="NOT ELIGIBLE"

   
    def OddEven():
      num=int(input("Enter a number:"))
      if((num%2) == 0):
         print(num,"is Even number")
         message=num,"is Even number"
      else:
         print(num,"is Odd number")
         message=num,"is Odd number"
      return message  

    def percentage():
        add=int(input("Enter the Totel:"))
        a=add
        b=500
        division=add/500*100
        print(division)


    def PerameterofTriangle():
        num=int(input("Perameter of Triangle:"))
        addition=3+4+45
        return addition

    def addition(Height1,Height2,Breadth):
        addition=(Height1+Height2+Breadth)
        return addition
       

   
       
           




           