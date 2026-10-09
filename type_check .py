#type_check.py
#this program check and converts data type

#predictions: 8080 int ,"8080"str,99.5 float,"198.51.100.7"str,1_000 int.

print(type(8080))
print(type("8080"))
print(type(99.5))
print(type("198.51.100.7"))
print(type(1_000))

number =int("443")
text =str(8080)
decimal =float("2.5")

print(number,type(number))
print(text,type(text))
print(decimal,type(decimal))