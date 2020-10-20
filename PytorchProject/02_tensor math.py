import torch

x = torch.tensor([1, 2, 3])
y = torch.tensor([9, 8, 7])
z = torch.empty(3)

# addition
torch.add(x, y, out=z)  # all possible
z = torch.add(x, y)
z = x + y

# division
# z = torch.true_divide(x, y)

# inplace operations
t = torch.zeros(3)
t.add_(x)
t += x

# exponentiation
z = x.pow(2)
z = x ** 2

# matrix multifilcation











