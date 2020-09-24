import numpy as np

def calculate(list):
  
  # raise error 
  if len(list) < 9: 
    raise ValueError("List must contain nine numbers.")
  
  
  npArr = np.array(list).reshape(3,3)
  
  calculations = {
    "mean": [np.mean(npArr, axis=0), np.mean(npArr, axis=1), np.mean(npArr)],
    "variance": [np.var(npArr, axis=0), np.var(npArr, axis=1), np.var(npArr)],       
    "standard deviation": [np.std(npArr, axis=0), np.std(npArr, axis=1), np.std(npArr)], 
    "max": [np.max(npArr, axis=0), np.max(npArr, axis=1), np.max(npArr)],
    "min": [np.min(npArr, axis=0), np.min(npArr, axis=1), np.min(npArr)],
    "sum": [np.sum(npArr, axis=0), np.sum(npArr, axis=1), np.sum(npArr)]   
    
}

  for k, v in calculations.items(): 
    calculations[k] = [i.tolist() for i in v]
  
  return calculations
  
  