# HISAC
Histopathological Image Segmentation and Classifier

---
Histopathological image analysis, including biopsy image segmentation and classification, is an important field in digital pathology that uses advanced computational techniques to analyze microscopic images of tissue samples. This process aids pathologists in diagnosing diseases, particularly cancer.

# Overview
This project implements automated nucleus segmentation on the MoNuSeg dataset using deep learning.
It compares a U-Net baseline with a BASNet-inspired boundary-aware model, designed to accurately detect and delineate cell nuclei boundaries in histopathological images.

We introduce a hybrid loss (Dice + Focal + SSIM) that balances overlap accuracy, hard-pixel learning, and structural consistency.
The model achieves consistent improvements across Dice, IoU, and Boundary F1 metrics.

## Project Report
[Histopathological Image Segmentation Report.pdf](https://github.com/user-attachments/files/23002434/Histopathological.Image.Segmentation.Report.pdf)
