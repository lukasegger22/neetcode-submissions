class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        left = 0
        max_length = 0  # Hier speichern wir den Rekord!
        
        for right in range(len(s)):
            # Phase 1: Kontraktion (Solange Duplikat da, räum links auf)
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            
            # Phase 2: Expansion (Jetzt ist Platz, füge hinzu)
            unique.add(s[right])
            
            # Rekord aktualisieren
            max_length = max(max_length, right - left + 1)
            
        return max_length