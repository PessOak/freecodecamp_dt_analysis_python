import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  np_array = np.array(list)
  matrix_array = np_array.reshape((3,3))
  
  all_means = [np.mean(matrix_array, axis=0).tolist(), np.mean(matrix_array, axis=1).tolist(), np.mean(np_array)]
  all_var = [np.var(matrix_array, axis=0).tolist(), np.var(matrix_array, axis=1).tolist(), np.var(np_array)]
  all_std = [np.std(matrix_array, axis=0).tolist(), np.std(matrix_array, axis=1).tolist(), np.std(np_array)]
  all_max = [np.amax(matrix_array, axis=0).tolist(), np.amax(matrix_array, axis=1).tolist(), np.amax(np_array)]
  all_min = [np.amin(matrix_array, axis=0).tolist(), np.amin(matrix_array, axis=1).tolist(), np.amin(np_array)]
  all_sum = [np.sum(matrix_array, axis=0).tolist(), np.sum(matrix_array, axis=1).tolist(), np.sum(np_array)]
  
  calculations = {
  'mean': all_means,
  'variance': all_var,
  'standard deviation': all_std,
  'max': all_max,
  'min': all_min,
  'sum': all_sum
}
  
  return calculations



calculate([0,1,2,3,4,5,6,7,8])