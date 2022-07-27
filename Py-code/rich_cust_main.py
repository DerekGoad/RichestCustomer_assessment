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


#----------------------------------------------------------------------------------------------------
#    this is for the questions in the assessment 

#    1.    What is the difference between rebasing and merging in source control?
#    Rebasing and Merging server very similar purposes, they both contribute to the brances in the project
#    Rebasing makes commits easier to track by rewinding the main branch pulling from main and adding the commits together
#    Merging is simple only requiring the commit changes to be added to the main branch, typically harder to track changes, more interwoven

#    2.    How do you approach solving merge conflicts? 
#    This is something that has to be done manually, there are tools (like git diff / difftool) that will give   
#    a visual comparison to aid in deciding which commit shall win over the other, 
#    This is at the discretion of the developer reviewing the conflict.The file will need to be manually edited/reviewed then committed
#----------------------------------------------------------------------------------------------------