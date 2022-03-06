from mimetypes import init


def lucas_recursion(n):
    """
    The Lucas Numbers are a related series of integers that start with the values 2 
    and 1 rather than 0 and 1.
    n= the number that we need to calculate lucas seris to it 

    

    """
    #base cases
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas_recursion(n-1) + lucas_recursion(n-2)
    
def lucas_loop(n):

    """

        this function to calculate lucas series 
n= the number that we need to calculate lucas seris to it 
    """
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


    

    

def fibonanci(n):
    """
    this function to calculate fibonacci series 

   n= the number that we need to calculate fibonacci seris to it 
    Input : an integer value  nth number in series presume starting at zero 
        4
    Output: fibonanci(4)  -->         fibonanci(3)          +  fibonanci(2)
                          --> (fibonanci(2) + fibonanci(1)) +  fibonanci(2)
                          -->  ( 1          +      1      ) +     1
  
        0,1,1,2
     
    Input  : n = 2
    Output : 1

    Input  : n = 9
    Output : 34
    """                  
    if n<=1:
        return n
    else:
        return (fibonanci(n-1)+fibonanci(n-2))
      


def sum_series(n, n2=0 ,n3=1) :
    """
    this function to calculate any  series where 
    n = the number of terms in the  seris. 
    n2 ==> the index number 1 for this series 
    n3 ==> the index number 2 for this series 
"""   

    #  the base
        # if n2 == 0 and n3 == 1 :
    if n <=0 : 
         return 'plese the number must more than 0'
    elif n == 1 :
         return n2 
    elif n ==2 :
         return n3
    else :
         return sum_series(n-1,n2,n3) + sum_series(n-2,n2,n3)