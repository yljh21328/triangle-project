=============================================
 Example: guide.rst — The trianglelib guide
=============================================

Whether you need to test the properties of triangles,
or learn their dimensions, trianglelib does it all!

Special triangles
-----------------

There are two special kinds of triangle
for which trianglelib offers special support.

*Equilateral triangle*
   All three sides are of equal length.

*Isosceles triangle*
   Has at least two sides that are of equal length.

These are supported both by simple methods
that are available in the trianglelib.utils module,
and also by a pair of methods of the main
Triangle class itself.

Triangle dimensions
-------------------

Here is a block quote:

    This is normal text. But we show code too::

       This is code because of the precedind "::"

    But this is normal text because I'm back at the
    level of indentation of the paragrash that
    *started* the block quote.

This is code::

   a + b
   #comment
   #beneath

The library can compute triangle perimeter, area,
and can also compare two triangles for equality.
Note that it does not matter which side you start with,
so long as two triangles have the same three sides in the same order!



.. testcode::

   print("hi!")

.. testoutput::

   hi there!


>>> 3 + 3
6

>>> from trianglelib.shape import Triangle
>>> t1 = Triangle(3, 4, 5)
>>> t2 = Triangle(4, 5, 3)
>>> t3 = Triangle(3, 4, 6)
>>> print(t1 == t2)
True
>>> print(t1 == t3)
False
>>> print(t1.area())
6.0
>>> print(t1.scale(2.0).area())
24.0

Valid triangles

Many combinations of three numbers cannot be the sides of a triangle.
Even if all three numbers are positive instead of negative or zero,
one of the numbers can still be so large
that the shorter two sides
could not actually meet to make a closed figure.
If c is the longest side, then a triangle is only possible if:

a + b > c

While the documentation
for each function in the utils module
simply specifies a return value for cases that are not real triangles,
the Triangle class is more strict
and raises an exception if your sides lengths are not appropriate:

>>> from trianglelib.shape import Triangle
>>> Triangle(1, 1, 3)
Traceback (most recent call last):
  ...
ValueError: one side is too long to make a triangle

If you are not sanitizing your user input
to verify that the three side lengths they are giving you are safe,
then be prepared to trap this exception
and report the error to your user.
