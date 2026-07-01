# Project Name: Hallucination Detection & Mitigation

A structured, modular deep learning pipeline designed for detecting and analyzing hallucinations in model outputs. This repository contains the complete workflow from data preprocessing and training to evaluation and inference.

## 📂 Project Structure

```text
hallucination/
│
├── .venv/              # Python virtual environment
├── checkpoints/        # Saved model weights (.pt or .pth) during training
│
├── configs/            # Configuration files (YAML) for experiments
│   └── baseline.yaml
│
├── data/               # Raw and processed data splits
│   ├── dataset samples.json
│   ├── sample_submission.csv
│   ├── test.csv
│   └── train.csv
│
├── logs/               # Training logs, console dumps, and run histories
│
├── notebooks/          # Jupyter notebooks for EDA and prototyping
│   └── eda.ipynb
│
├── outputs/            # Evaluation metrics and training loss plots
│
├── scripts/            # Independent scripts for utility tasks and extra tests
│   ├── eda.py
│   ├── json_to_csv.py
│   └── test_banglabert.py
│
├── src/                # Core source code modules
│   ├── dataset.py      # Custom Dataset and PyTorch DataLoader logic
│   ├── inference.py    # Inference utilities for model predictions
│   ├── metrics.py      # Evaluation metrics (e.g., Accuracy, F1, BLEU/ROUGE)
│   ├── model.py        # Model architecture and network definition
│   ├── trainer.py      # Training loop, validation logic, and early stopping
│   └── utils.py        # Helper functions (logging, seeding, I/O)
│
├── submissions/        # Generated final predictions / submission files
│
├── .gitignore          # Git ignore file
├── infer.py            # Main script to run model evaluation/inference
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
├── test_env.py         # Script to test your local environment configuration
└── train.py            # Main script to trigger model training