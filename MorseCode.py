morse = {}
morse['a'] = ".-"
morse['b'] = "-..."
morse['c'] = "-.-."
morse['d'] = "-.."
morse['e'] = "."
morse['f'] = "..-."
morse['g'] = "--."
morse['h'] = "...."
morse['i'] = ".."
morse['j'] = ".---"
morse['k'] = "-.-"
morse['l'] = ".-.."
morse['m'] = "--"
morse['n'] = "-."
morse['o'] = "---"
morse['p'] = ".--."
morse['q'] = "--.-"
morse['r'] = ".-."
morse['s'] = "..."
morse['t'] = "-"
morse['u'] = "..-"
morse['v'] = "...-"
morse['w'] = ".--"
morse['x'] = "-..-"
morse['y'] = "-.--"
morse['z'] = "--.."
morse[" "] = "/"
reverse_morse = {}
for x,y in zip(morse.keys(), morse.values()):
    reverse_morse[y] = x
def convert_word(sent, dict=morse):
    newSent = ""
    sent = sent.lower()
    for i in sent:
        if i in dict:
            newSent += dict[i] + " "
        else:
            newSent += i

    print(newSent)
def convert_morse(sent, dict=reverse_morse):
    newSent = ""
    sent = sent.split(" ")
    for i in sent:
        if i in dict:
            newSent += dict[i]
        else:
            newSent += " "

    print(newSent)

sentence = input("Enter a sentence: ")
convert_word(sentence)

sent = input("Enter morse code:")
convert_morse(sent)
