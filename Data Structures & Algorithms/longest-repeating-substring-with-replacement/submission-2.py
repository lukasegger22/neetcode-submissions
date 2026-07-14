class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        longest_streak = 0
        
        for right in range(len(s)):
            # 1. Zeichen aufnehmen (sauberer 1-Liner statt 4 Zeilen if/else)
            char = s[right]
            count[char] = count.get(char, 0) + 1
            
            # 2. Den Boss finden
            max_values = max(count.values())
            
            # 3. Kontraktion: Wenn das Budget platzt, linker Zeiger rückt nach
            while (right - left + 1) - max_values > k:
                count[s[left]] -= 1
                left += 1
                
            # 4. Rekord updaten (Fenster ist hier immer 100 % valide)
            longest_streak = max(longest_streak, right - left + 1)

        return longest_streak