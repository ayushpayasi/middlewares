class NumberSystem:

    # returns list of boolean value and nearest divisible number  
    def divisible(self, number, value, alldata=False):
        rem = value % number
        quotient = value/number
        if number/2 <= rem:
            nearestDivisible = value - rem
        else:
            nearestDivisible = value + rem
        # alldata true return list
        if alldata == True:
            return [quotient,rem,nearestDivisible, value % number == 0]
        # alldata false return boolean
        else:
            return value % number == 0
    
    #gets list as input 
    def gcd(self,a):
        result = a[0]
        for i in a[1:]:
            while i > 0:
                    result, i = i, result % i
            result = result
        return result        


    def lcm(self, x, y):  
        if x > y:  
            greater = x  
        else:  
            greater = y  
        while(True):  
            if((greater % x == 0) and (greater % y == 0)):  
                lcm = greater  
                break  
            greater += 1  
        return lcm  

# print(result)

class train():

    def ms_to_kmhr(self,value):
        constant = 18/5
        return value *constant
    
    def kmhr_to_ms(self,value):
        constant = 5/18
        return value*constant

    def 

        
