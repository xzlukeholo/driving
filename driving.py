name = input('請輸入您的名子:')
gender = input('請輸入性別(男或女或其他):')
country = input('請輸入您的國家:')
age = input('請輸入您的年齡:')

if gender == '男':
	gender = '帥哥'
elif gender == '女':
	gender = '小姐'	
else:
	gender = ''

age = int(age)

if country == '台灣':
	if age >= 18 and age <= 70:
		print(name+gender, '可以去考汽車駕照囉!')
	else:
		print(name+gender, '還不能考駕照喔!')
elif country == '美國':
	if age >= 16:
		print(name+gender, '可以去考汽車駕照囉!')
	else:
		print(name+gender, '還不能考駕照喔!')
elif country == '日本':
	if age >= 18:
		print(name+gender, '可以去考汽車駕照囉!')
	else:
		print(name+gender, '還不能考駕照喔!')
elif country == '中國':
	if age >= 18:
		print(name+gender, 'owo')
	else:
		print(name+gender, '0w0')
else:
	print(name+gender, '抱歉喔!我們目前只能輸入台灣、美國、日本喔')