name_1 = input("what your name?:").lower()
name_2 = input("What is the name of the intended?:").lower()
name_3 = name_1 + name_2
len_name = len(name_3)
percent = "The compatibility between you is:"

t = name_3.count("t")
if t > 0:
    t = 1
else:
    t = 0
r = name_3.count("r")
if r > 0:
    r = 1
else:
    r = 0
u = name_3.count("u")
if u > 0:
    u = 1
else:
    u = 0
e = name_3.count("e")
if e > 0:
    e = 1
else:
    e = 0
l = name_3.count("l")
if l > 0:
    if  l < 2:
        l = 1
    else:
        l = 2
else:
    l = 0
o = name_3.count("o")
if o > 0:
    o = 1
else:
    o = 0
v = name_3.count("v")
if v > 0:
    v = 1
else:
    v = 0
number = t + r + u + e + l + o + v
percent_ = int(number * 100 / len_name)
if percent_ <= 10:
    print(f"{percent}{percent_}% \nGo to: \"chatuna mimabat reshon\"")
elif percent_ <= 60:
    print(f"{percent}{percent_}% \ngo for it. You have a reasonable chance.")
else:
    print(f"{percent}{percent_}% \nWow that's great!!!")

