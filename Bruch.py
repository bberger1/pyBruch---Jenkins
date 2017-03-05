'''
Created on 26.10.2016

@author: Benedikt Berger
'''

class Bruch(object):

    def __iter__(self):
        """
        makes the class iterable
        """
        return (self.zaehler, self.nenner).__iter__()

    def __init__(self, zaehler=0, nenner=1):
        """
        :raise TypeError: invalid variable types
        :raise ZeroDivisionError: if nenner equals zero
        :param zaehler: has to be Bruch or int
        :param nenner: has to be int and not zero
        """

        if isinstance(zaehler, Bruch):
            self.zaehler, self.nenner = zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('__init__: invalid variable type: '+type(zaehler))
        elif type(nenner) is not int:
            raise TypeError('__init__: invalid variable type: '+type(nenner))

        if zaehler < 0 and nenner < 0:
            nenner = abs(nenner)
            zaehler = abs(zaehler)
        elif nenner == 0:
            raise ZeroDivisionError

        self.zaehler = zaehler
        self.nenner = nenner

    def __float__(self):
        """
        overrides float() to allow Bruch
        :return: float result of the division of zaehler and nenner
        """

        return float(self.zaehler / self.nenner)

    def __int__(self):
        """
        overrides int() to allow Bruch
        :return: int value which calls float()
        """
        return int(self.__float__())

    def __gt__(self, other):
        """
        overrides greater than operator (>)
        :param other: value to compare
        :return: true or false (if greater than)
        """
        if float(self) > float(other):
            return True

    def __mul__(self, other):
        """
        overrides multiply operator (*)
        :param other: value to multiply
        :return: Bruch with self mulitplied by other
        """
        if(isinstance(other, Bruch)):
            return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)
        if(isinstance(other, int)):
            return self * Bruch(other)
        else:
            raise TypeError('__mul__: invalid variable type: '+type(other))

    def __str__(self):
        """
        overrides to string()
        :return: Bruch in the given format
        """
        if self.nenner == 1:
            return '(%s)' % (str(self.zaehler))
        else:
            return '(%s/%s)' % (str(self.zaehler), str(self.nenner))

    def __pow__(self, p):
        """
        overrides pow()
        :param power: exponent of Bruch
        :return: Bruch with zaehler and nenner to the power of the exponent
        """
        return Bruch(self.zaehler**p, self.nenner**p)

    def __abs__(self):
        """
        overrides abs()
        :return: Bruch with the absolute values of self.zaehler and self.nenner
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __neg__(self):
        """
        overrides minus operator (-)
        :return: Bruch with negative zaehler or negative nenner
        """
        if(self.zaehler < 0):
            return Bruch(-self.zaehler, self.nenner)
        elif(self.nenner < 0):
            return Bruch(self.zaehler, -self.nenner)


    @staticmethod
    def __makeBruch(zaehler):
        """
        returns a Bruch with the given value
        :param value: the zaehler of the returned Bruch
        :return: Bruch with the given zaehler as zaehler
        """
        return Bruch(zaehler, 1)

    def __sub__(self, other):
        """
        overrides minus operator (-)
        :param other: value to subtract
        :return: Bruch with subtracted from other
        """
        if (isinstance(other, int)):
            return Bruch(self.zaehler - (self.nenner * other), self.nenner)
        elif (isinstance(other, Bruch)):
            zaehlerSelf = self.zaehler
            zaehlerOther = other.zaehler

            neuerNenner = lcm(self.nenner, other.nenner)
            zaehlerSelf *= neuerNenner / self.nenner
            zaehlerOther *= neuerNenner / other.nenner

            return Bruch(int(zaehlerSelf - zaehlerOther), neuerNenner)
        else:
            raise TypeError('__sub__: invalid variable type: '+type(other))

    def __isub__(self, other):
        """
        overrides minus equals operator (-=)
        :param other: value to substract
        :return: Bruch with self subtracted from other
        """
        return self - other

    def __rsub__(self, other):
        """
        overrides minus operator (-)  on right side
        :param other: value to substract
        :return: Bruch with other subtracted from self
        """
        return Bruch(other) - self


    def __add__(self, other):
        """
        overrides plus operator (+)
        :param other: value to add
        :return: Bruch with other added to self
        """
        if(isinstance(other, int)):
            return Bruch(self.zaehler+(self.nenner*other), self.nenner)
        elif(isinstance(other, Bruch)):
            zaehlerSelf = self.zaehler
            zaehlerOther = other.zaehler

            neuerNenner = lcm(self.nenner, other.nenner)
            zaehlerSelf *= neuerNenner / self.nenner
            zaehlerOther *= neuerNenner / other.nenner

            return Bruch(int(zaehlerSelf+zaehlerOther), neuerNenner)
        else:
            raise TypeError('__add__: invalid variable type: '+type(other))

    def __iadd__(self, other):
        """
        overrides the plus equals operator (+=)
        :param other: value to add
        :return: Bruch with other added to self
        """
        return self + other

    def __radd__(self, other):
        """
        overrides add operator (+) on the right side
        :param other: value to add
        :return: Bruch with self added to other
        """
        return Bruch(other) + self

    def __truediv__(self, other):
        """
        overrides division operator (/) (for python version 3.x)
        :param other: value to divide
        :return: Bruch with self divided by other
        """
        if(isinstance(other, Bruch)):
            return Bruch(self.zaehler*other.nenner, self.nenner*other.zaehler)
        elif(isinstance(other, int)):
            return self / Bruch(other)
        elif(other == 0):
            raise ZeroDivisionError
        else:
            raise TypeError('__truediv__: invalid values for division: '+type(other))

    def __itruediv__(self, other):
        """
        overrides divide equals operator (/=)
        :param other: value to divide
        :return: Bruch with self divided by other
        """
        return self / other

    def __rtruediv__(self, other):
        """
        overrides divide operator (/) (for python version 3.x)
        :param other: value to divide
        :return: Bruch with other divided by self
        """
        return Bruch(other) / self

    def __eq__(self, other):
        """
        overrides euals operator (==)
        :param other: value to compare
        :return: true or false (if equals)
        """
        if float(self) == float(other):
            return True

    def __ge__(self, other):
        """
        overrides greater than or equals operator (>=)
        :param other: value to compare
        :return: true or false (if greater than or equals)
        """
        if float(self) >= float(other):
            return True

    def __invert__(self):
        """
        overrides invert operator (~)
        :return: Bruch, where nenner and zaehler are switched
        """
        return Bruch(self.nenner, self.zaehler)

    def __lt__(self, other):
        """
        overrides less than operator (<)
        :param other: value to compare
        :return: true or false (if less than)
        """
        if float(self) < float(other):
            return True

    def __le__(self, other):
        """
        overrides less than operator (<=)
        :param other: value to compare
        :return: true or false (if less than)
        """
        if float(self) <= float(other):
            return True

    def __rmul__(self, other):
        """
        overrides multiply operator (*) right side
        :param other: value to multiply with
        :return: Bruch with other multiplied by self
        """
        return Bruch(other) * self

    def __imul__(self, other):
        """
        overrides the multiply equals operator (*=)
        :param other: value to multiply with
        :return: Bruch with self mutliplied by other
        """
        return self * other

def lcm(x, y):
    """
    least common multiple of the values x and y
    :param x: First integer
    :param y: Second integer
    :return: least common multiple of the given values
    """
    if x > y:
       greater = x
    else:
       greater = y

    while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

    return lcm
