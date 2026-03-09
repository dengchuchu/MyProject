# 本脚本运行方式为在终端运行命令：streamlit run D:\MyPython\Essay01\GUI.py
import os
import joblib
import numpy as np
import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))
model_filename = "ML model.joblib"
scaler_filename = "StandardScaler.joblib"
model_path = os.path.join(current_dir, model_filename)
scaler_path = os.path.join(current_dir, scaler_filename)
model = joblib.load(model_path)
ss = joblib.load(scaler_path)

col1, col2, col3 = st.columns(3)

with col1:
    col1.subheader(':red[]')
    feature1 = st.number_input(u'$\mathrm{SBET\;(m²/g)}$', step=0.01, format='%.2f')
    feature2 = st.number_input(u'$\mathrm{Vtotal\;(cm³/g)}$', step=0.001, format='%.3f')
    feature3 = st.number_input(u'$\mathrm{Dp\;(nm)}$', step=0.001, format='%.3f')

with col2:
    col2.subheader(':blue[]')
    feature4 = st.number_input(u'$\mathrm{C}$', step=0.01, format='%.2f')
    feature5 = st.number_input(u'$\mathrm{H}$', step=0.01, format='%.2f')
    feature6 = st.number_input(u'$\mathrm{O}$', step=0.01, format='%.2f')
    feature7 = st.number_input(u'$\mathrm{N}$', step=0.01, format='%.2f')

with col3:
    col3.subheader(':orange[]')
    feature8 = st.number_input(u'$\mathrm{Dosage\;(g/L)}$', step=0.001, format='%.3f')
    feature9 = st.number_input(u'$\mathrm{Initial\;concentration\;(mg/L)}$', step=0.001, format='%.3f')
    feature10 = st.number_input(u'$\mathrm{Temperature\;(K))}$', step=0.01, format='%.2f')
    feature11 = st.number_input(u'$\mathrm{Initial\;pH}$', step=0.1, format='%.1f')
feature_values = [feature1, feature2, feature3, feature4, feature5, feature6, feature7,
                  feature8, feature9, feature10, feature11]

if st.button('Predict', type='primary'):
    # 简单的验证：检查是否所有输入都为0（可选，防止用户未输入直接点击）
    if all(f == 0.0 for f in feature_values):
        st.warning("检测到所有输入均为0，请确认输入参数是否正确。")
    else:

        try:
            input_data = np.array([feature_values])
            input_data_scaled = ss.transform(input_data)
            prediction = model.predict(input_data_scaled)
            result = prediction[0]

            if result < 0:
                st.error(
                    "❌ **输入参数有误**：模型预测结果为负数，这在物理上是不可能的。请检查输入值是否在合理范围内，或是否超出了模型的训练域。")
            else:
                st.success(f'✅ Predicted adsorption capacity: {result:.2f} mg/g')

        except Exception as e:
            st.error(f"预测过程中发生错误：{e}")
