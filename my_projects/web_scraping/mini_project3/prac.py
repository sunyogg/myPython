# lis = ['sun', 'suy', 'mun', 'anu']

# for i in lis[1:2]:
#     print(i)

# -----------------------------------------------------------

# lis = ['sun[3]', 'suy[21]', 'mun[28]', 'anu[6]']

# n_lis = []
# while lis:
#     x = lis.pop()
#     s = x.split('[')
#     print(s)
#     n_lis.append(s[0])

# print(n_lis)


# -----------------------------------------------------------

# s = "Baby Shark Dance"[3]
# z = s.split('[')
# print(z)

# a = [20]

# print(type(a))
# if type(a) == list:
#     print(True)
# else:
#     print(False)


# -----------------------------------------------------------


# b = 'sunyog'
# a = '[2]'
# z = list(a)
# print(z)
# print(type(a))

# -----------------------------------------------------------
# a = "Bailando"[43]

# # how to convert this into

# a = "Bailando[43]"

# -----------------------------------------------------------


data = ['Baby Shark Dance[3]', 'Despacito[6]', 'Johny Johny Yes Papa[12]', 
    'Shape of You[13]', 'See You Again[15]', 'Bath Song[20]', 
    'Phonics Song with Two Words[21]', 'Uptown Funk[22]', 
    'Learning Colors – Colorful Eggs on a Farm[23]', 
    'Masha and the Bear – Recipe for Disaster[24]', 'Gangnam Style[25]', 
    'Wheels on the Bus[30]', 'Dame Tu Cosita[31]', 'Sugar[32]', 'Roar[33]', 
    'Counting Stars[34]', 'Sorry[35]', 'Thinking Out Loud[36]', 'Axel F[37]', 
    'Girls Like You[38]', 'Faded[39]', 'Dark Horse[40]', 
    'Baa Baa Black Sheep[41]', 'Let Her Go[42]', 'Bailando[43]', 
    'Lean On[44]', 'Shake It Off[45]', 'Perfect[46]', 
    'Waka Waka (This Time for Africa)[47]', 'Mi Gente[48]']



# new_data = []
# newer_data = []

# for element in data:
#     x = element.split('[')
#     new_data.append(x)

# # new_data = [['Baby Shark Dance', '3]'], ['Despacito', '6]'], ['Johny Johny Yes Papa', '12]'], ['Shape of You', '13]'], ['See You Again', '15]'], ['Bath Song', '20]'], ['Phonics Song with Two Words', '21]'], ['Uptown Funk', '22]'], ['Learning Colors – Colorful Eggs on a Farm', '23]'], ['Masha and the Bear – Recipe for Disaster', '24]'], ['Gangnam Style', '25]'], ['Wheels on the Bus', '30]'], ['Dame Tu Cosita', '31]'], ['Sugar', '32]'], ['Roar', '33]'], ['Counting Stars', '34]'], ['Sorry', '35]'], ['Thinking Out Loud', '36]'], ['Axel F', '37]'], ['Girls Like You', '38]'], ['Faded', '39]'], ['Dark Horse', '40]'], ['Baa Baa Black Sheep', '41]'], ['Let Her Go', '42]'], ['Bailando', '43]'], ['Lean On', '44]'], ['Shake It Off', '45]'], ['Perfect', '46]'], ['Waka Waka (This Time for Africa)', '47]'], ['Mi Gente', '48]']]

# for element in new_data:
#     newer_data.append(element[0])

# print(newer_data)
    




# for element in new_data :
#     print(element[1])
#     # for i in element:
#     #     print(i)


# -----------------------------------------------------------

# element = ['Baby Shark Dance', '3]']

# for i in element:
#     print(i[0])

# -----------------------------------------------------------

name = '"Bailando"[43]'
for x in name:
    x = name.replace('"','')
    print(x.split('[')[0])