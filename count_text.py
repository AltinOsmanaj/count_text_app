import streamlit as st
from io import StringIO

st.title("Count text")

def count_word(name_file: str) -> list:
    # read file
    vaporat = name_file

    # read lines
    vaporat_list = vaporat.readlines()
    rez_list = []
    for i in vaporat_list:
        if i == '\n':
            continue
        rez_list.append(i.replace('\n', '').split())

    # count words from a list
    count_word = {}
    for lst in rez_list:
        for word in lst:
            word = word.upper()
            if word not in count_word:
                count_word[word] = 1
            else:
                count_word[word] += 1

    # sort the dictionary
    sorted_list = sorted(count_word.items(), key=lambda x: x[1], reverse=True)

    # return the output
    return sorted_list

def convert_to_file(sorted_list) -> str:
    with open('result_count.txt', 'w') as vaporat_upper:
        for row in sorted_list:
            word = f'The word >> {row[0]} << occurs {row[1]} times !'
            vaporat_upper.write(word + '\n')
    return "File has been written successfully."

file_in = st.file_uploader("Please upload a file: ")
if file_in is not None:
    file_in_read = StringIO(file_in.getvalue().decode("utf-8"))
    file_str = count_word(file_in_read)
    st.write(file_str)

    vaporat_upper_str = convert_to_file(file_str)

    st.write(vaporat_upper_str)

    data_str = ""
    for row in file_str:
        word = f'The word >> {row[0]} << occurs {row[1]} times !\n'
        data_str += word

    st.download_button(
        label="Download data as CSV",
        data=data_str,
        file_name='large_df.txt',
        mime='text/csv',
    )