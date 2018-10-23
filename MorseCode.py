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
def convert_word(sent, dict=morse):
    newSent = ""
    sent = sent.lower()
    for i in sent:
        if i in dict:
            newSent += dict[i] + " "
        else:
            newSent += i

    print(newSent)

sentence = input("Enter a sentence: ")
convert_word(sentence)
