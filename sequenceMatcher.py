import difflib

a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = []
def sequ(a1, a2):
    words1 = a1
    words2 = a2
    matcher = difflib.SequenceMatcher(a = words1, b = words2)
    for block in matcher.get_matching_blocks():
        if block.size == 0:
            continue
        yield ' '.join(words1[block.a:block.a + block.size])
print(list(sequ(a1, a2)))
