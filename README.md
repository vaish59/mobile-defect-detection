# 📱 Mobile Defect Detection

This project focuses on detecting defects in mobile devices such as oil stains, scratches, and other anomalies using deep learning. A pre-trained **ResNet-18** model is fine-tuned to classify defects into three categories: **Oil, Scratch, and Stain**.

---

## 🚀 Features
- Utilizes **ResNet-18** for accurate defect classification.
- Supports **GPU acceleration** for faster inference.
- Custom dataset handling and augmentation.
- Generates classification reports for model performance evaluation.

---

## 📂 Project Structure
📁 Mobile Defect Detection/ │── 📄 requirements.txt # Dependencies for the project │── 📄 README.md # Documentation │── 📄 train.py # Training script │── 📄 test.py # Testing script │── 📄 predict.py # Single image prediction script │── 📁 dataset/ # Dataset directory │── 📁 models/ # Trained model weights │── 📁 notebooks/ # Jupyter notebooks for EDA & testing └── 📁 utils/ # Utility functions

yaml

---

## 🛠️ Installation
First, clone this repository:
```sh
git clone https://github.com/vaish59/mobile-defect-detection.git
cd mobile-defect-detection
Then, install the required dependencies:

sh
pip install -r requirements.txt
📊 Model Training
To train the model on your dataset, run:

sh

python train.py
This will:

Load the dataset

Apply transformations

Train the ResNet-18 model

Save the trained weights in models/

🧐 Testing & Evaluation
To test the model, run:

sh
python test.py
This will:

Load the trained model

Evaluate it on the test dataset

Print the accuracy & classification report

🔍 Predict a Single Image
To classify an image:

sh
python predict.py --image_path "path/to/your/image.jpg"
Example output:

yaml
Predicted Defect: Scratch
📦 Dataset
The dataset is available on Google Drive.
🔗 Download Dataset

📌 Flow Diagram
A high-level overview of the system flow:

🔗 Repository Link
GitHub Repository: https://github.com/vaish59/mobile-defect-detection

📞 Contact
For any queries, feel free to reach out:

Vaishnavi Jevale

📧 Email: vaishnavijevale59@gmail.com


🚀 Happy Coding! 
