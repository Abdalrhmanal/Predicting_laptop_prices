import sqlite3

# اتصال بقاعدة البيانات أو إنشاءها إذا لم تكن موجودة
db = sqlite3.connect('app.db')

# إنشاء مؤشر لقاعدة البيانات
cursor = db.cursor()

# إنشاء الجدول "المستخدم" إذا لم يكن موجودًا بالفعل
cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                  id INTEGER PRIMARY KEY,
                  username TEXT NOT NULL,
                  email TEXT NOT NULL,
                  password TEXT NOT NULL
                )''')

# إنشاء الجدول "ProductLap" إذا لم يكن موجودًا بالفعل
cursor.execute('''CREATE TABLE IF NOT EXISTS ProductLap (
                  id INTEGER PRIMARY KEY,
                  attribute1 TEXT,
                  attribute2 TEXT,
                  attribute3 TEXT,
                  attribute4 TEXT,
                  attribute5 TEXT,
                  attribute6 TEXT,
                  attribute7 TEXT,
                  img1 TEXT,
                  img2 TEXT,
                  img3 TEXT
                )''')



# إنشاء الجدول "Orders" إذا لم يكن موجودًا بالفعل
cursor.execute('''CREATE TABLE IF NOT EXISTS Orders (
                  id INTEGER PRIMARY KEY,
                  Users_username TEXT,
                  ProductLap_attribute1 TEXT,
                  totaly REAL,
                  FOREIGN KEY (Users_username) REFERENCES Users(username),
                  FOREIGN KEY (ProductLap_attribute1) REFERENCES ProductLap(attribute1)
                )''')

# حفظ التغييرات وإغلاق قاعدة البيانات
db.commit()
db.close()
