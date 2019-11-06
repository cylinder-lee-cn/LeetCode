"""
535. TinyURL 的加密与解密


TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，
它将返回一个简化的URL http://tinyurl.com/4e9iAk.

要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。
你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，
并且这个TinyURL可以用解密方法恢复成原本的URL。

"""


class Codec:
    def __init__(self):
        self.urls = {}
        self.k = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        short = 'http://tinyurl.com/' + str(self.k)
        self.urls[short] = longUrl
        self.k = self.k + 1
        return short

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        return self.urls[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
"""
此题解法：
* 投机取巧，将long url放入字典，给个顺序值是key就行了
"""
