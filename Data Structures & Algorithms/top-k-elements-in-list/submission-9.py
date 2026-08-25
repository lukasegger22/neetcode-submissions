class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        for number in nums:
            count[number]=count.get(number,0)+1
        buckets = [[] for _ in range(len(nums) + 1)]
        for number, freq in count.items():
            buckets[freq].append(number)
        result =[]
        for freq in range(len(buckets)-1,0,-1):
            for number in buckets[freq]:
                result.append(number)
                if len(result) == k:
                    return result

        