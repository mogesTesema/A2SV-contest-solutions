class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for dir in path:
            if dir =="..":
                if stack:
                    stack.pop()
            else:
                if dir != "." and dir != "":
                    stack.append(dir)
        return "/" + "/".join(stack)
"concrete example for testing input"
path = "/home/user/Documents/..//Pictures"
path = path.split('/')
print(path) #output: ['', 'home', 'user', 'Documents', '..', '', 'Pictures']