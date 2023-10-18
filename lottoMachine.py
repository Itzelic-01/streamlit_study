import streamlit as st
import random
import datetime
from PIL import Image

image = Image.open('money.jpeg')

st.image(image, caption="It's Your Tomorrow")
st.title(':moneybag:로또번호 생성기:moneybag:')


def generate_lotto():
    lotto = set()

    while len(lotto) < 6:
        number = random.randint(1, 46)
        lotto.add(number)

    lotto = list(lotto)
    lotto.sort()
    return lotto

# st.subheader(f'행운의 번호: :green[{generate_lotto()}]')
# st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

button = st.button('이번주 당첨 번호 보기')

if button:
    for i in range(1, 6):
        st.subheader(f'{i}. 행운의 번호: :green[{generate_lotto()}]')
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
