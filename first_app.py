import streamlit as st

x1=st.slider('peso in kg', 0, 120, 50)
x2=st.slider('altezza in m', 0.0, 2.0, 1.5)


def bmi(a:float,b:float):
    bmi=a/(b*b)
    return bmi

bmi= bmi(x1,x2)
#st.write(bmi)

if 16< bmi <19:
    st.write('il tuo bmi è', round(bmi,2), 'sei sottopeso')
elif  19< bmi <25:
    st.write('il tuo bmi è', round(bmi,2), 'sei normopeso')
else:#elif 25< bmi <30:
    st.write('il tuo bmi è', round(bmi,2), 'sei sovrappeso')

if st.button('baloons'):
    st.balloons()

