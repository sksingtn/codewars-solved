class RomanNumerals: 
    @staticmethod    
    def to_roman(number):
        roman = ""
        chart = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        for digit in sorted(chart,reverse = True):
            roman += chart[digit]*(number//digit)
            number = number%digit
    
        return roman
    @staticmethod    
    def from_roman(roman):
        chart ={'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        roman_pad = str(roman) + str("0")
        a = iter(range(len(roman)))
        number = 0
        for i in a:
            if roman_pad[i:i+2] in chart:
                number += chart[roman_pad[i:i+2]]
                next(a)
            elif roman_pad[i:i+1] in chart:
                number += chart[roman_pad[i:i+1]]

        return number
