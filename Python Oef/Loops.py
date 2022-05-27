#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
from traceback import print_tb


picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

outside = 0;
inside = 0;

for i in picture:
  for item in i:
    if item == 0:
      print(" ", end='')
    else:
      print("*", end='')
  print("")
  

# Exercise  
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

length = len(some_list)
i = 1
for one in some_list:
  for second in some_list[i:length]:
    if second == one:
      print(one);
      some_list.remove(one)
      print(some_list)
  i += 1;
  

# exericise
def checkDriverAge(age=0):
    
  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(20)


def Chris_Function():
  is_chris_coming = False
  
  if is_chris_coming == False:
    print("Lekker en jy jou nar kop.")
  else:
    print("Wat the ou")
    
Chris_Function()

# Exercise 
def highest_even(nums):
      high = 0;

      for item in nums:
        if(item %2 == 0 and item > high):
          high = item;
  
      if high == 0:
        return "there where no even numbers";
  
      return high;

nums = []
print(highest_even(nums))