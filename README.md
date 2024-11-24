# Handwritten Digit Recognizer

This is a web-based application that recognizes handwritten digits using a trained Artificial Neural Network (ANN) model based on the MNIST dataset. Users can upload an image of a handwritten digit, and the app predicts the digit.

## Features
Upload a handwritten digit image.
Click the "Predict" button to get the predicted digit.
Interactive and user-friendly interface built with Streamlit.

## Project Structure
drop_model.h5: Trained ANN model for digit recognition.
mnist_interface.py: Streamlit application for the web interface.
MNIST.ipynb: Contains the notebook of training model.

## How It Works
Training the Model:

The ANN model was trained on the MNIST dataset, which contains 70,000 images of handwritten digits (60,000 for training and 10,000 for testing).
The model achieves 92% accuracy in predicting digits from 0 to 9.

Web App:

Users upload an image of a digit via the web interface.
The image is preprocessed (grayscale conversion, resizing).
The trained model predicts the digit, and the result is displayed.

## Installation
Clone this repository:

bash
Copy code
git clone https://github.com/abbas-cs/Handwritten-Digit-Recognizer.git

## Run the Streamlit app:

bash
Copy code
streamlit run mnist_interface.py
Usage
Upload a clear image of a handwritten digit (preferably on a white background).
Click the "Predict" button to see the predicted digit.
Enjoy testing the app with different handwritten digits!


Dependencies
Python 3.7+
TensorFlow
NumPy
OpenCV

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request to improve this project.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

