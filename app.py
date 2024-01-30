# _*_ coding:utf-8 _*_

import streamlit as st
import seaborn as sns


def main():
    st.title("Hello")
    iris = sns.load_dataset("iris")

if __name__ == "__main__":
    main()
    