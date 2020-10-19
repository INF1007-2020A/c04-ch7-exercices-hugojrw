#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def compute_volume_mass(a ,b ,c ,p):
    volume=(4/3)*math.pi**a*b*c
    mass=p*volume
    return mass,volume

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(compute_volume_mass(2, 4, 2, 10))
    pass
