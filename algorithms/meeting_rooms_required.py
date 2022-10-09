from data_structures.min_heap import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def get_number_of_rooms_needed(meetings):
    if len(meetings) == 0:
        return

    meetings.sort(key=lambda x: x.start)

    min_heap = Heap()
    min_heap.insert(meetings[0].end)
    count = 1

    for meeting in meetings[:1]:
        if meeting.start < min_heap.peek_min():
            count = count + 1
            min_heap.insert(meeting.end)
        else:
            current_min = min_heap.extract_min()

            min_heap.insert(min(current_min, meeting.end))

    return count


