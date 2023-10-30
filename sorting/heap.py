# Heap Sort
'''
    각 메서드의 수행시간 
        1. heapify_down
            -> 최악의 경우, heap의 높이만큼 상수시간 연산을 반복한다.
            -> 높이 = log n
            -> O(log n)
        2. make_heap
            -> 가장 마지막 leap node부터 root node까지 heapify_down 반복
            -> n * log n
            -> O(n*log n)
        3. heap_sort
            ->  heapify_down을 n - 1번 호출
            -> (n - 1) * log n
            -> O(n*log n)
'''

class Heap:
    def __init__(self):
        self.list = list(map(int, input().split()))
        self. n = len(self.list)

    def heapify_down(self, index, n):
        while 2*index + 1 < n: # leaf node인지 확인
            # 자식노드들과 부모노드 중 더 큰값의 index를 선택한다.
            max_index = index
            if self.list[max_index] < self.list[2*index + 1]:
                max_index = 2*index + 1
            if 2*index + 2 < n and self.list[max_index] < self.list[2*index + 2]:
                max_index = 2*index + 2
            
            if max_index != index:
                self.list[max_index], self.list[index] = self.list[index], self.list[max_index]
                index = max_index
            else:
                break # max_index를 root node로 가지는 subheap는 이미 정렬된 상태이다. 
    
    def make_heap(self):
        for index in range(self.n - 1, -1, -1):
            self.heapify_down(index, self.n)

    def heap_sort(self):
        self.make_heap()
        for i in range(self.n - 1, 0, -1):
            self.list[0], self.list[i] = self.list[i], self.list[0]
            self.heapify_down(0, i)


heap = Heap()
heap.heap_sort()