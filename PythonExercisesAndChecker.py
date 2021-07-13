
import unittest

#### Exercise 1
def exercise_1(x,y):
    if x % 2 == 1:#checks condition of x, odd 
        ex1= [ x - 1 for x in y ] #var uses listcomp to remove 1
        return sum(ex1) 
    if x == 0: #sums list if x = 0
        return sum(y)
    if x % 2 == 0:
        for i in range(len(y)):
            y[i] = y[i] * 2
        return sum(y)
    #doubles elements of y and returns sum


#### Exercise 2
def exercise_2(y):
    a = 1
    if y[0] % 2 == 1:#checks if odd number at the first position of the list
        for x in range(len(y)): #checks through each element full lenght of list
            a = a * (y[x] *2) # multiplies each element of list by 2
        return a       
    if y[2] % 2 == 1:
        for x in range(len(y)):
             y[x] = y[x] / 2
        return sum(y)     
    if y[0] % 2 != 1 and y[2]%2 != 1: #condition checks that it is not equal to the other 2
        for x in range(len(y)):#iterates through entire len of y 
            return(sum(x*x for x in y))#squares elements in y and returns sum
                
#### Exercise 3
def exercise_3(y):
    z =[]
    c = len(y)/2
    ele = 0
    for i in range(int(c)):
        if y[-ele-1] < y[ele]:
            z.append(True)
        else:
            z.append(False)
    print(z)
    return(z)

#### Exercise 4 take 3rd biggest number --- len y < 5 returns biggest len -1 element
def exercise_4(y):
    y.sort() ###orders list low-high
    if not y: ###if list is empty returns none
        return None
    if len(y) < 5: ###
        return y[-2]##returns index posiiton -2
    else:
        return y[-3]##returns index condition -3
        
            
    

#### Exercise 5
def exercise_5(x):
    x = x.lower() #makes sure that all string is lower so capitals wont cause errors
    if x == x[::-1]: #reverse check
         return False
    else:
        return True
     
    

#### Exercise 6
def exercise_6(x):
  Caps = 'MNOPQRSTUVWXYZ' #upper case var to be checked
  nonCaps = 'abdcefghijkl' #lowcase var to be checked
  result = '' #empty answer var to be updated according to condition status

  for letter in x:#iterates through x
    if letter.lower() in nonCaps:#checks if elements in x are in non capitals
      result += letter.lower() #updates result according to findings 

    elif letter.upper() in Caps:#checks if elements in x are capitals
      result += letter.upper()#updates result accordingly
      print(result)
  return result
    

#### Exercise 7
def exercise_7(x):
    myList = [] #append to
    for ele in x:#iterates through string and appends to list
        myList.append(ele)#append statement

    a1 = 0#using var 
    y = 0#functions as a counter
    while y <= (len(x)-1):
        x.sort()#orders list low-high
        temp = x[y]#list index 0
        x.remove(x[y])#removes index 0 from list 
        for u in x:#iterate through x
            if temp in u:
                a2 = 0
                while a2 <=(len(myList)-1):
                    if temp == myList[a2]:
                        a1 = a1 + 1
                        return a2
                    a2 = a2 + 1
        x.append(temp)
        y = y + 1
    if a1 == 0:
        return -1

#### Exercise 8
 
def exercise_8(x):
    return None
    


class TestAssignment1(unittest.TestCase):

#function 1
    def test1_exercise_1(self):
        self.assertTrue(fun_exercise_1(3,[4,2,3]) == 6)

    def test2_exercise_1(self):
        self.assertTrue(fun_exercise_1(2,[2,3,4]) == 18)

    def test3_exercise_1(self):
        self.assertTrue(fun_exercise_1(0,[5,3,2]) == 10)

    def test4_exercise_1(self):
        self.assertTrue(fun_exercise_1(3,[1,1,1]) == 0)

#function 2
    def test1_exercise_2(self):
        self.assertTrue(fun_exercise_2([3, 2, 4]) == 192)

    def test2_exercise_2(self):
        self.assertTrue(fun_exercise_2([6, 2, 3]) == 5.5)

    def test3_exercise_2(self):
        self.assertTrue(fun_exercise_2([6, 5, 4]) == 77)

    def test4_exercise_2(self):
        self.assertTrue(fun_exercise_2([1, 2, 3]) == 48)

#function 3 *****
    def test1_exercise_3(self):
        self.assertTrue(fun_exercise_3([2, 3, 4, 5, 6, 7]) ==[False, False,False])

    def test2_exercise_3(self):
        self.assertTrue(fun_exercise_3([6, 4, 3, 2, 1, 0]) == [True,True,True])

    def test3_exercise_3(self):
        self.assertTrue(fun_exercise_3([6, 5, 4, 2]) == [True, True])

    def test4_exercise_3(self):
        self.assertTrue(fun_exercise_3([1, 2, 3, 4]) == [False, False])

#function 4
    def test1_exercise_4(self):
        self.assertTrue(fun_exercise_4([5, 3, 4, 2 , 6]) == 4)

    def test2_exercise_4(self):
        self.assertTrue(fun_exercise_4([3, 2, 6]) == 3)

    def test3_exercise_4(self):
        self.assertTrue(fun_exercise_4([]) == None)

    def test4_exercise_4(self):
        self.assertTrue(fun_exercise_4([2, 3, 4, 7, 6, 5]) == 5 )

#function 5
    def test1_exercise_5(self):
        self.assertTrue(fun_exercise_5("osso") == False)

    def test2_exercise_5(self):
        self.assertTrue(fun_exercise_5("goat") == True)

    def test3_exercise_5(self):
        self.assertTrue(fun_exercise_5("Mom") == False)

    def test4_exercise_5(self):
        self.assertTrue(fun_exercise_5("boat") == True )

#function 6
    def test1_exercise_6(self):
        self.assertTrue(fun_exercise_6("osso") == "OSSO")

    def test2_exercise_6(self):
        self.assertTrue(fun_exercise_6("goat") == "gOaT")

    def test3_exercise_6(self):
        self.assertTrue(fun_exercise_6("bag") == "bag")

    def test4_exercise_6(self):
        self.assertTrue(fun_exercise_6("boat") == "bOaT" )

#function 7
    def test1_exercise_7(self):
        list1 = ["goat"]
        ptr = fun_exercise_7(list1)
        self.assertTrue(ptr == -1)

    def test2_exercise_7(self):
        list1 = ["soul", "soulmate", "origin"]
        ptr = fun_exercise_7(list1)
        self.assertTrue(ptr == 0)

    def test3_exercise_7(self):
        list1 = ["FASER", "submission", "online", "drive", "frequent"]
        ptr = fun_exercise_7(list1)
        self.assertTrue(ptr == -1)

    def test4_exercise_7(self):
        list1 = ["banana", "applejuice", "kiwi", "strawberry", "apple", "peer"]
        ptr = fun_exercise_7(list1)
        self.assertTrue(ptr == 4)

    #function 8
    def test1_exercise_8(self):
        self.assertTrue(fun_exercise_8("GTTAAA") == "T")


    def test2_exercise_8(self):
        self.assertTrue(fun_exercise_8("unforeseen") == "n")


    def test3_exercise_8(self):
        self.assertTrue(fun_exercise_8("developed") == "d")


    def test4_exercise_8(self):
        self.assertTrue(fun_exercise_8("circumstances") == "s")

if __name__ == '__main__':
    unittest.main()
