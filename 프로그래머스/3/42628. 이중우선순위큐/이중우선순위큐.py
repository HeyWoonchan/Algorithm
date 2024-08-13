import heapq
def solution(operations):
    heap = []
    for op in operations:
        command, num = op.split()
        if command == 'D':
            if not heap:
                continue
            if num =='1':
                heap.remove(heapq.nlargest(1,heap)[0])
            else:
                heapq.heappop(heap)
        else:
            heapq.heappush(heap,int(num))
    return [heapq.nlargest(1,heap)[0], heap[0]] if heap else [0,0]





