__author__ = 'darren lefcoe'
__twitter__ = '@dlefcoe'



def __example():
    ''' example of the code '''

    result = force_mass_acceleration(mass=10, acceleration=5)
    print('force:', result)

    result = force_mass_acceleration(force=10, acceleration=5)
    print('mass:', result)

    result = force_mass_acceleration(force=10, acceleration=1)
    print('mass:', result)

    result = force_mass_acceleration(force=10, acceleration=0.001)
    print('mass:', result)

    try:
        result = force_mass_acceleration(force=10, acceleration=0)
        print('mass:', result)
    except ValueError as e:
        print(e)

    return


def force_mass_acceleration(
        force:float|None=None, 
        mass:float|None=None, 
        acceleration:float|None=None) -> float|str:
    '''
    work out either:
        - force, masss or acceleration
        - using, force = mass x acceleration
        - given any two parameters with one unknown
    
    args:
        force: the force of the object (newtons)
        mass: the mass of the object (kg)
        acceleration: the acceleration of the object (m/s**2)
    
    returns:
        the missing parameter, either force or mass or acceleration.
    '''
    
    if force == None:
        force = mass * acceleration
        return force

    if mass == None:
        if acceleration == 0:
            raise ValueError('acceleration = 0, would return an infinite mass')
        else:
            mass = force / acceleration
            return mass
    
    if acceleration == None:
        if mass == 0:
            raise ValueError('mass = 0, would return infinite acceleration')
        else:
            acceleration = force / mass
            return acceleration

    return


# main guard idiom
if __name__=='__main__':
    __example()
