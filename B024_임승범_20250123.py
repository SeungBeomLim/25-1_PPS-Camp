# B024. Relative Ranks - Leetcode
# sort 함수와 enumerate를 사용하는 방법에 대해서 공부해보기

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(enumerate(score), key=lambda x:-x[1])
        
        result = [""] * len(score)
        for rank, (index, _) in enumerate(sorted_scores):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)
        
        return result