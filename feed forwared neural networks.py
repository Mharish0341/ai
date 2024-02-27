import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Define the neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights with random values
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)

    def forward(self, inputs):
        # Perform the forward pass through the network
        self.hidden_layer_input = np.dot(inputs, self.weights_input_hidden)
        self.hidden_layer_output = sigmoid(self.hidden_layer_input)

        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output)
        self.predicted_output = sigmoid(self.output_layer_input)

        return self.predicted_output

    def backward(self, inputs, targets, learning_rate):
        # Calculate the error and deltas
        output_error = targets - self.predicted_output
        output_delta = output_error * sigmoid_derivative(self.predicted_output)

        hidden_layer_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_layer_delta = hidden_layer_error * sigmoid_derivative(self.hidden_layer_output)

        # Update weights with the deltas
        self.weights_hidden_output += self.hidden_layer_output.T.dot(output_delta) * learning_rate
        self.weights_input_hidden += inputs.T.dot(hidden_layer_delta) * learning_rate

    def train(self, inputs, targets, epochs, learning_rate):
        for epoch in range(epochs):
            # Perform forward and backward passes for each training example
            for i in range(len(inputs)):
                input_data = inputs[i:i+1]
                target_data = targets[i:i+1]

                self.forward(input_data)
                self.backward(input_data, target_data, learning_rate)

                # Print the training progress
                if (epoch % 1000 == 0) and (i == len(inputs) - 1):
                    print(f"Epoch {epoch}, Loss: {np.mean(np.square(target_data - self.predicted_output))}")

# Example usage:
# Define input and target data
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = np.array([[0], [1], [1], [0]])

# Create a neural network with 2 input neurons, 4 hidden neurons, and 1 output neuron
neural_network = NeuralNetwork(input_size=2, hidden_size=4, output_size=1)

# Train the neural network
neural_network.train(inputs, targets, epochs=10000, learning_rate=0.1)

# Test the trained neural network
for input_data in inputs:
    predicted_output = neural_network.forward(input_data)
    print(f"Input: {input_data}, Predicted Output: {predicted_output}")
