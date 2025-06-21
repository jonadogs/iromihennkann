import streamlit as st

st.title("CMYK 補正値 自動計算（引き算バージョン）")

correction_per_unit = st.number_input("0.01あたりの補正（％）", 0.0, 10.0, 0.5, step=0.1)

st.subheader("元のCMYK値（％）を入力してな")
orig_C = st.number_input("元のC (%)", 0.0, 100.0, 78.0, step=0.1)
orig_M = st.number_input("元のM (%)", 0.0, 100.0, 76.0, step=0.1)
orig_Y = st.number_input("元のY (%)", 0.0, 100.0, 24.0, step=0.1)
orig_K = st.number_input("元のK (%)", 0.0, 100.0, 3.0, step=0.1)

st.subheader("測定誤差（正なら多い、負なら少ない）を入力してな")
meas_C = st.number_input("測定C誤差", -5.0, 5.0, 0.02, step=0.01)
meas_M = st.number_input("測定M誤差", -5.0, 5.0, 0.00, step=0.01)
meas_Y = st.number_input("測定Y誤差", -5.0, 5.0, 0.01, step=0.01)
meas_K = st.number_input("測定K誤差", -5.0, 5.0, -0.01, step=0.01)

if st.button("修正後のCMYKを計算するで！"):
    def corrected(orig, meas):
        correction = meas * correction_per_unit * 100
        val = orig - correction
        return max(0.0, min(100.0, val))

    corrected_C = corrected(orig_C, meas_C)
    corrected_M = corrected(orig_M, meas_M)
    corrected_Y = corrected(orig_Y, meas_Y)
    corrected_K = corrected(orig_K, meas_K)

    st.write("✅ 修正後のCMYK値（％）やで！")
    st.write(f"C: {corrected_C:.2f}%")
    st.write(f"M: {corrected_M:.2f}%")
    st.write(f"Y: {corrected_Y:.2f}%")
    st.write(f"K: {corrected_K:.2f}%")
