import random

def init_weights(input_size, output_size):
  # input_size is the number of columns in the weights matrix
  # output_size is the number of rows in the weights matrix
  weights = []

  # create randomized weights
  for _ in range(output_size):
    row_weights = []
    for _ in range(input_size):
      weight = random.uniform(-1, 1)
      row_weights.append(weight)
    weights.append(row_weights)

  # create biases, all initialized to zero
  biases = []
  for _ in range(output_size):
      bias = 0
      biases.append(bias)

  return weights, biases

def forward_pass(input, weights, biases):
    output = []
    for i in range(len(weights)):
        # Initialize the weighted sum for the current neuron to zero
        weighted_sum = 0

        # Calculate the weighted sum for the current neuron
        for j in range(len(input)):
            # Multiply each input by the corresponding weight and add it to the sum
            weighted_sum += input[j] * weights[i][j]

        # Add the bias to the weighted sum
        weighted_sum += biases[i]

        # Append the result to the output list
        output.append(weighted_sum)

    return output
