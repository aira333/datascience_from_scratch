'''
MTL, the networ has a few shared layers and task-specific segments
during backpropagation, gradients are accumualted from all branches

input = x

output = sin(x), cos(x)
'''

import torch
import torch.nn as nn
import torch.optim as optim

class Net(nn.Module):
    def __init__(self, h):
        super(Net, self).__init__()
        # shared layers
        self.model = torch.nn.Sequential(
            torch.nn.Linear(1, h),
            torch.nn.ReLU(),
            torch.nn.Linear(h, h),
            torch.nn.ReLU()
        )
        # sine branch
        self.model_sin = torch.nn.Sequential(
            torch.nn.Linear(h, h),
            torch.nn.ReLU(),
            torch.nn.Linear(h, 1)
        )
        # cosine branch
        self.model_cos = torch.nn.Sequential(
            torch.nn.Linear(h, h),
            torch.nn.ReLU(),
            torch.nn.Linear(h, 1)
        )

    def forward(self, inputs):

        # pass through shared layers
        x1 = self.model(inputs)

        # generate sin(X) prediction
        output_sin = self.model_sin(x1)

        # generate cos(x) prediction
        output_cos = self.model_cos(x1)

        # return both predictions
        return output_sin, output_cos

# Hyperparameters
h = 150
epochs = 100
learning_rate = 0.01

# Generate some dummy data
x = torch.randn(100, 1)  # Example input data
sin_true = torch.sin(x)
cos_true = torch.cos(x)

# Initialize the network, loss function, and optimizer
net = Net(h)
loss_func = nn.MSELoss()
optimizer = optim.Adam(net.parameters(), lr=learning_rate)

# Training loop
for epoch in range(epochs):

    # generate prediction
    sin_pred, cos_pred = net(x)

    # compute loss
    loss1 = loss_func(sin_pred, sin_true)
    loss2 = loss_func(cos_pred, cos_true)

    # add loss
    loss = loss1 + loss2

    # run backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

print("Training finished!")