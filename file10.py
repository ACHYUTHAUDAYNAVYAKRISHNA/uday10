# 21-03-24.

#1) Tasks
#d1 = {"shirt": 1000,"pant": 1500, "shoes":"900","handkey":30}
#1) find the min ans max priced product
#2) find the product starts with 's' and 's'



#2) find the n =67,is strong number or not


#3) l1 = [1,2,3,4,5,6]
# n=2--->[5,6,1,2,3,4]
# n=3--->[4,5,6,1,2,3]



# Method riding
#*polymorphism in classes using inheritance


    ### Eg : 1
'''
class bank:
    def ratio(self):
        print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()


s = SBI()
s.ratio()
'''

### Eg : 2
'''
class USA:
    def language(self):
        print("English")
    def capital(self):
        print("washington DC")
class India(USA):
    def language(self):
        print("None")
        
    def capital(self):
        print("New deelhi")


I = India()
I.language()
I.capital()
'''

### Eg : 3
'''
class c1:
    def f1(self):
        print("class 1")
    

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj2 = c1()


def display(a):
    a.f1()

display(obj1)
display(obj2)

# polymorphism using objects

#c1,c2---c1 = print(c1),print(c2)
#f1,f2
'''
### Eg : 4

'''
class c1:
    def f1(self):
        print("class 1")
    

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj2 = c1()


def display(a):
    a.f1()

display(obj1)
display(obj2)

'''


#changing the functionality of builtin functions
'''
class shooping:
    def item_list(self,l1):
        items = len(l1)
        self.items = l1

    def __len__(self):
        length = len(self.items)
        return length

s =  shooping([1,2,3,4,5])
print(len(s))
'''

'''
a = 9
b = 6
#print(a+b)
print(a.__add__(b))   ## dunder method or mafic method
'''

#int()
'''
a = 9
b = 6
print(a.__sub__(b))
'''

# Method overloading.
#   Eg : 1
'''
class suming:
    def add(self, a, b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)

s = suming()
s.add(4,3)
s.add(4,5,1)
'''


# Eg : 2
class suming:
    def add(self, a=None, b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b)
        else:
            print(a)

obj= suming()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)



















