vowels = "aiueo"
ip_str = "Halo nama saya Seviko Attalarik Pramayudha Handoko saya sedang belajar python"
ip_str = ip_str.casefold()

count = {}.fromkeys(vowels, 0)

for char in ip_str :
    if char in count:
        count[char] += 1
    
print(count)