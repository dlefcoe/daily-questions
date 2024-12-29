'''
temperature conversion class example.
converts from C to F or F to C.

'''
__author__ = '@dlefcoe'


# imports
from dataclasses import dataclass

@dataclass
class Temp:
    ''' temperature conversion '''
    value: float = 0
    unit: str = 'c'

    def __post_init__(self):
        if self.unit == 'c':
            self.celcius_to_farenheight()
        elif self.unit == 'f':
            self.farenheight_to_celcius()
        else:
            
            raise ValueError(
                f'unit given was {self.unit}.\n'
                f'unit needs to be "c" or "f".')

    def celcius_to_farenheight(self):
        ''' celcius to farenheight '''
        self.value = self.value*9/5 + 32
        self.unit = 'f'
        return

    def farenheight_to_celcius(self):
        ''' celcius to farenheight '''
        self.value = (self.value - 32) * (5/9)
        self.unit = 'c'
        return


def main():
    ''' main entry point for the code '''
    t1 = Temp(10, 'c')
    t2 = Temp(t1.value, t1.unit)
    print(t1)
    print(t2)
    return


# main guard idiom
if __name__=='__main__':
    main()



