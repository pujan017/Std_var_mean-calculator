import numpy as np

def calculate(numbers):
  if len(numbers)!=9:
    raise ValueError('List must contain nine numbers.')
    
  result=np.array(numbers).reshape(3,3)

  mean=[list(np.mean(result,axis=0)),list(np.mean(result,axis=1)),np.mean(result)]
  variance=[list(np.var(result,axis=0)),list(np.var(result,axis=1)),np.var(result)]
  standard_deviation=[list(np.std(result,axis=0)),list(np.std(result,axis=1)),np.std(result)]
  max=[list(np.max(result,axis=0)),list(np.max(result,axis=1)),np.max(result)]
  min=[list(np.min(result,axis=0)),list(np.min(result,axis=1)),np.min(result)]
  sum=[list(np.sum(result,axis=0)),list(np.sum(result,axis=1)),np.sum(result)]


  calculations={
    'mean':mean,
    'variance':variance,
    'standard deviation':standard_deviation,
    'max':max,
    'min':min,
    'sum':sum
  }




  return calculations