import torch
import numpy as np

# initialize Tensor

data = [[1,2], [3,4]]
# to data
x_data = torch.tensor(data)  

# to Numpy
np_array = np.array(data) 
x_np = torch.from_numpy(np_array)

# other Tensor
x_ones = torch.ones_like(x_data) # keep attribute
x_rand = torch.rand_like(x_data, dtype=torch.float) # modify attribute

# Using random or const value

shape = (2,3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print (x_data)
print (x_np)
print(f"Ones Tensor: \n {x_ones} \n")
print(f"Random Tensor : {x_rand}\n")
print("\n RANDOM \n")
print(f"Random Tensor: \n {rand_tensor}")
print(f"Ones Tensor: \n {ones_tensor}")
print(f"Zeros Tensor: \n {zeros_tensor}")
