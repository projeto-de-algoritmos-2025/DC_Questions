class Solution:
    def getSkyline(self, buildings):
        if not buildings:
            return []

        # Caso base: apenas um prédio
        if len(buildings) == 1:
            x1, x2, h = buildings[0]
            return [[x1, h], [x2, 0]]

        # Divide ao meio
        mid = len(buildings) // 2
        left_skyline = self.getSkyline(buildings[:mid])
        right_skyline = self.getSkyline(buildings[mid:])

        # Conquista: mescla os dois skylines
        return self.mergeSkylines(left_skyline, right_skyline)

    def mergeSkylines(self, left, right):
        i = j = 0
        h1 = h2 = 0
        result = []
        prev_height = 0

        while i < len(left) and j < len(right):
            # Ponto com menor coordenada x
            if left[i][0] < right[j][0]:
                x, h1 = left[i]
                i += 1
            elif right[j][0] < left[i][0]:
                x, h2 = right[j]
                j += 1
            else:
                x = left[i][0]
                h1 = left[i][1]
                h2 = right[j][1]
                i += 1
                j += 1

            max_height = max(h1, h2)
            if max_height != prev_height:
                result.append([x, max_height])
                prev_height = max_height

        # Adiciona os pontos restantes
        result.extend(left[i:])
        result.extend(right[j:])
        
        # Remove pontos consecutivos com mesma altura
        cleaned = [result[0]]
        for x, h in result[1:]:
            if h != cleaned[-1][1]:
                cleaned.append([x, h])

        return cleaned
