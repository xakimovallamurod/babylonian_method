import math


# 01
def bir_qadam(S, x):
    """
    Bobil usulining bitta qadamini bajaring: S soni va x taxmin berilgan, yangi taxminni qaytaring: (x + S / x) / 2.

    Argumentlar:
        S (float): son
        x (float): taxmin

    Qaytaradi:
        float: yangi taxmin
    """
    pass


# 02
def ikki_qadam(S, x):
    """
    Bobil usulining ikki qadamini bajarib, natijani qaytaring.

    Argumentlar:
        S (float): son
        x (float): taxmin

    Qaytaradi:
        float: taxmin
    """
    pass


# 03
def n_qadam(S, x, n):
    """
    Bobil usulining n ta qadamini bajarib, natijani qaytaring.

    Argumentlar:
        S (float): son
        x (float): taxmin
        n (int): qadamlar soni

    Qaytaradi:
        float: taxmin
    """
    pass


# 04
def xatolik(S, x):
    """
    x taxminning xatoligini qaytaring: |x² − S|.

    Argumentlar:
        S (float): son
        x (float): taxmin

    Qaytaradi:
        float: xatolik
    """
    pass


# 05
def boshlangich_taxmin(S):
    """
    Boshlang'ich taxminni qaytaring: S > 1 bo'lsa S / 2, aks holda 1.

    Argumentlar:
        S (float): son

    Qaytaradi:
        float: taxmin
    """
    pass


# 06
def main(S, d):
    """
    Bobil usuli: x taxmindan boshlab, |x² − S| < 1e-10 bo'lguncha qadamlarni takrorlang va natijani qaytaring.

    Argumentlar:
        S (float): son
        d (float): boshlang'ich taxmin

    Qaytaradi:
        float: kvadrat ildiz
    """
    pass


# 07
def qadamlar_soni(S, x, eps):
    """
    Aniqlik eps berilgan. |x² − S| < eps bo'lguncha nechta qadam kerak bo'lishini qaytaring.

    Argumentlar:
        S (float): son
        x (float): taxmin
        eps (float): aniqlik

    Qaytaradi:
        int: qadamlar soni
    """
    pass


# 08
def yaxlitlangan_ildiz(S, k):
    """
    S sonining kvadrat ildizini Bobil usulida hisoblang (boshlang'ich taxmin 5-topshiriqdagidek) va k xona aniqlikda yaxlitlab qaytaring.

    Argumentlar:
        S (float): son
        k (int): aniqlik

    Qaytaradi:
        float: ildiz
    """
    pass


# 09
def butun_ildiz(S):
    """
    S butun sonining kvadrat ildizining butun qismini Bobil usuli yordamida qaytaring.

    Argumentlar:
        S (int): son

    Qaytaradi:
        int: butun qism
    """
    pass


# 10
def mukammal_kvadratmi(S):
    """
    S butun soni mukammal kvadrat ekanini Bobil usuli yordamida tekshiring.

    Argumentlar:
        S (int): son

    Qaytaradi:
        bool: javob
    """
    pass


# 11
def qadamlar_royxati(S, x, n):
    """
    Bobil usulining n ta qadamidagi barcha taxminlarni 6 xona aniqlikda ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        S (float): son
        x (float): taxmin
        n (int): qadamlar soni

    Qaytaradi:
        list: taxminlar
    """
    pass


# 12
def math_bilan_farq(S):
    """
    Bobil usuli natijasi va math.sqrt() natijasi orasidagi farqning mutlaq qiymatini 12 xona aniqlikda qaytaring.

    Argumentlar:
        S (float): son

    Qaytaradi:
        float: farq
    """
    pass


# 13
def kub_ildiz(S, x, n):
    """
    Kub ildiz uchun Nyuton usuli: x = (2x + S / x²) / 3. n ta qadamdan keyingi natijani 6 xona aniqlikda qaytaring.

    Argumentlar:
        S (float): son
        x (float): taxmin
        n (int): qadamlar soni

    Qaytaradi:
        float: kub ildiz
    """
    pass


# 14
def yer_tomoni(maydon):
    """
    Allamurodning kvadrat shaklidagi yer maydoni berilgan. Yer tomonini Bobil usulida hisoblang va 2 xona aniqlikda qaytaring.

    Argumentlar:
        maydon (float): maydon (m²)

    Qaytaradi:
        float: tomon
    """
    pass


# 15
def diagonal(eni, boyi):
    """
    Allamurodning xonasi eni va bo'yi berilgan. Diagonalni Bobil usulida hisoblang va 2 xona aniqlikda qaytaring.

    Argumentlar:
        eni (float): eni
        boyi (float): bo'yi

    Qaytaradi:
        float: diagonal
    """
    pass


# 16
def masofa(x1, y1, x2, y2):
    """
    Allamurodning uyi (x1, y1) va ofisi (x2, y2) koordinatalari berilgan. Masofani Bobil usulida hisoblang va 2 xona aniqlikda qaytaring.

    Argumentlar:
        x1 (float): uy x
        y1 (float): uy y
        x2 (float): ofis x
        y2 (float): ofis y

    Qaytaradi:
        float: masofa
    """
    pass


# 17
def ildizlar_royxati(sonlar):
    """
    Sonlar ro'yxati berilgan. Har birining kvadrat ildizini Bobil usulida hisoblab, 3 xona aniqlikda ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        sonlar (list): musbat sonlar

    Qaytaradi:
        list: ildizlar
    """
    pass


# 18
def kvadrat_tenglama(a, b, c):
    """
    ax² + bx + c = 0 tenglamaning haqiqiy ildizlarini (diskriminant ildizini Bobil usulida hisoblab) 2 xona aniqlikda o'sish tartibida ro'yxat ko'rinishida qaytaring. Ildiz bo'lmasa, bo'sh ro'yxat qaytaring.

    Argumentlar:
        a (float): a
        b (float): b
        c (float): c

    Qaytaradi:
        list: ildizlar
    """
    pass


# 19
def geometrik_orta(a, b):
    """
    Ikki musbat son berilgan. Ularning o'rta geometrigini (√(a·b)) Bobil usulida hisoblang va 2 xona aniqlikda qaytaring.

    Argumentlar:
        a (float): 1-son
        b (float): 2-son

    Qaytaradi:
        float: o'rta geometrik
    """
    pass


# 20
def jadval(S, x, n):
    """
    Bobil usulining n ta qadamini "<i>-qadam: <taxmin>" ko'rinishidagi satrlar ro'yxati sifatida qaytaring (taxmin 4 xona aniqlikda).

    Argumentlar:
        S (float): son
        x (float): taxmin
        n (int): qadamlar soni

    Qaytaradi:
        list: satrlar
    """
    pass


# Tekshirish
print(main(16, 4))
print(main(26, 5))
