from turtle import Turtle, Screen

# timmy = Turtle() #יצירת אוביקט במחלקה שלTrtle
# timmy.shape("turtle")# בחירת צורה לצב
# timmy.forward(100)#בחירת תנועתיות קדימה
# timmy.left(120)# סיבוב במעלות
# #timmy.color("red")#בחירת צבע מיקום הפקודה ישפיע על נקודת הזמן בו יוחלף הצבע
# timmy.pencolor("red")#הגדרת צבע לעט של השובל
# timmy.penup()#הרמת העט כדי שלא יצבע
# #יש להגדיר את הצב ורק אח" להגדיר את המרחב ששו הוא יהיה
timmy = Turtle() #יצירת אוביקט במחלקה שלTrtle
#for i in range (400):

    #timmy.forward(100)#בחירת תנועתיות קדימה
    #timmy.right(90)# סיבוב במעלות
    #timmy.color("red")#בחירת צבע מיקום הפקודה ישפיע על נקודת הזמן בו יוחלף הצבע
    #יש להגדיר את הצב ורק אח" להגדיר את המרחב ששו הוא יהיה


# החלפת שם למודול (הענקת זהות בדויה)
#import turtle as mwe_name
#timmy = nwe_name.Tartle
# timmy.left(180)
# timmy.penup()
# timmy.forward(300)
# timmy.right(180)
# timmy.pendown()
# for i in range(2):
#     for i in range (15):   #יצירת קו מקווקו
#         timmy.forward(5)
#         timmy.penup()
#         timmy.forward(5)
#         timmy.pendown()
#     timmy.penup()
#     timmy.forward(75)
# timmy.circle -- # מתודה ליצירת עיגולים בזויות שונות

# r = 3
# m= 3
#
# for i in range (7):
#     n = 360 / m
#     for i in range (r):
#         timmy.pencolor("red")
#         timmy.right(n)
#         timmy.forward(100)
#     r +=1
#     m +=1








# screen = Screen()# חייבים סוגריים במתודה כמו בפונקציה
# screen.exitonclick()#יבוא פקודה מהמחלקה כדי שהמסך לא יעלם אלא על ידי לחיצה


#tuples   סןג נתונים בפייתון
# מופיע בצורה הזו --- (1,3,8)  דומה  בצורתו לרשימה אבל בסוגריים עגולים ההבדל ביניהם הוא
# my_tuple = (1, 3, 4)   --  מסודר לפי המיקום
#
# ההבדל בין רשימה לטאפל הוא - לא ניתן לשנות את הערכים שלו
# כמו כן לא ניתן להסיר או להוסיף פריטים כי לא ניתן לחולל שום שינוי באובייקט  tuple are immutapele -- חקוק באבן ולא ניתן לשינוי
#
#כדי לבצע שינויים בטאפל ניתן להמיר אותו לליסט
#לדוג' a = list(my_tuple)
# יתרון נוסף של הטאפל הוא שהוא מהיר יותר, מאחר ואינו ניתן לשינוי יש לו מקום קבוע בזיכרון
#




# my_screen = Screen()

# my_screen.listen()
# my_screen.exitonclick()
# my_screen.onkey("space", fun = )(      פןנקציה שקבלת פרמטר לא יכולה לשמש ב keyכי אתה מעביר אותה לארגומנט הפונקציה מגיעה ללא סוגריים) # כדי לקשר בין לחיצה על מקש לפעולה מסוימת שמתרחשת על המסך או בקוד שלנו )event(



#strings
#slycing


# parrot = "nagetiveere"
#
# print(parrot[0:6:3])   #  הערך השלישי אחרי הנקודותיים מייצג את הדילוגים
# print(parrot[6:0:-2])# כשהערך השלישי הוא במינוס הדילוגים וההדפסה יהיו מימין לשמאל
# print(parrot[::-1])# ידפיס מימין לשמשאל את כל הסטרינג
# print(parrot)
#
# number = "9,322,564,675,879:"
# print(number[1::4])# ידפיס רק את במפרידים(מהראשון עד האחרון בדילוג שייבחר בערך השלישי


