driving = input('請問你有開過車嗎?: ')
if driving != '有' and driving != '沒有':
	print('只能輸入 有 or 沒有')
	raise SystemExit
age = input('請問你的年齡是: ')
age = int(age)
if driving == "有":
	if age >= 18:
		print('你通過測驗')
	else:
		print('奇怪!你怎麼可以開車')
if driving == "沒有":
	if age >= 18:
		print('你可以考駕照啦~怎不去考?')
	else:
		print('很好!再過幾年就可以考駕照啦~')