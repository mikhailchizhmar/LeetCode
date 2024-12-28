# https://leetcode.com/problems/meeting-rooms-ii

def min_meeting_rooms(intervals):
    start = sorted([i for i, j in intervals])
    end = sorted([j for i, j in intervals])
    # start = sorted([i.start for i in intervals])
    # end = sorted([i.end for i in intervals])
    res, count = 0, 0
    s, e = 0, 0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    return res


print(min_meeting_rooms([(0, 30), (5, 10), (15, 20)]))
