import streamlit as st
from consumidor_api import resposta

st.set_page_config(page_title="Monitoramento Meteorológico", page_icon="🌦️")

st.title("🌦️ Monitoramento Meteorológico")
st.caption("Jaraguá do Sul - SC")

if st.button("Atualizar dados"):
    st.rerun()

try:
    dados = resposta.json()

    st.success("Dados carregados com sucesso.")

    col1, col2 = st.columns(2)

    col1.metric("Temperatura", f"{dados["current"]["temperature_2m"]:.1f} °C")
    col1.metric("Umidade", f"{dados["current"]["relative_humidity_2m"]:.0f} %")
    col1.metric("Sensação térmica", f"{dados["hourly"]["apparent_temperature"][0]:.1f} °C")

    col2.metric("Precipitação", f"{dados["hourly"]["precipitation"][0]:.1f} mm")
    col2.metric("Vento", f"{dados["hourly"]["wind_speed_10m"][0]:.1f} km/h")

    st.caption(f"Horário: {dados["hourly"]["time"][0]}")

except Exception as erro:
    st.error(f"Erro ao consultar os dados: {erro}")    