class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        n = len(candies)
        result = []
        max_element = max(candies)

        for candy in candies:
            total = extraCandies + candy
            if(total >= max_element):
                result.append(True)
            else:
                result.append(False)   

        return result             





