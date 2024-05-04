# Motion Sign Language Detection

🤖 **Welcome to the Motion Sign Language Detection project!** This GitHub repository focuses on detecting sign language gestures in real-time using a combination of computer vision and machine learning techniques.

## Files Overview

### [Sign language data collection.ipynb](https://github.com/Satyajeet-code/Machine-learning/blob/main/Voice%20enabled%20motion%20sign%20lnguage%20detection/Sign%20language%20data%20collection.ipynb) 📹
This Python script is dedicated to **data collection** using OpenCV and MediaPipe libraries. It captures video input, extracts hand landmarks, and saves the data for training the models.

### [Sign language model building.ipynb](https://github.com/Satyajeet-code/Machine-learning/blob/main/Voice%20enabled%20motion%20sign%20lnguage%20detection/Sign%20language%20model%20building.ipynb) 🧠
In this file, two models are trained - a **Recurrent Neural Network (RNN)** and a **Long Short-Term Memory (LSTM)** network. These models are trained on a dataset consisting of eight different sign language gestures.

### [Sign language load saved model.ipynb](https://github.com/Satyajeet-code/Machine-learning/blob/main/Voice%20enabled%20motion%20sign%20lnguage%20detection/Sign%20language%20load%20saved%20model.ipynb)👁️
This script uses OpenCV to capture real-time video input, extracts hand landmarks with MediaPipe, and utilizes the trained models from \`file2\` (RNN and LSTM) for predicting sign language gestures in real-time. The predictions are spoken using the \`win32com\` library and translated into German.

### [essentials.py](essentials.py)
This essential module contains various functions used across different scripts. It includes functions for reading video input using OpenCV, drawing landmarks, and converting them into arrays for further processing.

## Usage
1. Run `Sign language data collection.ipynb` to collect training data.
2. Execute `Sign language model building.ipynb` to train the RNN and LSTM models.
3. Finally, run `Sign language load saved model.ipynb` for real-time sign language detection, prediction, and translation.

Make sure to install the required dependencies using:

```bash
pip install -r requirements.txt
```
### Screenshots

![Screenshots](https://github.com/Satyajeet-code/Machine-learning/blob/main/Voice%20enabled%20motion%20sign%20lnguage%20detection/love%20you.png)

![Screenshots](https://github.com/Satyajeet-code/Machine-learning/blob/main/Voice%20enabled%20motion%20sign%20lnguage%20detection/Screenshot%202024-03-11%20192202.png)

Feel free to contribute and enhance the capabilities of this project! 🚀" > README.md
