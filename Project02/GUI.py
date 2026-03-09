# 本脚本运行方式为在终端运行命令：streamlit run D:\MyPython\Essay02\GUI.py
import joblib
import numpy as np
import streamlit as st

model = joblib.load('D:\MyPython\Essay02\ML model.joblib')
ss = joblib.load('D:\MyPython\Essay02\StandardScaler.joblib')

col1, col2, col3 = st.columns(3)

with col1:
    col1.subheader(':red[]')
    feature1 = st.number_input(u'$\mathrm{Pyrolysis\_temp}$', step=0.1, format='%.1f')
    feature2 = st.number_input(u'$\mathrm{Heating\;rate\;(oC)}$', step=0.1, format='%.1f')

with col2:
    col2.subheader(':blue[]')
    feature3 = st.number_input(u'$\mathrm{Pyrolysis\_time\;(min)}$', step=0.1, format='%.1f')
    feature4 = st.number_input(u'$\mathrm{C}$', step=0.001, format='%.3f')
    feature5 = st.number_input(u'$\mathrm{H}$', step=0.001, format='%.3f')
    feature6 = st.number_input(u'$\mathrm{O}$', step=0.001, format='%.3f')
    feature7 = st.number_input(u'$\mathrm{N}$', step=0.001, format='%.3f')
    feature8 = st.number_input(u'$\mathrm{H/C}$', step=0.001, format='%.3f')
    feature9 = st.number_input(u'$\mathrm{O/C}$', step=0.001, format='%.3f')
    feature10 = st.number_input(u'$\mathrm{N/C}$', step=0.001, format='%.3f')
    feature11 = st.number_input(u'$\mathrm{(O+N/C)}$', step=0.001, format='%.3f')

with col3:
    col3.subheader(':orange[]')
    feature12 = st.number_input(u'$\mathrm{Surface\;area}$', step=0.01, format='%.2f')
    feature13 = st.number_input(u'$\mathrm{Pore\;volume}$', step=0.001, format='%.3f')
    feature14 = st.number_input(u'$\mathrm{Average\;pore\;size}$', step=0.001, format='%.3f')
    feature15 = st.number_input(u'$\mathrm{Adsorption\_time\;(min)}$', step=0.1, format='%.1f')
    feature16 = st.number_input(u'$\mathrm{Ci\_ppm}$', step=0.01, format='%.2f')
    feature17 = st.number_input(u'$\mathrm{solution\;pH}$', step=0.1, format='%.1f')
    feature18 = st.number_input(u'$\mathrm{rpm}$', step=0.1, format='%.1f')
    feature19 = st.number_input(u'$\mathrm{Adsorbent\;usage\;(g/L)}$', step=0.01, format='%.2f')
    feature20 = st.number_input(u'$\mathrm{adsorption\_temp}$', step=0.1, format='%.1f')
    feature21 = st.number_input(u'$\mathrm{Cf}$', step=0.01, format='%.2f')
feature_values = [feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9,
                  feature10, feature11, feature12, feature13, feature14, feature15, feature16, feature17,
                  feature18, feature19, feature20, feature21]

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
