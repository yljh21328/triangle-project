# -*- coding: utf-8 -*-
"""
.. module:: Hello
   :synopsis: A simple module for printing "Hello"
 
.. moduleauthor:: Obama
 
"""
 
def print_hello_with_name(name):
    """This function prints hello with a name
 
    Args:
       name (str):  The name to use.
 
    Returns:
       int.  The return code::
 
          0 -- this always return 0
 
    Raises:
       AttributeError, KeyError
 
    A really simple function. Really!
    
    >>> from Hello import print_hello_with_name
    >>> print_hello_with_name('foo')
    Hello, foo
    0
    """
    print('Hello,', name)
    return 0

def print_hello_with_year(year):
    """This function prints hello with a name
 
    Args:
       name (str):  The name to use.
 
    Returns:
       int.  The return code::
 
          0 -- this always return 0
 
    Raises:
       AttributeError, KeyError
 
    A really simple function. Really!
 
    ::
    
       print_hello_with_year('foo')
       Hello, foo
       0
    """
    print('Hello', year)
    return 0