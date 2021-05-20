import datetime

#今日を取得


class Input:
#入力フェーズ
    def __init__(self):
        pass

    def ask_info(self):
        self.name = input("名前を入力してください: ")
        self.height = float(input("身長を入力してください[m]: "))
        self.weight = float(input("体重を入力してください[kg]: "))
        print("生年月日を下記に別々に入力してください")
        self.myYear = int(input("生まれた西暦を入力してください: "))
        self.myMonth = int(input("生まれた月を入力してください: "))
        self.myDay = int(input("生まれた日を入力してください: "))

    def get_name(self):
        return self.name
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_myYear(self):
        return self.myYear
    def get_myMonth(self):
        return self.myMonth
    def get_myDay(self):
        return self.myDay

class Person:

  #コンストラクタ
  def __init__(self, name, height, weight, myYear, myMonth, myDay):
    self.name = name
    self.height = height
    self.weight = weight
    self.myYear = myYear
    self.myMonth = myMonth
    self.myDay = myDay

  #ageメソッド
  def get_age(self):
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    age = year - int(self.myYear)
    if month < int(self.myMonth):
      age -= 1
    elif month == int(self.myMonth):
      if day < int (self.myDay):
        age -= 1
    return age
  
  #bmiメソッド
  def get_bmi(self):
    #print(self.height,self.weight)
    #print(self.height**2)
    #print(self.weight/(self.height**2))
    bmi = round(self.weight / (self.height ** 2), 2)
    return bmi
  
  #styleメソッド
  def get_style(self):
    if self.get_bmi() < 16.00:
      style = "重度の痩せ"
    elif 16.00 <= self.get_bmi() < 17.00:
      style = "中度の痩せ"
    elif 17.00 <= self.get_bmi() < 18.50:
      style = "軽度の痩せ"
    elif 18.50 <= self.get_bmi() < 25.00:
      style = "普通体型"
    elif 25.00 <= self.get_bmi() < 30.00:
      style = "前肥満"
    elif 30.00 <= self.get_bmi() < 35.00:
      style = "肥満（1度）"
    elif 35.00 <= self.get_bmi() < 40.00:
      style = "肥満（2度）"
    elif 40.00 <= self.get_bmi():
      style = "肥満（3度）"
    else:
      style = "入力ミスの可能性"
    return style

  def introduce(self):
    text = "私の名前は{}で、年齢は{}歳です。BMIは{}で、{}です。"
    return text.format(self.name, self.get_age(), self.get_bmi(), self.get_style())

"""class Daily_info:
    def __init__(self):
        today = datetime.date.today()
        year = today.year
        month = today.month
        day = today.day

    def get_info(self):
        return today, year, month, day
"""
#daily_info = Daily_info()
input_ = Input()

input_.ask_info()
person1 = Person(input_.get_name(), input_.get_height(), input_.get_weight(),input_.get_myYear(), input_.get_myMonth(), input_.get_myDay())
print(person1.introduce())
