# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
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
from streamlit.logger import get_logger
import requests
import os

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

    url = "https://api.together.xyz/v1/images/generations"
    
    payload = {
        "prompt": "cat floating in space, cinematic",
        "model": "stabilityai/stable-diffusion-xl-base-1.0",
        "steps": 20,
        "n": 1,
        "height": 1024,
        "width": 1024
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer 87f9262fea2d4be229dcd50e8bfaec073709d02a7ec24d55f2820bb77c97c863"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    st.write(response.text)





if __name__ == "__main__":
    os.environ["TOGETHER_API_KEY"] = "87f9262fea2d4be229dcd50e8bfaec073709d02a7ec24d55f2820bb77c97c86387f9262fea2d4be229dcd50e8bfaec073709d02a7ec24d55f2820bb77c97c863"
    run()
