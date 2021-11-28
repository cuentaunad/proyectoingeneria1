# Copyright 2021 henry.carrillo
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import time
import  random
from PIL import Image

def con_mer():
    st.subheader("Consulta de mercancía")

    with st.form("my_form"):
        st.write("Buscador de productos")
        text_input = st.text_input(label='Nombre del producto')

        # Every form must have a submit button.
        submitted = st.form_submit_button("Buscar")
        if submitted:
            with st.spinner('Consultando...'):
                time.sleep(random.randint(1,5))
                image = Image.open('car.jpg')
                st.image(image, caption='Sunrise by the mountains')
                st.success('Done!')