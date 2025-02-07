class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        ci = 0
        o = 0
        for i in range(len(chars) + 1):
            c = chars[i] if i < len(chars) else None
            if c == chars[o]:
                continue
            if i - ci > 1:
                g = str(i - ci)
                for gc in g:
                    o += 1
                    chars[o] = gc
            o += 1
            if c is None:
                continue
            chars[o] = c
            ci = i
        return o
