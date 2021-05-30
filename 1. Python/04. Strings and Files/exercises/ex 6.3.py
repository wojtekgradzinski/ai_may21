def w_counter(text):
    
    text = text.replace("?","").replace(".","")
    clean_text = text.lower().strip().split()
    counter = 0
    for i in clean_text:
        if i == "wood":
            counter =+ 1
    return counter
w_counter(text)        