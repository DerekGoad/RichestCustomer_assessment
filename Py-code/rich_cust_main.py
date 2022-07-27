'''
Created on Jul 27, 2022

@author: DerekG
'''



#v----------------------functions!!!--------------------------------v
#this will find the index of the wealthiest customer
def customer_wealth_picker(clist):
    _clist = clist
        
    #finds the max() in array
    maxC = max(_clist)
    
    #if the value of maxC is in the array. then grab the array index
    if maxC in _clist:
        maxIndex = clist.index(maxC)
    
    return maxIndex
    
    
#this prints the wealth of the accounts for each customer  
def list_all_customers(clist):
    _clist = clist
    
    #-- for each customer, display their wealth
    iterator = 0;
    for val in _clist:
        iterator += 1;
        print(f'{make_ordinal(iterator)} customer has a wealth = {sum(val)}')

    return 


#this reformats numbers with the appropraiate readable suffix (1 -> 1st, 2 -> 2nd, etc)
def make_ordinal(n):
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

#^----------------------functions!!!--------------------------------^







#v-----------------START PROGRAM---------------------------------------------v

#this is the given list of accounts to go through
clist = [[5,2],[9,8],[7,6]]
print(f'clist: {clist}\n')


#run a couple of functions for math
richest_customer_i = customer_wealth_picker(clist)
list_all_customers(clist)


#print the ordininal (the +1 is so we don't have 0st), and the sum of the clist where the index is the richest customer 
print(f'the {make_ordinal(richest_customer_i+1)} customer is the richest with a wealth of {sum(clist[richest_customer_i])}\n')


input('press enter to exit... ')
quit()
