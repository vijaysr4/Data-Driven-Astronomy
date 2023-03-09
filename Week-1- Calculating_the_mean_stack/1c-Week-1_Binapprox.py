import numpy as np
# Write your median_bins and median_approx functions here.

def median_bins(values, B):
  mean = np.mean(values)
  std = np.std(values)
  
  # Initialise bins
  left_bin = 0
  bins = np.zeros(B)
  bin_width = 2*std/B
  
  # Bin values
  for value in values:
    if value < mean - std:
      left_bin += 1
    elif value < mean + std:
      bin = int((value - (mean - std))/bin_width)
      bins[bin] += 1
    # Ignore values above mean + std
    
  return mean, std, left_bin, bins

def median_approx(values, B):
  # Call median_bins to calculate the mean, std,
  # and bins for the input values
  mean, std, left_bin, bins = median_bins(values, B)
    	
  # Position of the middle element
  N = len(values)
  mid = (N + 1)/2

  count = left_bin
  for b, bincount in enumerate(bins):
    count += bincount
    if count >= mid:
      # Stop when the cumulative count exceeds the midpoint
      break

  width = 2*std/B
  median = mean - std + width*(b + 0.5)
  return median


# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
