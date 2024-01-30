class Trie:
    def __init__(self):
        self.root = dict()
        self.size = 0

    def add(self, word, omit_error=True):
        r"""Add one word into the trie. Set`omit_error=False` to enabling error raising when a word already exist in the trie."""
        tgt = self.root
        for ch in word:
            if ch not in tgt:
                tgt[ch] = dict()
            tgt = tgt[ch]

        if 0 in tgt and not omit_error:
            raise ValueError(
                f"Trying to add already existing word {word}!", stacklevel=2
            )

        tgt[0] = True
        self.size += 1

    def __contains__(self, word):
        tgt = self.root
        for ch in word:
            if ch in tgt:
                tgt = tgt[ch]
            else:
                return False
        return 0 in tgt

    def __len__(self):
        return self.size

    def search_with_wildcard(self, word: str) -> bool:
        r"""Use `'.'` as a wildcard in serching"""
        return self.__search_with_wildcard(word, self.root)

    def __search_with_wildcard(self, word, cur):
        for i, ch in enumerate(word):
            if ch == ".":
                return any(self.__search(word[i + 1 :], cur[_]) for _ in cur if _ != 0)
            if ch in cur:
                cur = cur[ch]
            else:
                return False
        return 0 in cur


class TrieWithIDTracking:
    def __init__(self):
        self.root = dict()
        self.length = 0

    def try_to_add(self, word):
        tgt = self.root
        for ch in word:
            if ch in tgt:
                tgt = tgt[ch]
                continue
            else:
                tgt[ch] = dict()
                tgt = tgt[ch]
                continue
        if 0 in tgt:
            return tgt[0]
        else:
            tgt[0] = self.length
            self.length += 1
            return tgt[0]

    def __contains__(self, word):
        tgt = self.root
        for ch in word:
            if ch in tgt:
                tgt = tgt[ch]
                continue
            else:
                return False
        return 0 in tgt

    def get(self, word, default_val=None):
        tgt = self.root
        for ch in word:
            if ch in tgt:
                tgt = tgt[ch]
                continue
            else:
                return default_val
        if 0 in tgt:
            return tgt[0]
        else:
            return default_val

    def __len__(self):
        return self.length
