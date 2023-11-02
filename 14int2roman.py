class Solution:
    def intToRoman(self, num: int) -> str:
        # 暴力解，乐
        mappers = [
            {
                "0": "",
                "1": "I",
                "2": "II",
                "3": "III",
                "4": "IV",
                "5": "V",
                "6": "VI",
                "7": "VII",
                "8": "VIII",
                "9": "IX",
            },
            {
                "0": "",
                "1": "X",
                "2": "XX",
                "3": "XXX",
                "4": "XL",
                "5": "L",
                "6": "LX",
                "7": "LXX",
                "8": "LXXX",
                "9": "XC",
            },
            {
                "0": "",
                "1": "C",
                "2": "CC",
                "3": "CCC",
                "4": "CD",
                "5": "D",
                "6": "DC",
                "7": "DCC",
                "8": "DCCC",
                "9": "CM",
            },
            {"0": "", "1": "M", "2": "MM", "3": "MMM", "4": "MMMM"},
        ]

        ret = ""
        for i, ch in enumerate(reversed(str(num))):
            ret = mappers[i][ch] + ret

        return ret

    def best_mem_solution(self, num: int) -> str:
        count = 0
        roman = ""
        map1 = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        for key in map1:
            if num // key != 0:
                roman += map1[key] * (num // key)
                num %= key
        return roman

    def best_speed_solution(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"]  # 1000，2000，3000
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]  # 100~900
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]  # 10~90
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]  # 1~9
        return (
            M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]
        )


print(Solution().intToRoman(4))
