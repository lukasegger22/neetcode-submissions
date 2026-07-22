class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        half = (len(nums1)+len(nums2)+1)//2
        total_len = len(nums1) + len(nums2)
        left = 0
        right = len(nums1)
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = half - partition1
            
            # 3. Die 4 Kanten definieren (mit Infinity-Schutz für die Ränder)
            L1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            R1 = nums1[partition1] if partition1 < len(nums1) else float('inf')
            
            L2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            R2 = nums2[partition2] if partition2 < len(nums2) else float('inf')
            
            # 4. Der magische Kreuzvergleich
            if L1 <= R2 and L2 <= R1:
                # PERFEKTER SCHNITT GEFUNDEN!
                
                # Bei ungerader Gesamtlänge: Der Median ist das größte Element der linken Seite.
                if total_len % 2 == 1:
                    return float(max(L1, L2))
                
                # Bei gerader Gesamtlänge: Durchschnitt aus größtem links und kleinstem rechts.
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2.0
                
            elif L1 > R2:
                # L1 ist zu groß. Wir müssen den Schnitt im ersten Array weiter nach links schieben.
                right = partition1 - 1
            else:
                # L2 ist zu groß (bzw. L1 zu klein). Wir müssen weiter nach rechts.
                left = partition1 + 1
                
        return -1.0