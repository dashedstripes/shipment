from layers import LinearLayer

class NeuralNetwork:
  def __init__(self):
    self.layer = LinearLayer(2, 3)

  def forward(self, input):
    logits = self.layer.forward(input)
    return logits
