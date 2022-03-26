from typing import List

class Heap:
    """
    Time: O(NLogN)
    Space: O(N) for heap
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        import heapq
        heapq.heapify(heap)
        # push into end time of meeting
        heapq.heappush(heap, intervals[0][1])
        
        for interval in intervals[1:]:
            # if start time of current meeting is large than or equal to the minimum end time for the meetings that have started before
            # alternate top one meeting which has finished
            if interval[0] >= heap[0]:
                heapq.heappushpop(heap, interval[1])
            else:
                heapq.heappush(heap, interval[1])
        
        return len(heap)
                

        