import time, numpy as np
from astropy.io import fits

# Write your function median_FITS here:
def median_fits(filenames):
  start = time.time() # Start timer
  # Read in all the FITS files and store in list
  FITS_list = []
  for filename in filenames:
    hdulist = fits.open(filename)
    FITS_list.append(hdulist[0].data)
    hdulist.close()
    
  # Stack image arrays in 3D array for median calculation
  FITS_stack = np.dstack(FITS_list)
  
  median = np.median(FITS_stack, axis = 2)
  
  # Calculate the memory consumed by the data
  memory = FITS_stack.nbytes
  # or, equivalently:
  # memory = 200 * 200 * len(filename) * FITS_stack.itemsize
  
  # convert to kB:
  memory /= 1024
  
  stop = time.time() - start # stop timer
  return median, stop, memory
    


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])