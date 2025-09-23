from datetime import datetime, timedelta
from faker import Faker
from app import db
from models import User, Book, Genre, Rating, BorrowRecord


fake = Faker()

db.session.query(User).delete()
db.session.query(Book).delete()
db.session.query(Genre).delete()
db.session.query(Rating).delete()
db.session.query(BorrowRecord).delete()
db.session.commit()

