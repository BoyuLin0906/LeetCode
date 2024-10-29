'''
Runtime 23 ms / Beats 82.35%
Memory 29.58 MB / Beats 73.10%
'''

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        result = [folder[0]]

        for idx in range(1 ,len(folder)):
            last_folder = result[-1] + "/"

            current_folder = folder[idx]
            if not current_folder.startswith(last_folder):
                result.append(current_folder)

        return result