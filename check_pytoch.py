import torch

print(torch.__version__)
print(torch.cuda.is_available()) 
print(torch.cuda.get_device_name(0))
x = torch.rand(3, 3, device="cuda")
print (x @ x)

# True
# NVIDIA GeForce RTX 5060 Ti
# tensor([[1.0484, 1.1209, 0.5212],
#         [0.6519, 0.6917, 0.3581],
#         [0.9593, 0.8472, 0.5411]], device='cuda:0')