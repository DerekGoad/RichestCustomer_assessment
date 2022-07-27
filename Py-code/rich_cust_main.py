'''
Created on Jul 27, 2022

@author: DerekG
'''

if __name__ == '__main__':
    pass

def customer_wealth_picker(clist):
    _clist = clist
    
    print('\n-----customer_wealth_picker() Start-----') 
        
    maxC = max(clist)
    if maxC in clist:
        maxIndex = clist.index(maxC)
    
    #-- for each customer, display their wealth
    iterator = 0;
    for val in clist:
        sum(val)
        iterator += 1;
        print(f'{make_ordinal(iterator)} customer has a wealth = {sum(val)}')
        
    #-- print the max wealth and index of the customer
    print(f'the {make_ordinal(maxIndex+1)} customer is the richest with a wealth of {sum(clist[maxIndex])}')
    #print(f'these are their accounts: {clist[maxIndex]}')
    #print('\n------------------------------------------------') 
    
    return _clist
    

def make_ordinal(n):
    '''
    Convert an integer into its ordinal representation::

        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    '''
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix




#-----------------START PROGRAM---------------------------------------------#

clist = [[5,2],[9,8],[7,6]]

print(f'clist: {clist}')
customer_wealth_picker(clist)



input('press enter to exit... ')


quit()