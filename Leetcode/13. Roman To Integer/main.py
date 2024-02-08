def romanToInt(s: str) -> int:
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    roman_subtractions = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    count = 0
    result = 0

    while True:
        if count >= len(s):
            break

        if count <= len(s) - 2:
            if s[count] == "I" and s[count + 1] in ["V", "X"]:
                result += roman_subtractions[f"{s[count]}{s[count+1]}"]
                count += 2
                continue
            elif s[count] == "X" and s[count + 1] in ["L", "C"]:
                result += roman_subtractions[f"{s[count]}{s[count+1]}"]
                count += 2
                continue
            elif s[count] == "C" and s[count + 1] in ["D", "M"]:
                result += roman_subtractions[f"{s[count]}{s[count+1]}"]
                count += 2
                continue
        result += roman_map[s[count]]
        count += 1

    print(result)


romanToInt("III")
romanToInt("LVIII")
romanToInt("MCMXCIV")
romanToInt("DCXXI")
