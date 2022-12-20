class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        queue = []
        visited = set() 
        total_room = len(rooms) 
        
        queue.append(0)
        visited.add(0)

        while queue:
            key = queue.pop(0)
            for key_to_room in rooms[key]:
                if not key_to_room in visited:
                    visited.add(key_to_room)
                    queue.append(key_to_room)

        return len(visited) == total_room