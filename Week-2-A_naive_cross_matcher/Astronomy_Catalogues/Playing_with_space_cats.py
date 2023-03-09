import numpy as np
# Write your import_bss function here.

def hms2dec(hr, m, s):
  dec = hr + m/60 + s/3600
  return dec*15

def dms2dec(d, m, s):
  sign = d/abs(d)
  dec = abs(d) + m/60 + s/3600
  return sign*dec

def import_bss():
  res = []
  data = np.loadtxt('bss.dat', usecols = range(1, 7))
  for i, row in enumerate(data, 1):
    res.append((i, hms2dec(row[0], row[1], row[2]), dms2dec(row[3], row[4], row[5])))
  return res

def import_super():
  data = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=(0, 1))
  res = []
  for i, row in enumerate(data, 1):
    res.append((i, row[0], row[1]))
  return res

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)
