# Write your load_fits function here.
from astropy.io import fits
import numpy as np

def load_fits(file):
  hduli = fits.open(file)
  df = hduli[0].data
  
  arg_max = np.argmax(df)
  max_pos = np.unravel_index(arg_max, df.shape)
  return max_pos

if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image1.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()

 