import textwrap
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-","")
        S = S[::-1]
        S = textwrap.wrap(S,K)
        S = "-".join(S)
        return S[::-1]


t = Solution()
print(t.licenseKeyFormatting("2-5g-3-J",2))