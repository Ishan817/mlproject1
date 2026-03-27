import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)


st.markdown("<h1>🚗 Car Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("##### ML-Powered · Used Cars · Indian Market")
st.divider()

col1, col2 = st.columns(2)

with col1:
    car_name = st.text_input("Car Name", placeholder="e.g. Swift, Innova, i20")
    present_price = st.number_input("Showroom Price (Lakhs)", min_value=0.5, max_value=100.0, value=6.0, step=0.1)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, max_value=500000, value=30000, step=1000)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])

with col2:
    car_age = st.slider("Car Age (Years)", min_value=1, max_value=20, value=5)
    owner = st.selectbox("Previous Owners", [0, 1, 2, 3])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

selling_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
st.write("Button aane wala hai!")

if st.button("🔍 Predict Price"):
    fuel_enc  = encoders['Fuel_Type'].transform([fuel_type])[0]
    sell_enc  = encoders['Selling_type'].transform([selling_type])[0]
    trans_enc = encoders['Transmission'].transform([transmission])[0]

    features = np.array([[present_price, kms_driven, fuel_enc,
                          sell_enc, trans_enc, owner, car_age]])

    pred = max(0.1, model.predict(features)[0])
    dep  = ((present_price - pred) / present_price) * 100

    st.markdown(f"""
    <div style="background:#1a1a1a; border:2px solid #f5c518; border-radius:12px;
                padding:25px; text-align:center; margin-top:20px;">
        <div style="color:#aaa; font-size:12px; letter-spacing:3px;">ESTIMATED SELLING PRICE</div>
        <div style="font-size:3rem; font-weight:800; color:#f5c518;">₹ {pred:.2f} Lakhs</div>
        <div style="color:#888; font-size:13px; margin-top:8px;">
            📉 Depreciation: {dep:.1f}% &nbsp;|&nbsp;
            ⛽ {fuel_type} &nbsp;|&nbsp;
            🔧 {transmission} &nbsp;|&nbsp;
            📅 {car_age} yr old
        </div>
    </div>
    """, unsafe_allow_html=True)