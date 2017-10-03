phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(8,11):
    plist.pop()
plist.remove("'")
plist.remove("D")
plist.pop()
plist.append(plist.pop(4))
plist.insert(2,plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
