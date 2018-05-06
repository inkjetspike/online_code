#def repeat_str(repeat, string):
 #   counter = 0
  #  new_string = ''
   # while counter < repeat:
    #    new_string = new_string + string
     #   counter = counter + 1
    #return new_string



# repeat is 5
# counter (0) is less than repeat (5)
# add string to new_string
# 'cat' + '' = 'cat' // counter == 1
# 'cat' + 'cat' = 'catcat' // counter == 2
#def invert(lst):
 #   new_lst = []
  #  for item in lst:
   #     new_lst.append(item * -1)
    #print(new_lst)
    #return new_lst

#invert([1,2,3,4,5]def find_multiples(integer, limit):


#This is the "Find Multiples of a number" problem
#My attempt
#def find_multiples(integer, limit):
#    end = False
#    product = 0
#    x = 1
#   lst = []
#    while end == False:
#        product = x * integer
#        lst.append(product)
#        if product >= limit:
#            end = True
#        else:
#            x += 1

#    print(lst)
#find_multiples(5,25)

#Code on the Internet
#def find_multiples(integer, limit):
#    return range(integer,limit+1,integer)
 #or
#def find_multiples(m, n): return [m * (i + 1) for i in range(n / m)]


#def create_array(n):
#    res = []
#    i = 1
#    while i <= n:
#        res += [i]
#        i += 1

#    return (res)


#create_array(5)



