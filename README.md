# HISAC
Histopathological Image Segmentation and Classifier

---
Histopathological image analysis, including biopsy image segmentation and classification, is an important field in digital pathology that uses advanced computational techniques to analyze microscopic images of tissue samples. This process aids pathologists in diagnosing diseases, particularly cancer.

# Overview
This project focuses on automating nuclei segmentation from histopathological images using deep learning techniques.
Segmentation helps identify cellular structures essential for medical image analysis and diagnostic workflows.

Two models were developed and compared —
U-Net as the baseline encoder–decoder model, and BASNet-inspired model as a boundary-aware approach for enhanced precision.

The proposed method integrates a hybrid loss function (Dice + Focal + SSIM) that improves both overlap accuracy and boundary sharpness by reducing segmentation errors in overlapping nuclei.

# Objectives
* Developing a deep learning-based segmentation system for histopathological nuclei.

* Addressing boundary blurring and class imbalance using hybrid loss optimization.

* Comparing U-Net and BASNet-based architectures quantitatively.

* Evaluate performance using Dice Score, IoU, Pixel Accuracy, and Boundary F1 Score.

# Dataset
The project uses the MoNuSeg (Multi-Organ Nuclei Segmentation) dataset, containing histopathological images from multiple organs with expert-annotated masks.

Preprocessing Steps:

* Normalization of pixel intensity values (0–1 scale).

* Resizing of all images and masks to 256×256 pixels.

* Data augmentation using rotation, flipping, and color adjustments for generalization.

# Model Architecture
## U-Net
* Encoder–decoder CNN architecture with skip connections.

* Efficient in segmentation but limited at boundary delineation and overlapping nuclei separation.

## BASNet-Inspired Model (Improved)
* Incorporates residual and attention blocks for better feature extraction.

* Uses dense decoder refinement to preserve edges and small details.

* Designed for boundary-aware learning, improving precision and edge quality.

# Hybrid Loss Function
To balance accuracy, structure, and boundary learning, a hybrid loss function was used:

**Total Loss** = α₁·Dice + α₂·Focal + α₃·SSIM
�

This combination produced consistent improvement in both overlap accuracy and boundary quality.

🧮

## Project Report
[Histopathological Image Segmentation Report.pdf](https://github.com/user-attachments/files/23002434/Histopathological.Image.Segmentation.Report.pdf)
