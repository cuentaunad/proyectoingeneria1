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
import datetime

def reg_mer():
    name = st.text_input('Nombre producto - Escriba', '')
    last_name = st.text_input('Descripción -  Escriba', '')
    d = st.date_input("Fecha de ingreso -  Escoja en el calendario", datetime.date(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day))
    number = st.number_input('SKU',format="%d", value=0)
    uploaded_files = st.file_uploader("Subir foto del producto", accept_multiple_files=True)
    st.button('Guardar')

