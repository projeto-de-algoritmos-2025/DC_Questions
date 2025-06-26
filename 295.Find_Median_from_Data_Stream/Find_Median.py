import heapq

class MedianFinder:
    def __init__(self):
        # max-heap (valores negativos simulam um max-heap)
        self.valormax = []
        # min-heap
        self.crescente = []

    def addNum(self, num: int) -> None:
        # Adiciona à max-heap (invertida)
        heapq.heappush(self.valormax, -num)

        # Move o maior da max-heap para a min-heap
        heapq.heappush(self.crescente, -heapq.heappop(self.valormax))

        # Garante que valormax tenha tamanho igual ou maior
        if len(self.valormax) < len(self.crescente):
            heapq.heappush(self.valormax, -heapq.heappop(self.crescente))

    def findMedian(self) -> float:
        if len(self.valormax) > len(self.crescente):
            return -self.valormax[0]
        return (-self.valormax[0] + self.crescente[0]) / 2.0
