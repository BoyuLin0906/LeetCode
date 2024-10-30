"""
Runtime 145 ms / Beats 52.25%
Memory 18.14 MB / Beats 8.84%
"""

from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.booking = SortedList([(0, 0), (10**9, 10**9)])

    def book(self, startTime: int, endTime: int) -> bool:
        if self.is_booked(startTime, endTime):
            return False

        self.book_time(startTime, endTime)
        return True

    def is_booked(self, startTime, endTime):
        
        left_idx = 0
        right_idx = len(self.booking)-1
        while left_idx <= right_idx:
            middle_idx = (right_idx + left_idx) // 2

            if self.booking[middle_idx][1] <= startTime and endTime <= self.booking[middle_idx+1][0]:
                return False
            elif self.booking[middle_idx][0] < startTime:
                left_idx = middle_idx + 1
            else:
                right_idx = middle_idx - 1
 
        return True 

    def book_time(self, startTime, endTime):
        self.booking.add((startTime, endTime))
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)