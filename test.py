from app import User,db

user = User("Loki",1234)
db.session.add(user)
db.session.commit()
test = User.query.all()
print(test)