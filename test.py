from datetime import datetime, timedelta

x = datetime.now()

a = x.strftime("%B") + " " + str(x.day)

b = datetime.now().strftime("%x")


print(x)
print(x.day)
print(x.time())
print(x.strftime("%A"))
print(x.strftime("%B"))

print(a)

print(datetime.utcnow)

print(str(datetime.now()))
print(str(datetime.now().strftime("%x")))
print(str(datetime.now().strftime("%X")))

now = datetime.now()
now = now - timedelta(hours=8, minutes=23, seconds=10)
print(x - now)
