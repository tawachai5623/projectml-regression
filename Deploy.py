import streamlit as st
import numpy as np
import joblib

# โหลดโมเดลที่ถูกฝึกแล้ว
model_filename = 'CountCaloriesModel.sav'
lr = joblib.load(model_filename)

# ฟังก์ชันสำหรับการทำนายพลังงาน (Calories) จากโมเดลที่โหลดมา
def predict_calories(total_fat_g, trans_fat_g, saturated_fat_g, sodium_mg, total_carbohydrates_g, cholesterol_mg, dietary_fibre_g, sugar_g, protein_g, Vitamin_A_DV, Vitamin_C_DV, calcium_DV, iron_DV, caffeine_mg):
    Vitamin_A_DV /= 100
    Vitamin_C_DV /= 100
    calcium_DV /= 100
    iron_DV /= 100
    caffeine_mg /= 100

    input_data = np.array([[total_fat_g, trans_fat_g, saturated_fat_g, sodium_mg, total_carbohydrates_g, cholesterol_mg, dietary_fibre_g, sugar_g, protein_g, Vitamin_A_DV, Vitamin_C_DV, calcium_DV, iron_DV, caffeine_mg]])

    prediction = lr.predict(input_data)

    return round(prediction[0], 2)

# ส่วนหัวของเว็บ
st.title("Count Your Calories")
st.write("กรอกข้อมูลด้านล่างเพื่อดูผลการทำนายพลังงาน")

# แบ่งอินพุตออกเป็นคอลัมน์
col1, col2 = st.columns(2)

with col1:
    total_fat_g = st.number_input("Total Fat (g)", min_value=0.0)
    trans_fat_g = st.number_input("Trans Fat (g)", min_value=0.0)
    saturated_fat_g = st.number_input("Saturated Fat (g)", min_value=0.0)
    sodium_mg = st.number_input("Sodium (mg)", min_value=0.0)
    total_carbohydrates_g = st.number_input("Total Carbohydrates (g)", min_value=0.0)
    cholesterol_mg = st.number_input("Cholesterol (mg)", min_value=0.0)
    dietary_fibre_g = st.number_input("Dietary Fibre (g)", min_value=0.0)
with col2:    
    sugar_g = st.number_input("Sugar (g)", min_value=0.0)
    protein_g = st.number_input("Protein (g)", min_value=0.0)
    Vitamin_A_DV = st.number_input("Vitamin A (%DV)", min_value=0.0)
    Vitamin_C_DV = st.number_input("Vitamin C (%DV)", min_value=0.0)
    calcium_DV = st.number_input("Calcium (%DV)", min_value=0.0)
    iron_DV = st.number_input("Iron (%DV)", min_value=0.0)
    caffeine_mg = st.number_input("Caffeine (mg)", min_value=0.0)

# แสดงปุ่มทำนายและผลลัพธ์
if st.button("Predict Calories"):
    result = predict_calories(total_fat_g, trans_fat_g, saturated_fat_g, sodium_mg, total_carbohydrates_g, cholesterol_mg, dietary_fibre_g, sugar_g, protein_g, Vitamin_A_DV, Vitamin_C_DV, calcium_DV, iron_DV, caffeine_mg)
    st.success(f"Predicted Calories: {result} kcal")
