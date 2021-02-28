import re
text = open("input.txt", 'r', encoding="utf-8")
data = text.read()

CompanyNamePattern = r'ТОО \w+'
BinPattern = r'БИН (\d{12})'
ItemNamePattern = r'\d+\.\s(.+)'
ItemAmountPattern = r'(\d),000'
ItemPrice1Pattern = r'x (\d+\s?\d+,00)'
ItemPrice2Pattern = r'Стоимость\n(\d+\s?\d+,00)'
TimePattern = r'Время: (\d\d\.\d\d.\d{4}\s\d\d:\d\d:\d\d)'
AddressPattern = r'г\..+'
CompanyName = re.findall(CompanyNamePattern, data)
Bin = re.findall(BinPattern, data)
ItemName = re.findall(ItemNamePattern, data)
ItemAmount = re.findall(ItemAmountPattern, data)
ItemPrice1 = re.findall(ItemPrice1Pattern, data)
ItemPrice2 = re.findall(ItemPrice2Pattern, data)
Time = re.findall(TimePattern, data)
Address = re.findall(AddressPattern, data)

print(*CompanyName)
print(*Bin, '\n')
for i in range(0, len(ItemName)):
	print(ItemName[i])
	print(ItemAmount[i])
	print(ItemPrice1[i])
	print(ItemPrice2[i])
	print('\n')
print(*Time)
print(*Address)
text.close()