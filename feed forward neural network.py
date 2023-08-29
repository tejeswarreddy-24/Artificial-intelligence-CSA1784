import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate some random training data
np.random.seed(42)
X = np.random.rand(100, 2)
y = (X[:, 0] + X[:, 1] > 1).astype(int)

# Build the neural network model
model = Sequential([
    Dense(4, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=100, batch_size=32)

# Get user input
user_input = input("Enter two values separated by a space: ")
input_values = [float(val) for val in user_input.split()]

if len(input_values) != 2:
    print("Please enter exactly two values.")
else:
    # Make prediction
    prediction = model.predict(np.array([input_values]))
    predicted_label = "greater than 1" if prediction > 0.5 else "not greater than 1"
    
    print(f"The sum of the input values is predicted to be {predicted_label}.")
