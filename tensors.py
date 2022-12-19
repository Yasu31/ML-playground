import torch
"""
this error lost me a lot of time in the Probabilistic AI project to implement DQN
"""
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

print(f"{x=}\t{y=}")

print(f"{x + y=}")
print(f"{x.unsqueeze(1)=}")

print(f"{x.unsqueeze(1)+y=}")
print(f"{x.unsqueeze(1)+y.unsqueeze(1)=}")