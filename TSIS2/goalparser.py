class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        for i in range(0, len(command) - 1) :
            if command[i] == "(":
                if command[i+1] == ')':
                    res += 'o'
                else:
                    res += "al"
            elif command[i] == "G" :
                res += "G"
        if command[len(command) - 1 ] == 'G':
            res += 'G'
        return res