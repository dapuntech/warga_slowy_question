from typing import Union
import unittest


def pertambahan(
    angka1: Union[float, int], angka2: Union[float, int]
) -> Union[float, int]:
    return angka1 + angka2


def perkalian(
    angka1: Union[float, int], angka2: Union[float, int], angka3: Union[float, int] = 0
) -> Union[float, int]:
    if angka3 == 0:
        return angka1 * angka2
    if angka1 == 0:
        return angka2 * angka3
    else:
        pass


def pengurangan(
    angka1: Union[float, int], angka2: Union[float, int]
) -> Union[float, int]:
    return angka1 - angka2


class SolveItSoalPertama(unittest.TestCase):
    # A -> B = A + B
    hasil_A_ke_B_tambah = pertambahan(2.1, 5.9)
    # A -> C = A x C
    hasil_A_ke_C_kali = perkalian(2.1, 10)
    # C -> D = C x D
    hasil_C_ke_D_kali = perkalian(10, 0.9)
    # B -> D = B - D
    hasil_B_ke_D_kurang = pengurangan(5.9, 0.9)

    def test_hasil_A_ke_B_tambah(self):
        self.assertEqual(self.hasil_A_ke_B_tambah, 8)

    def test_hasil_A_ke_C_kali(self):
        self.assertEqual(self.hasil_A_ke_C_kali, 21)

    def test_hasil_C_ke_D_kali(self):
        self.assertEqual(self.hasil_C_ke_D_kali, 9)

    def test_hasil_B_ke_D_kurang(self):
        self.assertEqual(self.hasil_B_ke_D_kurang, 5)
