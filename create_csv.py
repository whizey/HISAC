import pandas as pd

# Define the table as a list of dictionaries
data = [
    {
        "Author(s)": "Neeraj Kumar et al.",
        "Methodology": "Fully Convolutional Networks (U-Net, FCN, Mask-RCNN) with watershed post-processing",
        "Evaluation Metric": "Average Jaccard Index (AJI)",
        "Dataset Used": "MoNuSeg",
        "Research Gap": "Generalizability to unseen organs, variation in nuclei appearance"
    },
    {
        "Author(s)": "Oscar Cuadros Linares et al.",
        "Methodology": "Fast Otsu algorithm, Super-pixel-based filter, Gaussian blur filter",
        "Evaluation Metric": "Average Jaccard Index",
        "Dataset Used": "Two publicly available datasets",
        "Research Gap": "Scalability for large, high-resolution images"
    },
    {
        "Author(s)": "Amirreza Mahbod et al.",
        "Methodology": "Dual Decoder U-Net-based model with watershed algorithm",
        "Evaluation Metric": "Panoptic Quality (PQ)",
        "Dataset Used": "CryoNuSeg, NuInsSeg, MoNuSAC",
        "Research Gap": "Robustness of segmentation for different tissue processing techniques"
    },
    {
        "Author(s)": "Andrew Lagree et al.",
        "Methodology": "U-Net, Mask R-CNN, GB U-Net",
        "Evaluation Metric": "Aggregated Jaccard Index (AJI), Mean Average Precision (mAP)",
        "Dataset Used": "MoNuSeg, TNBC",
        "Research Gap": "Evaluating model generalizability across different organs"
    },
    {
        "Author(s)": "Zongyi Li et al.",
        "Methodology": "FusionU-Net: U-Net with enhanced skip connection",
        "Evaluation Metric": "Custom segmentation metrics",
        "Dataset Used": "Multiple pathology datasets",
        "Research Gap": "Addressing the semantic gap between encoder and decoder"
    },
    {
        "Author(s)": "Haigen Hu et al.",
        "Methodology": "MC-Unet with multi-scale convolution blocks",
        "Evaluation Metric": "Dice Similarity Coefficient (DSC), IoU, Precision, Sensitivity",
        "Dataset Used": "T24 (bladder cancer), MoNuSeg",
        "Research Gap": "Small feature and weak boundary segmentation"
    },
    {
        "Author(s)": "Yanning Zhou et al.",
        "Methodology": "CIA-Net: Contour-Aware Information Aggregation Network with smooth truncated loss",
        "Evaluation Metric": "AJI, F1-Score",
        "Dataset Used": "MoNuSeg",
        "Research Gap": "Dealing with noisy annotations and generalizing to unseen data"
    },
    {
        "Author(s)": "Fabian Isensee et al.",
        "Methodology": "nnU-Net: Self-configuring U-Net-like architecture with dynamic rule-based pipeline configuration",
        "Evaluation Metric": "Dice Coefficient, Cross-Entropy Loss",
        "Dataset Used": "Medical Segmentation Decathlon (MSD), KiTS, CHAOS datasets, etc.",
        "Research Gap": "Automating segmentation pipeline configuration for different biomedical datasets"
    }
]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('segmentation_papers_summary.csv', index=False)

print("CSV file 'segmentation_papers_summary.csv' has been created.")
