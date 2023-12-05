from pyscript import document


def str_to_binary(str_txt):
    binary_val = ''.join(format(ord(i), '08b') for i in str_txt)
    return binary_val

def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    binary_val = str_to_binary(str(output_div))
    output_div.innerText = binary_val
    
def clear_text(mango):
    output_div = document.querySelector("#output")
    output_div.innerText = ""
