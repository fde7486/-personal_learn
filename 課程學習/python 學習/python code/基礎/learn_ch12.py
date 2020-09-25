"""
class Bank():
    #define a bank
    def __init__(self, n): #建構子
        self.b_name = n
    def motto(self):        
        return (self.b_name + " 以客為尊")
t = Bank("第七銀行")  #定義物件t
print(t.motto())
"""

# class Student():
#     def __init__(self, stid, t, w):
#         self.sid = stid
#         self.tall = t
#         self.weight = w  
#     def setTall(self,t):
#         self.tall = t
#     def setWeight(self,w):
#         self.weight = w
#     def tooFat(self):
#         if Student.BMI(self.tall,self.weight)>25:
#             return True
#         else:
#             return False
#     def BMI(t,w):
#         return (w/(t/100)**2)
# s1 = Student('Nick',170,60)
# print(s1.tooFat())

# """private attribute"""
# def BMI(t, w):
#     bmi = w/((t/100)**2)
#     print ('BMI=', bmi)
#     return (bmi)
# class Student():    
#    def __init__(self, ssid, t, w):
#        self.sid = ssid
#        self.__tall = t #在變數前加"__",使其變成私有變數
#        self.__weight = w              
#    def setWeight(self, w):
#        self.__weight = w       
#    def getTall(self):
#        return self.__tall/100   
#    def setTall(self, t):
#        if (t < 250 and t > 120):
#            self.__tall = t
#        else:
#            print ('Error')    
#    def tooFat(self):
#        if BMI(self.__tall, self.__weight)>25:
#            return True
#        else:
#            return False       
# s1 = Student('S101', 170, 60)       
# print (s1.tooFat())
# s1.weight = 2000
# s1.tooFat()
# s2 = Student('S102', 170, 60)       
# print (s1.tooFat())
# print(s1.getTall())
# s1.tall = 280
# s1.setTall(280)

# def BMI(t, w):
#     bmi = w/((t/100)**2)
#     print ('BMI=', bmi)
#     return (bmi)
# class Student():    
#    def __init__(self, ssid, t, w):
#        self.sid = ssid
#        self.__tall = t
#        self.__weight = w              
#    def setWeight(self, w):
#        self.__weight = w       
#    def getTall(self):
#        return self.__tall/100   
#    def setTall(self, t):
#        if (t < 250 and t > 120):
#            self.__tall = t
#        else:
#            print ('!!!!! Error !!!!!!')    
#    def tooFat(self):
#        if BMI(self.__tall, self.__weight)>25:
#            return True
#        else:
#            return False       
#    def __str__(self):
#        s = '{}, tall = {}, weight = {}. Is he too fat? {}'.format(self.sid,
#             self.__tall, self.__weight, self.tooFat())       
#        return (s)   
#    def __repr__(self):
#        return self.__str__()              
#    tall = property(getTall, setTall)       
# s1 = Student('S101', 170, 60)
# print (s1)

class GradeBook():
    def __init__(self, sid):
       self.__sid = sid
       self.__grade = dict()
    def setScore(self, sub, score):
        if score >= 0 and score <= 100:
            self.__grade[sub] = score
        else:
            print ('!!!!! Error !!!!!') 
    def getScore(self, sub):
        if self.__grade[sub] != None:
            return self.__grade[sub]
        else:
            print ('!!!! no such subject !!!!!')
    def getAverage(self):
        tot = sum(self.__grade.values())
        avg = tot/len(self.__grade.values())
        return avg
    def __str__(self):
        s = 'Student {}'.format(self.__sid)
        for sub, score in self.__grade.items():
            s += '\n {}: {}'.format(sub, score) 
        return (s)
    
    def __repr__(self):
        return self.__str__()

s1 = GradeBook('S101')
s1.setScore('Math', 100)
s1.setScore('Eng', 98)
print (s1.getScore('Math'))
print (s1.getAverage())

print (s1)