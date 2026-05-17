# Quantum Machine Learning for Causal Inference in Cardiovascular Epidemiology

This repository applies a **Variational Quantum Classifier (VQC)** using **IBM Qiskit** to estimate propensity scores for causal inference, utilizing clinical records of heart failure patients. This methodology provides a quantum-enhanced approach to risk stratification and confounding adjustment in observational epidemiological data.

## Live Interactive Research Dashboard

[👉 CLICK HERE TO VIEW THE FULL INTERACTIVE REPORT]https://huggingface.co/spaces/phyonyeinchan/quantum-cardiology

## 🎖 Verified IBM Quantum Credentials

The underlying core competencies driving this research are backed by professional IBM Quantum certifications:

<table>
  <tr>
    <td align="center">
      <a href="https://www.credly.com/badges/c13b4d21-4c38-4b28-9128-90fa3984c81d/public_url">
        <img src="https://images.credly.com/size/220x220/images/6474ba18-3b83-4a34-878d-158e5869a20d/Quantum_20Machine_20Learning.png" width="110" alt="Quantum Machine Learning"><br/>
        <sub><b>Quantum Machine Learning</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://www.credly.com/badges/1b2f698d-ac5a-46d1-9b55-64f295028d33/public_url">
        <img src="https://images.credly.com/size/220x220/images/3e026f05-3d63-44a0-9535-ce5c9089a268/Fundamentals_20of_20Quantum_20Algorithms.png" width="110" alt="Fundamentals of Quantum Algorithms"><br/>
        <sub><b>Quantum Algorithms</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://www.credly.com/badges/79bc0d5d-81cd-4aaf-8dc8-cb3d28820d70/public_url">
        <img src="https://images.credly.com/size/220x220/images/60cbe993-f35f-4b98-b7f6-8cd51233fe2a/image.png" width="110" alt="Basics of Quantum Information"><br/>
        <sub><b>Quantum Info Basics</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://www.credly.com/badges/dd8fea00-87ff-41a0-bd52-cacbc74b9238/public_url">
        <img src="https://images.credly.com/size/220x220/images/e934a013-956f-421a-9a3d-668da9eac7ae/General_20Formulation_20of_20Quantum_20Information.png" width="110" alt="General Formulation of Quantum Information"><br/>
        <sub><b>General Formulation</b></sub>
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://www.credly.com/badges/8164796f-e343-45ac-a66e-e57eafbae640/public_url">
        <img src="https://images.credly.com/size/220x220/images/f3ae0407-0eaa-4af7-ab15-0735c81af889/Foundations_20of_20Quantum_20Error_20Correction_20.png" width="110" alt="Foundations of Quantum Error Correction"><br/>
        <sub><b>Error Correction</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://www.credly.com/badges/bc31a16e-8469-4fc1-87d6-c8f2b61cf3b8/public_url">
        <img src="https://images.credly.com/size/220x220/images/53629652-f0f2-4bc8-abfd-444c366d3cf6/image.png" width="110" alt="Practical Introduction to Quantum-Safe Cryptography"><br/>
        <sub><b>Quantum-Safe Crypto</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://www.credly.com/badges/7aa93544-ca9d-41fb-b00a-ede85fe567b5/public_url">
        <img src="https://images.credly.com/size/220x220/images/f786ecd2-dce6-49d1-b7c6-6dcd832f8b14/image.png" width="110" alt="Quantum Business Foundations"><br/>
        <sub><b>Business Foundations</b></sub>
      </a>
    </td>
    <td></td>
  </tr>
</table>

## 🌟 Research Highlights
- **Epidemiological Context:** Focuses on adjusting confounding biases in observational cardiovascular cohort studies.
- **Quantum Advantage Exploration:** Utilizes high-dimensional Hilbert spaces via Quantum Feature Maps to capture complex, non-linear interactions among clinical covariates.
- **Hardware Optimized:** Developed and executed natively using local quantum simulators optimized for Apple Silicon (M4 architecture).

## 🛠 Project Structure
- `preprocessing.ipynb`: Data ingestion, cohort inspection, train/test splitting, and clinical feature scaling using `StandardScaler`.
- `quantum_causal_model.ipynb`: End-to-end implementation including 10-Qubit Quantum Circuit design, embedding clinical parameters, and VQC model training.

## 📊 Technical Specifications
- **Dataset:** Heart Failure Clinical Records (299 patients, 10 clinical confounding features).
- **Quantum Mapping:** 10-Qubit configuration leveraging `ZZFeatureMap` (linear entanglement, 1 rep).
- **Ansatz & Optimization:** `RealAmplitudes` (1 rep) driven by the `COBYLA` classical optimizer (max 20 iterations).

## 🚀 How to Run Locally

### 1. Prerequisites
Ensure you have Python 3.9+ and the required packages installed on your local environment:
```bash
pip install qiskit qiskit-machine-learning pandas scikit-learn numpy
```

### 2. Execution
Open the project folder in VS Code and execute the notebooks using your local Jupyter kernel:
```bash
# Execute end-to-end training
# Current deployment optimized for local Apple Silicon GPU/CPU simulator execution
```
