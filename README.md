# 🚑 چت‌بات اورژانس پزشکی | Emergency Medical Chatbot

**نسخه فارسی یک دستیار پزشکی برای پاسخ به سوالات اضطراری بر اساس پروتکل‌های اورژانس**

[![Hugging Face Spaces](https://img.shields.io/badge/HuggingFace-Space-blue?logo=huggingface)](https://huggingface.co/spaces/Mtgama/emergency_chatbot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

---

## 📌 معرفی پروژه

این پروژه یک **چت‌بات تعاملی** است که با استفاده از رابط کاربری زیبا (HTML + TailwindCSS + JavaScript) و یک **بک‌اند مبتنی بر FastAPI** به کاربران کمک می‌کند تا در شرایط اضطراری، پاسخ‌هایی مطابق با **پروتکل‌های رسمی اورژانس پزشکی** دریافت کنند.

✅ پشتیبانی از زبان فارسی  
✅ تعامل مبتنی بر چت با افکت‌های دیداری زیبا  
✅ قابلیت توسعه برای تبدیل گفتار به متن (Voice Input)  
✅ امکان استقرار در Hugging Face Spaces

---

## 🎯 ویژگی‌ها

- 💬 گفت‌وگو با دستیار پزشکی اورژانس
- 🔎 پاسخ بر اساس اسناد و پروتکل‌های از پیش بارگذاری شده
- 🔥 طراحی واکنش‌گرا و زیبا با Tailwind CSS
- 🔊 پشتیبانی اولیه از دکمه "خواندن صوتی" (TTS)
- 🌐 قابل میزبانی به‌صورت کاملاً رایگان روی Hugging Face

---

## 🧰 تکنولوژی‌های استفاده‌شده

| بخش | تکنولوژی |
|------|-----------|
| رابط کاربری | `HTML`, `TailwindCSS`, `FontAwesome`, `JavaScript` |
| بک‌اند | `Python`, `FastAPI`, `OpenAI API`, `Vectorize API` |
| هاست | [Hugging Face Spaces](https://huggingface.co/spaces/Mtgama/emergency_chatbot) |

---

## ⚙️ نصب و اجرا محلی

```bash
git clone https://github.com/yourusername/emergency-chatbot.git
cd emergency-chatbot

# ایجاد محیط مجازی
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate

# نصب وابستگی‌ها
pip install -r requirements.txt

# اجرای سرور
uvicorn app:app --reload
