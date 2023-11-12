from layers import LinearLayer

train_data = [
  [0,0,0,0],
  [1,1,1,1],
  [0.5,0.5,0.5,1],
  [0.25,0.25,0.25,0],
  [0.75,0.75,0.75,1],
]

class NeuralNetwork:
  def __init__(self):
    self.layer = LinearLayer(4, 2)

  def forward(self, input):
    logits = self.layer.forward(input)
    return logits

model = NeuralNetwork()
logits = model.forward(train_data)

print(logits)
