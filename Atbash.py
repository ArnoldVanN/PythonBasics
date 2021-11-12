class Atbash:
    def solve(self, text):
        N = ord('z') + ord('a')
        noWhiteSpace = text.replace(" ", "")
        ans = ''
        b = ans.join([chr(N - ord(s)) for s in noWhiteSpace])
        return ' '.join([b[i:i+5] for i in range(0, len(b), 5)])
ob = Atbash()
print(ob.solve("abcdefg"))
print(ob.solve("hello my name is arno does this actually work"))