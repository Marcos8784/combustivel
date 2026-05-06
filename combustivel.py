import streamlit as st
st.title(' marcos vinicios')
st.subheader('gasolina x etanol⛽')
gasolina = st.number_input('digite o valor da gasolina:', min_value=0.0)
etanol = st.number_input('digite o valor do etanol:🍃🍂🌿🍀🍁', min_value=0.0)
if gasolina > 0:
    resultado = etanol / gasolina
    if resultado < 0.70:
        mg= 'abasteça com etanol chefe  🪨✌️'
    else:
        mg ='abasteça com gasolina chefe! ⛽else: '
else:
    st.write("digite um valor acima de 0")

if st.button('calcular'):
    st.info(mg)