# print("pi is {0:15}".format(22/7))# ה0 מייצג את האינקס אותו אני רוצה לעצב. הנקודתיים זה אופרטור של הפרדה. ה15 זה מינימום התוים שאני מקצה לשדה.
# print("pi is {0:15.5f}".format(22/7))#ה .5 F מגדירה את מגבת התוים שיוצגו אחרי הנ קודה.
# print("pi is {0:15f}".format(22/7))# יציג קק 5 ספרות אחרי הנקודה
# # floit באופן בסיסי מציג מקסימום 6 ספרת אחרי הנקודה

# list = [12, 10, 34]
# a, b, c = list # השמת ערכים הליסט לתוך משתנים (כמות המשתנים חייבת להיות זהה לכמות הערכים הליסט
# print(list)
# print(a, b, c)

# tuples are immutable == טאפל הינו מסד נתונים כמו ליסט אך בשונה מליסט לא ניתתן לבצע בו שינויים
# my_tuple = 1, 2, 3# באופן בסיסי כל השמה של מספר ערכים למשתנה אחד מגדירה אותם כטאפל
# print(type(my_tuple))
# print(my_tuple)
# t = ('one', 2)# tuple יכול להכיל ערכים מסוגים שונים

# print(type(t))
# print(t[-1])# באופן דומה לליסט גם בטאפל ניתן לגשת למופע שנמצא באינדקס ספציפי
# t = ('a', 'b', 'a', 'd')# למעשה בהשמה של מספר ערכים למשתנה אחד אין צורך בסוגריים כדי שיוגדרו כטאפל אך חשוב להקפיד על סוגריים בשביל הנראות
# print(t.count('a'))# הפקודה countמציגה את מספר הפעמים בו מופע מסןים כסטרינג או מספר נמצא בתוך מחרוזת ליסט או טאפל וכו
# print(t.index('a'))# כשערך קיים יותר מפעם אחת ונבקש את האינדקס של אותו הערך ע"י פקודת האינקס יופיע רק האינדקס של המופע הראשון

# Unpacking a Tuple # פריקת טאפל
# a = b = c= d = e = f = 12 # shorthand assignment השמה מקוצרת של מספר משתנים שונים בערך אחד
# c = 22
# print(c)
#
# a = "srer"
# b = a
# a = "sss"
# print(b)

# x, y, z = 1, 2, 76#השמה מקוצרת של מספר משתנים במספר ערכים שונים
# print(x)
# print(y)
# print(z)
# print(type(x))
# student_1, student_2, student_3 = "avi", "beni", "david"
# print(student_3)
# students = student_1, student_2, student_3
# print(students)
# print(type(students))# it is a "tuple"

# print("Unpacking a tuple")
# data = 1, 2, 76  # data   a tuple
# print(type(data))
# x, y, z = data #פריקה של טאפל למשתנים נפרדים
# print(x)
# print(y)
# print(z)

# tuples are immutable

# print("Unpacking a list")
#
# p, q, r = data_list
# print(q)
# print(p)
# print(r)


# for i in "abfffd":
#     print(i)

# enumeration
# for index, character in enumerate("abcdefgh"):  # also unpacks the tuple# אינומרייט מכליל ספירה של האינדקס ביחד עם הערך ומייצג אותם כטאפל(ממזג גל ערך והאינדקס שלו לטאפל נפרד)
#     print(index, character)

# names = ["Alice", "Bob", "Charlie"]
# for index, name in enumerate(names):
#     print(f"{index + 1}. {name}")  # the tuples were unpacked

# for tutian in enumerate("abcdefgh"):
#     print(tutian)  # will show us tuples# כשיוכנס רק משתנה אחד הפלט יכלול קבוצות של טאפלים שמכילים כל אחד ערך ואינדקס מתאים

for t in enumerate("abcdefgh"):
    index, character = t  # unpacking the tuple...
    print(index, character)


