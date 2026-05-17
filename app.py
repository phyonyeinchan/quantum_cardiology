import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit_machine_learning.algorithms import VQC
from qiskit_algorithms.optimizers import COBYLA

# ၁။ Web App ၏ ခေါင်းစဉ်နှင့် မျက်နှာစာ အလှဆင်ခြင်း
st.set_page_config(page_title="Quantum Cardiology Dashboard", layout="wide")
st.title("⚛️ Quantum AI Cardiology Dashboard")
st.write("Causal Inference & Propensity Score Estimation using Variational Quantum Classifier (VQC)")

# ၂။ Background မှာ Data နှင့် Quantum Model ကို တစ်ခါတည်း Train ထားခြင်း
@st.cache_resource
def train_quantum_model():
    url = "https://githubusercontent.com"
    df = pd.read_csv(url)
    X_features = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 
                  'ejection_fraction', 'platelets', 'serum_creatinine', 
                  'serum_sodium', 'sex', 'smoking']
    
    X = df[X_features]
    w = df['high_blood_pressure'] # Treatment
    
    X_train, X_test, w_train, w_test = train_test_split(X, w, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    num_qubits = X_train_scaled.shape[1]
    feature_map = ZZFeatureMap(feature_dimension=num_qubits, reps=1, entanglement='linear')
    ansatz = RealAmplitudes(num_qubits=num_qubits, reps=1)
    
    optimizer = COBYLA(maxiter=15)
    vqc = VQC(feature_map=feature_map, ansatz=ansatz, optimizer=optimizer)
    vqc.fit(X_train_scaled, w_train.values)
    
    return vqc, scaler

with st.spinner("Training Quantum Model on Background... Please wait..."):
    vqc, scaler = train_quantum_model()
st.success("Quantum VQC Model is Ready!")

# ၃။ Sidebar တွင် လူနာအချက်အလက်များကို Interactive ရွေးချယ်နိုင်ရန် ပြုလုပ်ခြင်း
st.sidebar.header("👤 Patient Clinical Parameters")
age = st.sidebar.slider("Age (အသက်)", 20, 100, 60)
anaemia = st.sidebar.selectbox("Anaemia (သွေးအားနည်းရောဂါ)", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
cpk = st.sidebar.number_input("Creatinine Phosphokinase", 10, 8000, 250)
diabetes = st.sidebar.selectbox("Diabetes (ဆီးချို)", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
ef = st.sidebar.slider("Ejection Fraction (%)", 10, 80, 38)
platelets = st.sidebar.number_input("Platelets (သွေးဥမွှား)", 25000, 850000, 260000)
sc = st.sidebar.slider("Serum Creatinine", 0.5, 10.0, 1.3)
ss = st.sidebar.slider("Serum Sodium", 100, 150, 136)
sex = st.sidebar.selectbox("Sex (ကျား/မ)", [0, 1], format_func=lambda x: "Female" if x==0 else "Male")
smoking = st.sidebar.selectbox("Smoking (ဆေးလိပ်သောက်ခြင်း)", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")

# ၄။ ရွေးချယ်လိုက်သော လူနာအချက်အလက်ကို Quantum Model ထဲထည့်၍ တွက်ချက်ခြင်း
input_data = np.array([[age, anaemia, cpk, diabetes, ef, platelets, sc, ss, sex, smoking]])
input_scaled = scaler.transform(input_data)

probabilities = vqc.predict_proba(input_scaled)
propensity_score = probabilities[0][1] # တိကျသော Score တန်ဖိုးကို ထုတ်ယူခြင်း

# ၅။ ရလဒ်ကို Dashboard ပေါ်တွင် လှပစွာ ပြသခြင်း
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Estimated Propensity Score (Quantum ML)", value=f"{propensity_score:.4f}")
with col2:
    st.write("### Clinical Interpretation")
    st.write(f"This patient has a **{propensity_score*100:.2f}%** probability of having High Blood Pressure (Treatment condition) based on the 10-Qubit Quantum Variational Classifier.")
