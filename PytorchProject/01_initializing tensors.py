import torch


# initializing tensor
device = 'cuda' if torch.cuda.is_available() else 'cpu'
my_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32, device=device, requires_grad=True)

print(my_tensor)
print(my_tensor.dtype)
print(my_tensor.device)
print(my_tensor.requires_grad)


# other common initialization methods
x = torch.empty((3, 3))
x = torch.zeros((3, 3))
x = torch.rand((3, 3))
x = torch.ones((3, 3))
x = torch.eye(3, 3)  # Identity matrix 단위 행렬
x = torch.arange(0, 5, 1)
x = torch.linspace(1, 5, 10)
x = torch.empty((1, 100)).normal_(mean=0, std=1)
x = torch.empty((1, 100)).uniform_(0, 1)  # torch.rand()와 동일
x = torch.diag(torch.ones(5))   # torch.eye()와 동일
x = torch.diag(torch.tensor([1, 2, 3]))

print(x)


# How to initialize and convert tensors to other types (int, float, double)
tensor = torch.arange(4)  # [0, 1, 2, 3]

print(tensor)
print(tensor.bool())
print(tensor.short())  # dtype=torch.int16
print(tensor.long())   # dtype=torch.int64 super important
print(tensor.half())   # dtype=torch.float16
print(tensor.float())  # dtype=torch.float32 super important
print(tensor.double()) # dtype=torch.float64


# array to tensor and vice-versa
import numpy as np
array = np.zeros((5, 5))
tensor = torch.from_numpy(array)         # default는 float64
tensor = torch.from_numpy(array).long()  # torch.int64로 지정
tensor = torch.from_numpy(array).float() # torch.float32로 지정

array_back = tensor.numpy()

print(array_back)
print(array_back.dtype)
