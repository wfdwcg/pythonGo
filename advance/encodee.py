###1.base64
import base64
import hashlib

strr = "hello world"
strEncoded = base64.b64encode(str.encode(strr))
print(strEncoded)

strDeEncoded = base64.b64decode(strEncoded)
print(bytes.decode(strDeEncoded))


###2.MD5哈希 sha256加密
hashh = hashlib.md5()
hashh.update(str.encode("hello"))
print("\n\nhashedValue: " + hashh.hexdigest())


hashSha256 = hashlib.sha256()
hashSha256.update(str.encode("hello"))
print("hashSha256Value: " + hashSha256.hexdigest())

###加盐加密
hashSha256s = hashlib.sha256(str.encode("saltt"))
hashSha256s.update(str.encode("hello"))
print("hashSha256SaltValue: " + hashSha256s.hexdigest())
