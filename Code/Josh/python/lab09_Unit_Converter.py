
def distance_m(in_units, distance_f):
    if in_units == 'ft':
        m =  distance_f / 3.2808
    elif in_units == 'mi':
        m = distance_f / 0.00062137
    elif in_units == 'm':
        m = in_units
    elif in_units == 'km':
        m = distance_f / 0.0010000
    return m
def converted_distance(distance_in, units_out):
    if units_out == 'ft':
        new_d = distance_in * 3.2808
    elif units_out == 'mi':
        new_d = distance_in * 0.00062137
    elif units_out == 'm':
        new_d = units_out
    elif units_out =='km':
        distance_in / 1000
    return new_d

distance = int(input('What is the distance?'))
from_units = (input('What are the input units?'))
to_units = (input('what do you want to convert to?'))

meters = distance_m(from_units, distance)
new_distance = converted_distance(meters, to_units)
print(meters)
print(f'{new_distance} {to_units}')



