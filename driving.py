name = input('請輸入您的名子:')
gender = input('請輸入性別(男或女或其他):')
country = input('請輸入您的國家:')
age = input('請輸入您的年齡:')
age = int(age)

if gender == '男':
	gender = '帥哥'
elif gender == '女':
	gender = '小姊姊'	
else:
	gender = '' 	

if country == '台灣':
	if age >= 18 and age <= 70:
		print(name+gender,  '可以去考取汽車，摩托車等駕照囉!')
	else:
		print(name+gender,  '還不能考駕照喔!')
