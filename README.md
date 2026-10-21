# Bobil usuli (kvadrat ildizni hisoblash)

![Bobil usuli](babylonian_.png)

Bobil usulida S sonining kvadrat ildizi ketma-ket yaqinlashish orqali topiladi: x taxmindan boshlab, har qadamda x = (x + S / x) / 2 hisoblanadi. Barcha funksiyalar `main.py` faylida. `math.sqrt()` dan foydalanmang (12-topshiriqdan tashqari).

## 01. bir_qadam

Bobil usulining bitta qadamini bajaring: S soni va x taxmin berilgan, yangi taxminni qaytaring: (x + S / x) / 2.

**Misol 1:**

```Python
Kirish: S=26, x=5
Chiqarish: 5.1
```

**Misol 2:**

```Python
Kirish: S=16, x=4
Chiqarish: 4.0
```

---

## 02. ikki_qadam

Bobil usulining ikki qadamini bajarib, natijani qaytaring.

**Misol 1:**

```Python
Kirish: S=26, x=5
Chiqarish: 5.099019607843138
```

---

## 03. n_qadam

Bobil usulining n ta qadamini bajarib, natijani qaytaring.

**Misol 1:**

```Python
Kirish: S=2, x=1, n=3
Chiqarish: 1.4142156862745097
```

**Misol 2:**

```Python
Kirish: S=2, x=1, n=0
Chiqarish: 1.0
```

---

## 04. xatolik

x taxminning xatoligini qaytaring: |x² − S|.

**Misol 1:**

```Python
Kirish: S=26, x=5.1
Chiqarish: 0.01
```

---

## 05. boshlangich_taxmin

Boshlang'ich taxminni qaytaring: S > 1 bo'lsa S / 2, aks holda 1.

**Misol 1:**

```Python
Kirish: S=26
Chiqarish: 13.0
```

**Misol 2:**

```Python
Kirish: S=0.5
Chiqarish: 1
```

---

## 06. main

Bobil usuli: x taxmindan boshlab, |x² − S| < 1e-10 bo'lguncha qadamlarni takrorlang va natijani qaytaring.

**Misol 1:**

```Python
Kirish: S=16, d=4
Chiqarish: 4.0
```

**Misol 2:**

```Python
Kirish: S=26, d=5
Chiqarish: 5.099019513592786
```

---

## 07. qadamlar_soni

Aniqlik eps berilgan. |x² − S| < eps bo'lguncha nechta qadam kerak bo'lishini qaytaring.

**Misol 1:**

```Python
Kirish: S=26, x=5, eps=0.0001
Chiqarish: 2
```

**Misol 2:**

```Python
Kirish: S=16, x=4, eps=0.0001
Chiqarish: 0
```

---

## 08. yaxlitlangan_ildiz

S sonining kvadrat ildizini Bobil usulida hisoblang (boshlang'ich taxmin 5-topshiriqdagidek) va k xona aniqlikda yaxlitlab qaytaring.

**Misol 1:**

```Python
Kirish: S=26, k=3
Chiqarish: 5.099
```

**Misol 2:**

```Python
Kirish: S=2, k=5
Chiqarish: 1.41421
```

---

## 09. butun_ildiz

S butun sonining kvadrat ildizining butun qismini Bobil usuli yordamida qaytaring.

**Misol 1:**

```Python
Kirish: S=26
Chiqarish: 5
```

**Misol 2:**

```Python
Kirish: S=144
Chiqarish: 12
```

---

## 10. mukammal_kvadratmi

S butun soni mukammal kvadrat ekanini Bobil usuli yordamida tekshiring.

**Misol 1:**

```Python
Kirish: S=144
Chiqarish: true
```

**Misol 2:**

```Python
Kirish: S=150
Chiqarish: false
```

---

## 11. qadamlar_royxati

Bobil usulining n ta qadamidagi barcha taxminlarni 6 xona aniqlikda ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: S=26, x=5, n=3
Chiqarish: [5.1, 5.09902, 5.09902]
```

---

## 12. math_bilan_farq

Bobil usuli natijasi va `math.sqrt()` natijasi orasidagi farqning mutlaq qiymatini 12 xona aniqlikda qaytaring.

**Misol 1:**

```Python
Kirish: S=26
Chiqarish: 0.0
```

---

## 13. kub_ildiz

Kub ildiz uchun Nyuton usuli: x = (2x + S / x²) / 3. n ta qadamdan keyingi natijani 6 xona aniqlikda qaytaring.

**Misol 1:**

```Python
Kirish: S=27, x=3, n=5
Chiqarish: 3.0
```

**Misol 2:**

```Python
Kirish: S=100, x=4, n=5
Chiqarish: 4.641589
```

---

## 14. yer_tomoni

Allamurodning kvadrat shaklidagi yer maydoni berilgan. Yer tomonini Bobil usulida hisoblang va 2 xona aniqlikda qaytaring.

**Misol 1:**

```Python
Kirish: maydon=600
Chiqarish: 24.49
```

---

## 15. diagonal

Allamurodning xonasi eni va bo'yi berilgan. Diagonalni Bobil usulida hisoblang va 2 xona aniqlikda qaytaring.

**Misol 1:**

```Python
Kirish: eni=3, boyi=4
Chiqarish: 5.0
```

**Misol 2:**

```Python
Kirish: eni=4, boyi=5
Chiqarish: 6.4
```

---

## 16. masofa

Allamurodning uyi (x1, y1) va ofisi (x2, y2) koordinatalari berilgan. Masofani Bobil usulida hisoblang va 2 xona aniqlikda qaytaring.

**Misol 1:**

```Python
Kirish: x1=0, y1=0, x2=2, y2=3
Chiqarish: 3.61
```

---

## 17. ildizlar_royxati

Sonlar ro'yxati berilgan. Har birining kvadrat ildizini Bobil usulida hisoblab, 3 xona aniqlikda ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: sonlar=[2, 9, 26]
Chiqarish: [1.414, 3.0, 5.099]
```

---

## 18. kvadrat_tenglama

ax² + bx + c = 0 tenglamaning haqiqiy ildizlarini (diskriminant ildizini Bobil usulida hisoblab) 2 xona aniqlikda o'sish tartibida ro'yxat ko'rinishida qaytaring. Ildiz bo'lmasa, bo'sh ro'yxat qaytaring.

**Misol 1:**

```Python
Kirish: a=1, b=-5, c=6
Chiqarish: [2.0, 3.0]
```

**Misol 2:**

```Python
Kirish: a=1, b=2, c=5
Chiqarish: []
```

**Misol 3:**

```Python
Kirish: a=1, b=-3, c=1
Chiqarish: [0.38, 2.62]
```

---

## 19. geometrik_orta

Ikki musbat son berilgan. Ularning o'rta geometrigini (√(a·b)) Bobil usulida hisoblang va 2 xona aniqlikda qaytaring.

**Misol 1:**

```Python
Kirish: a=4, b=9
Chiqarish: 6.0
```

**Misol 2:**

```Python
Kirish: a=2, b=26
Chiqarish: 7.21
```

---

## 20. jadval

Bobil usulining n ta qadamini "<i>-qadam: <taxmin>" ko'rinishidagi satrlar ro'yxati sifatida qaytaring (taxmin 4 xona aniqlikda).

**Misol 1:**

```Python
Kirish: S=26, x=5, n=3
Chiqarish: ["1-qadam: 5.1", "2-qadam: 5.099", "3-qadam: 5.099"]
```

