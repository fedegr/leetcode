class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = {}
        colors_count = 0
        answer = []
        for ball, color in queries:
            previous_color = balls.get(ball, None)
            balls[ball] = color
            
            color_used_count = colors.get(color, 0)
            colors[color] = color_used_count + 1
            
            colors_count += 1 if color_used_count == 0 else 0
            if previous_color is not None:
                colors[previous_color] -= 1
                colors_count -= 1 if colors[previous_color] == 0 else 0
            
            answer.append(colors_count)
        return answer
