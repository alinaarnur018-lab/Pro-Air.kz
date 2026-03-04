import streamlit as st

def calculate_aqi(pm):
    # Твоя формула из Untitled3.ipynb
    if pm <= 12: aqi = pm * 4.1
    elif pm <= 35.4: aqi = 50 + (pm - 12.1) * 2.1
    elif pm <= 55.4: aqi = 100 + (pm - 35.5) * 2.5
    elif pm <= 150.4: aqi = 150 + (pm - 55.5) * 0.52
    else: aqi = 200
    return int(aqi)

st.title("🛡️ A.L.G.O.R.I.T.H.M. Dashboard")

# Слайдер для теста (имитация датчика на сайте)
pm_val = st.slider("Текущий уровень PM2.5 в Алматы (мкг/м³)", 0, 200, 45)
aqi_res = calculate_aqi(pm_val)

st.metric("Рассчитанный AQI (по вашей формуле)", aqi_res)

st.subheader("Инновация: Стимул или Налог")
if aqi_res > 120:
    st.error("🚨 Внимание! Прогноз смога повышен. Активированы финансовые меры:")
    st.markdown("1. **Стимул (The Carrot):** Вам доступен автокредит под 2.5% на электрокар/гибрид.")
    st.markdown("2. **Налог (The Stick):** Введен временный экологический сбор для ТС ниже Euro-4.")
else:
    st.success("Воздух в норме. Экономические ограничения не применяются.")
