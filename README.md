# Interview Task — Test API bilan ishlash

Ushbu proyekt test API bilan ishlashni ko'rsatadi: POST so'rov yuborish, ikki bo'lakli kodni olish, kodlarni birlashtirish va GET orqali asli xabarni olish.

<b>Loyihada server qismi uchun FastAPI dan foydalandim Global (Public) Url manzil uchun Ngrokdan foydalandim.</b>

## 1. Loyiha uchun virtual environment yaratib kerakli paketlarni install qilib olamiz

    python3 -m venv venv
 
    source venv/bin/activate
 
    pip install -r requirements.txt

## 2. Uvicorn orqali FastAPI serverimizni ishga tushirib olamiz

    uvicorn server:app --reload

Uvicorn default tarzda loyihani <b>8000</b> portda ishga tushiradi

## 3. Ngrokni sozlab olamiz

    ngrok http 8000

Ngrok bizga vaqtinchalik Public URL manzil beradi shu manzilni <i>test.py</i> ichidagi <code>callback_url</code> ga qo'yamiz. Bizga bu apidan codening ikkinchi qismini olish uchun foydanamiz.

## 4. <i>test.py</i> fileni ishga tushiramiz

    python3 test.py


## Qanday ishlaydi

<b>
1. test.py ishga tushishi bilan https://test.icorp.uz/interview.php manziliga POST so'rov yuboriladi.
So'rovda quyidagi ma'lumotlar bor:
<i>msg</i> — ixtiyoriy xabar
<i>url</i> — Ngrok orqali olingan callback manzil

2. API javoban part1 kodni qaytaradi.

3. Kodning ikkinchi qismi — part2 — FastAPI serverimizga callback orqali yuboriladi.
Bu qiymat received_data.json fayliga yozib qo'yiladi.
(Agar loyiha kattaroq bo'lganida, buni saqlash uchun Redis ishlatishni maqul ko'rar edim)

4. Skript received_data.json ichidan part2ni o'qib oladi.

5. part1 va part2 birlashtirilib yakuniy kod hosil qilinadi.

6. Shu yakuniy kod GET so'rov orqali API'ga yuboriladi:

    https://test.icorp.uz/interview.php?code={full_code}

7. API javoban asl xabarni qaytaradi.
</b>
