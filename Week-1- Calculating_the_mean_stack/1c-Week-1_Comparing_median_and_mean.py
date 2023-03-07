# Write your list_stats function here.
import numpy as np

def list_stats(values):
  
  N = len(values)
  if N == 0:
    return
  
  # Mean
  mean = sum(values)/N
  
  # Median 
  values.sort()
  mid = int(N/2)
  if N%2 == 0:
    median = (values[mid] + values[mid - 1])/2
  else:
    median = values[mid]
  return median, mean
  
  
    
  return median, mean



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)