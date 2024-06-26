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

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Sample",
        page_icon="👋",
    )

    # st.write("# Welcome to Streamlit! 👋")
    st.markdown('# Sample')

    option = st.selectbox("カテゴリを選択してください。", ("ヘルスケア", "アパレル", "調理器具", "その他"))
    st.write("選択したカテゴリは", option, "です。")

    number = st.number_input("金額を入力してください。", step=1)
    st.write("入力した金額は ", number, "円です。")
    st.divider()
    pred = (-0.00636949 * number) + 512.953 # 単回帰モデルで求めたパラメータを使用(精度はサンプルなので気にしないでください)
    if pred < 5:
      pred = 5 # 負の値はわかりづらいと思ったので。
    st.write("予想件数:  ", int(pred))
    st.write("注意！！サンプルなので精度は気にしないでください。")
    st.divider()

    if pred > 512:
      score = 5
    elif pred >= 470:
      score = 4
    elif pred >= 455:
      score = 3
    elif pred >= 425:
      score = 2
    else:
      score = 1
    st.write("5段階評価:  ", score)


if __name__ == "__main__":
    run()
