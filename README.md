# گزارش پروژه اول (Simple Wolfram)
## مقدمه  
در این آزمایش ما قصد آشنایی با ابزار git 
و دستورات پرکابرد آن را داریم. به این منظور یک پروژه ساده با نام Simple Wolfram طرح کرردیم که با زبان پایتون پیاده سازی شده است. 
این پروژه یک ماشین حساب است که از سه بخش اصلی تشکیل می شود:

 بخش اول (Calculator)
 اعمال ساده جمع، تفریق،ضرب و تقسیم به همراه توان و ریشه یابی است. 

بخش دوم (Matrix Operations)
عملیات های ماتریسی جمع، ضرب ماتریسی، محاسبه دترمینان و معکوس ماتریس است.

بخش سوم (دبو)

## رفع نیازمندی های آزمایش

### 1.مخزن گیت هاب پروژه (GitHub Repository)
مخزن این پروژه در 
[این آدرس](https://github.com/MoNam97/Simple-Wolfram)
در گیت هاب وجود دارد و قابل دسترسی عمومی است.

![github repo after creation](./Screenshots/project-init.PNG)

### 2. فایل gitignore.

با توجه به اینکه پروژه به زبان پایتون است فایل gitignore را برای زبان پایتون ایجاد کردیم. دراین فایل اسم و آدرس فایل هایی که که می خواهیم توسط گیت دیده نشوند و
 نمی خواهیم در مخزن گیت هاب قرار بگیرند، مثل فایل های میانی ناشی از اجرا مفسر پایتون از جمله pycache را مشخص می کنیم.
همچنین به این فایل آدرس فایل های تولید شده توسط IDE مورد استفاده را نیز اضافه می کنیم.

![part of gitignore file](./Screenshots/gitignore.PNG)

### 3. commit ها

در فرآیند توسعه پروژه بیش از 30 کامیت معنادار انجام شد که روند کلی آن ها در ادامه آمده است. <br>
با پیاده سازی ساختار اولیه پروژه و یک رابط کاربری ساده شروع به کار کردیم. سپس با اضافه کردن هر یک از ماژول ها، به طور مثال توان در بخش calculator، یک کامیت انجام دادیم.
همچنین برای رفع اشکال های کد ، تمیز کردن کد و برطرف کردن خطا ناشی از merge conflict نیز کامیت های مربوطه را انجام داده ایم.

تصاویر گزیده ای از کامیت های بنده در ادامه آمده است:

![commit2](./Screenshots/commit2.PNG)
![commit3](./Screenshots/commit3.PNG)
![commit4](./Screenshots/commit4.PNG)
![commit7](./Screenshots/commit7.PNG)
![commit8](./Screenshots/commit8.PNG)
![commit9](./Screenshots/commit9.PNG)
![commit11](./Screenshots/commit11.PNG)
![commit12](./Screenshots/commit12.PNG)
![commit13](./Screenshots/commit13.PNG)

### 4. سه شاخه معنادار پروژه

با توجه به تعریف پروژه ما سه شاخه polynomials ، main
 و matrix_operations ایجاد کردیم، بخش اول (Calculator) که
 در واقع یک ماشین حساب ساده است در شاخه main پیاده شده است.
    بخش دوم که عملیات های ماتریسی است در شاخه matrix_operations توسعه یافته و بخش سوم 
    (دبو)
.

 با پایان یافتن هر کدام از بخش ها، آن ها را با شاخه main ادغام کردیم.

 ![branch matrix](./Screenshots/git-branch-matrix.PNG)

(دبو)


### 5. رفع merge conflic ها

در فرآیند توسعه پروژه در دو قسمت دچار conflict شدیم؛
هم در یک شاخه و هم هنگام ادغام دو شاخه.

در توسعه بخش اول در شاخه main، از آنجایی که هر دو عضو تیم در یک فایل کار می کردیم و غالبا مجبور به تغییر یک تابع بودیم، مثلا برای به روز کردن رابط کاربری، در مواردی به conflict برخوردیم. در این مواقع  با بررسی کد تصمیم متناسب را برای کد ادغام شده گرفتیم.

در ادامه تصایری از یکی از این موارد آمده است:
![merge conflict 1](./Screenshots/merge-conflict1.PNG)
![merge conflict 2](./Screenshots/merge-conflict2.PNG)
![merge conflict 3](./Screenshots/merge-conflict3.PNG)

(دبو)


در ادغام دو شاخه main و matrix_operations نیز با conflict مواجه شدیم. در این مورد ابتدا با بررسی کد تصمیم متناسب را برای کد ادغام در شاخه  matrix_operations گرفتیم؛ سپس با توجه به protected بودن شاخه main
با ایجاد یک pull request آن را با شاخه اصلی ادغام کردیم.

![branch merge conflict 1](./Screenshots/merge-conflict-f1.PNG)
یکی از مصادیق conflict در ادغام کد:
![branch merge conflict 2](./Screenshots/merge-conflict-f2.PNG)
![branch merge conflict 3](./Screenshots/merge-conflict-f3.PNG)

(دبو)

### 6. اعمال محدودیت برای شاخه اصلی(main) و محافظت از آن

همانطور که در کلاس هم گفته با رفتن در تنظیمات مخزن گیت هاب وارد قسمت Branches شده و برای شاخه اصلی(main) محدودیت ایجاد کردیم. این محدودیت به این صورت است که هر کامیتی که قرار است در شاخه اصلی انجام شود، باید حتما از یکی از شاخه های دیگر به صورت pull request ادغام شود.

 ![branch main secured 1](./Screenshots/main-branch-secured.PNG)
 ![branch main secured 2](./Screenshots/main-branch-secured1.PNG)

ادغام کردن شاخه main با شاخه matrix_operations در گیت هاب:
![branch merge 1](./Screenshots/merge-req.PNG)
![branch merge 2](./Screenshots/merge-req2.PNG)
![branch merge 3](./Screenshots/merge-req3.PNG)

## پاسخ به سوالات
