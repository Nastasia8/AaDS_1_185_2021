text = "Hello hi how hello are and you I am fine thank you and you hello You Thank And".lower().split()
slov = {i: text.count(i) for i in text}
print(slov)