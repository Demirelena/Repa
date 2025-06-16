import pytest
from string_utils import StringUtils 


utils = StringUtils()

# --- Тесты для capitalize ---

# Позитивные кейсы
assert utils.capitalize("skypro") == "Skypro", "Should capitalize first letter"
assert utils.capitalize("s") == "S", "Should capitalize single character"
assert utils.capitalize(" skypro") == " skypro", "Should not change leading space"

# Негативные кейсы
assert utils.capitalize("") == "", "Empty string should stay empty"
assert utils.capitalize("123abc") == "123abc", "Should not change digits"

# --- Тесты для trim ---

# Позитивные кейсы
assert utils.trim("   skypro") == "skypro", "Should trim leading spaces"
assert utils.trim("skypro") == "skypro", "No leading spaces should return same string"
assert utils.trim(" ") == "", "Only space should become empty"

# Негативные кейсы
assert utils.trim("") == "", "Empty string should stay empty"
assert utils.trim("   ") == "", "String with only spaces should become empty"

# --- Тесты для contains ---

# Позитивные кейсы
assert utils.contains("SkyPro", "S") == True, "Should find S"
assert utils.contains("SkyPro", "P") == True, "Should find P"
assert utils.contains("SkyPro", "y") == True, "Should find y"

# Негативные кейсы
assert utils.contains("SkyPro", "U") == False, "Should not find U"
assert utils.contains("", "a") == False, "Empty string should not contain anything"
assert utils.contains("SkyPro", "") == True, "Empty string is technically in any string"

# --- Тесты для delete_symbol ---

# Позитивные кейсы
assert utils.delete_symbol("SkyPro", "k") == "SyPro", "Should remove k"
assert utils.delete_symbol("SkyPro", "Pro") == "Sky", "Should remove Pro"
assert utils.delete_symbol("SkyPro", "") == "SkyPro", "Deleting empty symbol changes nothing"

# Негативные кейсы
assert utils.delete_symbol("SkyPro", "U") == "SkyPro", "Deleting non-existent symbol changes nothing"
assert utils.delete_symbol("", "S") == "", "Deleting from empty string stays empty"
