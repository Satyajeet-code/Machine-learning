# Motion Sign Language Detection

🤖 **Welcome to the Motion Sign Language Detection project!** This GitHub repository focuses on detecting sign language gestures in real-time using a combination of computer vision and machine learning techniques.

## Files Overview

### [Sign language data collection.ipynb](Sign language data collection.ipynb) 📹
This Python script is dedicated to **data collection** using OpenCV and MediaPipe libraries. It captures video input, extracts hand landmarks, and saves the data for training the models.

### [Sign language load saved model.ipynb](Sign language load saved model.ipynb) 🧠
In this file, two models are trained - a **Recurrent Neural Network (RNN)** and a **Long Short-Term Memory (LSTM)** network. These models are trained on a dataset consisting of eight different sign language gestures.

### [Sign language model building.ipynb](Sign language model building.ipynb) 👁️
This script uses OpenCV to capture real-time video input, extracts hand landmarks with MediaPipe, and utilizes the trained models from \`file2\` (RNN and LSTM) for predicting sign language gestures in real-time. The predictions are spoken using the \`win32com\` library and translated into German.

### [essentials.py](essentials.py)
This essential module contains various functions used across different scripts. It includes functions for reading video input using OpenCV, drawing landmarks, and converting them into arrays for further processing.

## Usage
1. Run \`file1_data_collection.py\` to collect training data.
2. Execute \`file2_train_models.py\` to train the RNN and LSTM models.
3. Finally, run \`file3_real_time_prediction.py\` for real-time sign language detection, prediction, and translation.

Make sure to install the required dependencies using:

\`\`\`bash
pip install -r requirements.txt
\`\`\`
 

Feel free to contribute and enhance the capabilities of this project! 🚀" > README.md
