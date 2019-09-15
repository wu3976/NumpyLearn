import numpy as np

# sin, cos, arcsin....
arr1=np.array([0, 30, 45, 60, 90], dtype='f')
sin_arr=np.sin(arr1*np.pi/180) # convert to radian
print(sin_arr)

#np.degree convert radian to degree
inverse=np.arcsin(sin_arr)
print(np.degrees(inverse))

# numpy.around(a,decimals) rounding a to the decimal specified
inv_round=np.around(np.degrees(inverse), 0)
print(inv_round)

#np.floor() take largest integer i, such that i <= x
# np.cell() is the inverse
inv_flr_deg=np.floor(np.degrees(inverse))
print(inv_flr_deg)