class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for i in nums:
            map[i] = map.get(i,0) + 1

        
        sorted_ = sorted(map.items() , key=lambda x : x[1],reverse=True)

        res = []
        for i in sorted_[:k]:
            res.append(i[0])
        return res

        
        

        