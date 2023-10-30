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



 <!-- ![branch main secured 1](./Screenshots/main-branch-secured.PNG)
 ![branch main secured 2](./Screenshots/main-branch-secured1.PNG) -->
