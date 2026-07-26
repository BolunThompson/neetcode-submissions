class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pending_temps = [] # i
        results = [0 for _ in temperatures]
        for i, t in enumerate(temperatures):
            while pending_temps and t > temperatures[pending_temps[-1]]:
                resolved_day = pending_temps.pop()
                results[resolved_day] = i - resolved_day
            pending_temps.append(i)
        return results