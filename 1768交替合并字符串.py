word1 = "abc"
word2="pqrst"

#lahelr 简单遍历

def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    ret = []
    for i in range(min(len(word1),len(word2))):
        ret.append(word1[i])
        ret.append(word2[i])
    if len(word1)<len(word2):
        ret.extend(word2[min(len(word1),len(word2)):])
    elif len(word1)>len(word2):
        ret.extend(word1[min(len(word1),len(word2)):])
    return "".join(ret)

print(mergeAlternately(word1,word2))