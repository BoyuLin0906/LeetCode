class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Runtime 67 ms / Beats 93.24% 
        Memory 14.5 MB / Beats 39.38%
        """
        graph = defaultdict(set)
        queue = []
        visited = set() 
        total_room = len(rooms) 

        for idx in range(total_room):
            for key in rooms[idx]:
                graph[idx].add(key)
        
        queue.append(0)
        visited.add(0)

        while queue:
            room = queue.pop(0)
            for key_to_room in graph[room]:
                if not key_to_room in visited:
                    visited.add(key_to_room)
                    queue.append(key_to_room)
                    
        return len(visited) == total_room