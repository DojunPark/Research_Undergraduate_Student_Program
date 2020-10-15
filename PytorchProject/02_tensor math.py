import torch

tensor = torch.tensor([1, 3])         # int64
tensor = torch.tensor([1.0, 3.0])   # float32
tensor = torch.LongTensor([1, 3])   # int64
tensor = torch.FloatTensor([1, 3])  # float32

print(tensor)
print(tensor.dtype)