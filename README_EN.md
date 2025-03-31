# 🩻 Musculoskeletal Radiograph Classification with Deep Learning

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/PyTorch-%3E=2.0-orange)](https://pytorch.org/)
[![Status](https://img.shields.io/badge/status-Completed-brightgreen.svg)]()
[![Model](https://img.shields.io/badge/model-ResNet18-blueviolet)]()

This project applies Deep Learning techniques to classify musculoskeletal radiographs as **normal** or **abnormal**. It is designed as an experimental tool to support medical diagnostics, using a transfer learning approach.

---

## 🎯 Problem Statement

Healthcare professionals analyze thousands of radiographs daily. This task is **time-consuming, repetitive, and prone to human error**. The goal of this project is to build a model that, given a radiograph, predicts whether it contains a structural abnormality.

This tool is not intended to replace radiologists, but to serve as an **initial support system** to help prioritize or automatically detect potentially pathological cases.

---

## 🗂️ Dataset Used

- **Name**: MURA (Musculoskeletal Radiographs)
- **Source**: [Stanford ML Group](https://stanfordmlgroup.github.io/competitions/mura/)
- **Type**: **Public and open-source** dataset for research
- **Contents**:
  - Over 40,000 radiographic images
  - 7 anatomical regions (shoulder, elbow, wrist, etc.)
  - Study-level labels: `positive` (abnormal), `negative` (normal)
- **Preprocessing**:
  - A **custom dataset** was created by ignoring the body part and grouping all images by condition (`positive` or `negative`)
  - A significant **class imbalance** was detected in favor of normal images

---

## 🧠 Solution Overview

This project follows a modern computer vision pipeline using deep learning:

- Base model: `ResNet18` pretrained on ImageNet
- Partial fine-tuning: only deeper layers (`layer2`, `layer3`, `layer4`, `fc`) were unfrozen
- Data augmentation: random rotation, crop, color jitter, etc.
- Class imbalance handling:
  - Weighted loss function (`CrossEntropyLoss`)
  - F1-score as the main evaluation metric
- Early stopping and automatic learning rate reduction with `ReduceLROnPlateau`
- Misclassification visualization for qualitative analysis
- Trained model saved in `.joblib` format for reuse

---

## 🧱 Project Structure

```plaintext
src/ │ ├── data_sample/ # Lightweight data samples
     │ ├── img/ # Project-related or visualization images 
     │ ├── notebooks/ # Experimental or exploratory Jupyter notebooks
     │ ├── results_notebook/ # Final notebook with clean, reproducible code
     │ ├── models/ # Saved models (state_dict as .pt or .joblib)
     │ └── utils/ # Helper functions, utility scripts, custom classes
```

📌 *Note*: Large data files have not been uploaded to GitHub, however they can be found at [Stanford ML Group](https://stanfordmlgroup.github.io/competitions/mura/) .

---

## 📦 Dependencies

Make sure to install the following libraries (recommended via `pip install -r requirements.txt`):

- `torch >= 2.0`
- `torchvision`
- `numpy`
- `matplotlib`
- `seaborn`
- `Pillow`
- `scikit-learn`
- `joblib`
- `tqdm` (optional for progress bars)

---

## 🧪 Results

The trained model achieves solid F1-scores on the validation set, showing good ability to detect abnormal cases despite the class imbalance.  
A classification report, confusion matrix, and sample misclassifications are included for analysis.

---

## 🚀 How to Run

To train or evaluate the model:

1. Place your data in `src/data_sample/` or configure the path to the full MURA dataset.
2. Run the final notebook in `src/results_notebook/`
3. Use the trained weights in `src/models/` for inference or transfer

---

## 👨‍⚕️ Disclaimer

This project is intended for **educational and research purposes only**.  
It is **not suitable for clinical use** without rigorous validation by certified medical professionals.

---

✍️ Autor
Álvaro Sánchez Martín
