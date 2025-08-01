class Solution:

    def encode(self, strs: List[str]) -> str:
        en=''
        for i in strs:
            en+=str(len(i))+'#'+i
        return en

    def decode(self, s: str) -> List[str]:
        en=[]
        i=0
        while(i<len(s)):
            j=i
            while(s[j]!="#"):
                j+=1
            length=int(s[i:j])
            en.append(s[j+1:j+1+length])
            i=j+1+length
        return en

