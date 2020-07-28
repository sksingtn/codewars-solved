import re
def decodeBits(bits):
    bits=bits.strip("0")
    u = len(sorted(re.findall(r'0+',bits)+re.findall(r'1+',bits),key=len)[0])
    dot,dash,pause,pause_ch,pause_wo="1"*u,"111"*u,"0"*u,"000"*u,"0000000"*u
    decoded = bits.replace(dash,"-").replace(dot,".").replace(pause_wo," G ").replace(pause_ch," ").replace(pause,"")
    return decoded

def decodeMorse(morseCode):
    decrypt = ""
    for x in morseCode.split(" "):
        if x != "G":decrypt+=MORSE_CODE[x]            
        else: decrypt+=" "           
    return decrypt      
