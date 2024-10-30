"""
Runtime 468 ms / Beats 12.91%
Memory 17.63 MB / Beats 15.30%
"""

class MyCalendar:

    def __init__(self):
        self.booking = [(0, 0), (10**9, 10**9)]

    def book(self, startTime: int, endTime: int) -> bool:
        if self.is_booked(startTime, endTime):
            return False

        self.insert(startTime, endTime)
        return True

    def is_booked(self, startTime, endTime):
        for idx in range(1, len(self.booking)):
            prev_end_time = self.booking[idx-1][1]
            next_start_time = self.booking[idx][0]
            if prev_end_time <= startTime and next_start_time >= endTime:
                return False

        return True 

    def insert(self, startTime, endTime):
        self.booking.append((startTime, endTime))
        self.booking.sort()
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)