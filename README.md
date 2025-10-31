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
* Develop a deep learning-based segmentation system for histopathological nuclei.

* Address boundary blurring and class imbalance using hybrid loss optimization.

* Compare U-Net and BASNet-based architectures quantitatively.

* Evaluate performance using Dice Score, IoU, Pixel Accuracy, and Boundary F1 Score.

## Project Report
[Histopathological Image Segmentation Report.pdf](https://github.com/user-attachments/files/23002434/Histopathological.Image.Segmentation.Report.pdf)
