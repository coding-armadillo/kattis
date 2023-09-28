sentence = input()
words = sentence.split()
if len([w for w in words if "ae" in w]) / len(words) >= 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
