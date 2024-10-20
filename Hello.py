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
import json
from PIL import Image
from io import BytesIO

LOGGER = get_logger(__name__)
st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )


def run(user_prompt,selected_model):

    url = "https://api.together.xyz/v1/images/generations"
    
    payload = {
        "prompt": user_prompt,
        "model": selected_model,
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
    response = response.text

    json_data = json.loads(response)
    url = json_data["data"][0]["url"]
    st.image(url)





if __name__ == "__main__":

    st.title("🤖 Image Generation with together & models")

    model_options = {
        "Flux Pro": "fal-ai/flux-pro",
        "Flux Dev": "fal-ai/flux/dev",
        "Flux Schnell": "fal-ai/flux/schnell",
        "Flux Realism": "fal-ai/flux-realism",
        "stabilityai/stable-diffusion-xl-base-1.0": "stabilityai/stable-diffusion-xl-base-1.0"
    }

    selected_model = st.selectbox("Select Model:", list(model_options.keys()), index=4)

    image_size = st.selectbox("Image Size:", ["square_hd", "square", "portrait_4_3", "portrait_16_9", "landscape_4_3", "landscape_16_9"], index=0)

    # Initialize session state
    if 'user_prompt' not in st.session_state:
        st.session_state.user_prompt = ""
    if 'tuned_prompt' not in st.session_state:
        st.session_state.tuned_prompt = ""
    if 'prompt_accepted' not in st.session_state:
        st.session_state.prompt_accepted = False

    # User input for the prompt
    user_prompt = st.text_input("Enter your image prompt:", value=st.session_state.user_prompt)

    # Update session state when user types in the input field
    if user_prompt != st.session_state.user_prompt:
        st.session_state.user_prompt = user_prompt
        st.session_state.prompt_accepted = False

    if st.button("☁️ Generate Image",type="primary"):
        if not user_prompt:
            st.warning("⛔️ Please enter a prompt for image generation.")
        # Display the prompt being used
        st.subheader("☁️ Generating image with the following prompt:")
        st.info(user_prompt)

        run(user_prompt,selected_model)

        # Display the generated image and save it along with Markdown data
        

        


    ##

