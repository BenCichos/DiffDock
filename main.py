import torch

if torch.backends.mps.is_available():
    print("True")
