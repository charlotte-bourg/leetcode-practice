class Solution:
    def simplifyPath(self, path: str) -> str:
        fileStack = []
        i = 0 
        while i < len(path):
            if path[i] == "/":
                i += 1 
            else: 
                j = i 
                while j < len(path) and path[j] != '/':
                    j += 1
                seg = path[i:j]
                if seg == ".":
                    pass
                elif seg == "..":
                    if fileStack:
                        fileStack.pop() 
                else:
                    fileStack.append(seg)
                i = j + 1
        print(fileStack)
        canonical = "/".join(fileStack)
        return "/"+canonical