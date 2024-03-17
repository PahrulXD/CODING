import os
from fbthon import Facebook
from fbthon import Web_Login

def masuk():
	os.system ("clear")
	email = input ("- email atau nomer ponsel : ")
	password = input ("- kata sandi : ")
	print ("")
	login = Web_Login(email,password)
	cookie = login.get_cookie_str() 
	fb = Facebook(cookie)
	print (cookie)
	
	
masuk()