# Quantum Machine Learning for Causal Inference in Cardiovascular Epidemiology

This repository applies a **Variational Quantum Classifier (VQC)** using **IBM Qiskit** to estimate propensity scores for causal inference, utilizing clinical records of heart failure patients. This methodology provides a quantum-enhanced approach to risk stratification and confounding adjustment in observational data.

## 🌟 Research Highlights
- **Epidemiological Context:** Focuses on adjusting confounding biases in cardiovascular cohort studies.
- **Quantum Advantage Exploration:** Utilizes high-dimensional Hilbert spaces via Quantum Feature Maps to capture complex interactions among clinical covariates.
- **Hardware Optimized:** Developed and executed natively using local quantum simulators optimized for Apple Silicon (M4 architecture).

## 🛠 Project Structure
- `preprocessing.ipynb`: Data ingestion, inspection, train/test splitting, and feature scaling (`StandardScaler`).
- `quantum_causal_model.ipynb`: End-to-end integration of dataset loading, 10-Qubit Quantum Circuit design, and VQC model training.

## 📊 Technical Specifications
- **Dataset:** Heart Failure Clinical Records (299 patients, 10 clinical confounding features).
- **Quantum Mapping:** 10-Qubit configuration leveraging `ZZFeatureMap` (linear entanglement, 1 rep).
- **Ansatz & Optimization:** `RealAmplitudes` (1 rep) driven by the `COBYLA` classical optimizer (max 20 iterations).

## 🚀 How to Run Locally

### 1. Prerequisites
Ensure you have Python 3.9+ and the required packages installed:
```bash
pip install qiskit qiskit-machine-learning pandas scikit-learn numpy
```

### 2. Execution
Open the project folder in VS Code and run `quantum_causal_model.ipynb` using your local Jupyter kernel.

## 🎖 Verified IBM Quantum Credentials

<table border="0">
  <tr>
    <td>
      <a href="https://www.credly.com/badges/c13b4d21-4c38-4b28-9128-90fa3984c81d/public_url">
        <img src="https://images.credly.com/size/220x220/images/6474ba18-3b83-4a34-878d-158e5869a20d/Quantum_20Machine_20Learning.png">
      </a>
    </td>
    <td>
      <a href="https://www.credly.com/badges/79bc0d5d-81cd-4aaf-8dc8-cb3d28820d70/public_url">
        <img src="https://images.credly.com/size/220x220/images/60cbe993-f35f-4b98-b7f6-8cd51233fe2a/image.png">
      </a>
    </td>
  </tr>
</table>


<a href="https://www.credly.com/badges/c13b4d21-4c38-4b28-9128-90fa3984c81d/public_url">
  <img src="https://credly.com" width="130" alt="QML Badge">
</a>
