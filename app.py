import streamlit as st
import pandas as pd

# Dummy function to calculate NPK values
def get_best_npk(latitude, longitude, ph, moisture, soil_texture):
    # These are dummy values. You can replace this logic with a real ML model later.
    if ph > 7:
        npk = {'N': 90, 'P': 40, 'K': 30}
    else:
        npk = {'N': 80, 'P': 35, 'K': 25}
    
    if soil_texture == "Sandy":
        npk['N'] += 5
    
    npk['P'] += int(moisture * 0.1)  # Just an example logic
    
    return npk

# Streamlit app
def main():
    st.title("NPK Recommendation System")
    
    # Input for coordinates
    st.subheader("Enter Coordinates")
    latitude = st.number_input("Latitude", format="%.6f", value=0.0)
    longitude = st.number_input("Longitude", format="%.6f", value=0.0)
    
    # Input for other soil characteristics
    st.subheader("Soil Characteristics")
    ph = st.slider("Soil pH", 0.0, 14.0, 7.0)
    moisture = st.slider("Soil Moisture (%)", 0, 100, 50)
    soil_texture = st.selectbox("Soil Texture", ["Sandy", "Clayey", "Loamy", "Silty"])
    
    # When the user clicks the "Submit" button, calculate the NPK values
    if st.button("Get Best NPK Values"):
        npk_values = get_best_npk(latitude, longitude, ph, moisture, soil_texture)
        st.subheader("Recommended NPK Values")
        st.write(f"Recommended Nitrogen (N): {npk_values['N']} kg/ha")
        st.write(f"Recommended Phosphorus (P): {npk_values['P']} kg/ha")
        st.write(f"Recommended Potassium (K): {npk_values['K']} kg/ha")
    
    # Display a table of the dummy results
    st.subheader("Sample Data")
    df = pd.DataFrame({
        'Latitude': [12.9716, 13.0827],
        'Longitude': [77.5946, 80.2707],
        'pH': [6.5, 7.2],
        'Moisture (%)': [55, 45],
        'Soil Texture': ['Loamy', 'Clayey'],
        'N (kg/ha)': [85, 90],
        'P (kg/ha)': [36, 38],
        'K (kg/ha)': [28, 32]
    })
    st.dataframe(df)

if __name__ == "__main__":
    main()
