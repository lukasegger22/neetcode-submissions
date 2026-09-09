class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        # Sicherheitsschritt: Direkt am Anfang alles auf 32-Bit zwingen
        a = a & mask
        b = b & mask
        
        while b:
            # Tuple-Unpacking: Berechnet Summe und Übertrag gleichzeitig
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            
        # Wenn a positiv ist (kleiner gleich der maximalen positiven 32-Bit Zahl)
        if a <= 0x7FFFFFFF:
            return a
        # Wenn a negativ ist, für Python zurückübersetzen
        else:
            return ~(a ^ mask)