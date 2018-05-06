start_list = [5, 3, 1, 2, 4]
square_list = []
# Your code here!

for item in start_list:
  contain = item ** 2 #sqr and save the value in a variable
  square_list.append(contain)#append the value to the new list
  square_list.sort()
print square_list