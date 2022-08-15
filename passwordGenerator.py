import random;

def passBinder():
    finalPass = []

    coverted=[]
    
    for i in range(0,2):
        upperCase = random.randint(65,90)
       
        lowerCase = random.randint(97,122)
        
        specialChar = random.randint(33,47)
       
        number = random.randint(48,57)
       
        password = [upperCase , lowerCase , specialChar , number]
        
        finalPass.append(password)
    
    for i in finalPass:
        for j in i:
            coverted.append(chr(j))

      



    return ''.join(coverted)
   






print(passBinder())

