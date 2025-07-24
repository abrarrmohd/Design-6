from collections import defaultdict
from heapq import heappop, heappush

class Sentence:
    def __init__(self, s, freq):
        self.s = s
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.s > other.s
        return self.freq < other.freq

class TrieNode:
    def __init__(self):
        self.children = [None for i in range(27)]
        self.isEnd = False
        self.minHeap = []

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.currString = ""
        self.freqMap = defaultdict(int)
        self.trieRoot = TrieNode()

        self.curr = self.trieRoot
        for i in range(len(sentences)):
            word = sentences[i]
            self.freqMap[word] = times[i]
            self.buildTrie(word, self.trieRoot, times[i])
            
        
    def buildTrie(self, word, root, count):
        curr = root
        for ch in word:
            idx = 26 if ch == " " else ord(ch) - ord('a')

            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            
            curr = curr.children[idx]
            sameWordFound = False
            for i in range(len(curr.minHeap)):
                if word == curr.minHeap[i].s:
                    sameWordFound = True
                    break
            newWord = Sentence(word, count)
            if sameWordFound:
                tmpMinHeap = []
                newWord = Sentence(word, count)
                for tmpsentence in curr.minHeap:
                    if tmpsentence.s != word:
                        heappush(tmpMinHeap, tmpsentence)
                curr.minHeap = tmpMinHeap

            heappush(curr.minHeap, newWord)
            while len(curr.minHeap) > 3:
                heappop(curr.minHeap)
            # if word == "i a":
            #     for i in range(len(curr.minHeap)):
            #         print(curr.minHeap[i].s)
            #     #print(sent.freq for sent in curr.minHeap)
            
        curr.isEnd = True
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.freqMap[self.currString] += 1
            self.buildTrie(self.currString, self.trieRoot, self.freqMap[self.currString])
            self.currString = ""
            self.curr = self.trieRoot
            return []

        self.currString += c
        idx = 26 if c == " " else ord(c) - ord('a')

        if not self.curr or not self.curr.children[idx]:
            self.curr = None
            return []

        self.curr = self.curr.children[idx]

        res = [s.s for s in sorted(self.curr.minHeap, key=lambda x: (-self.freqMap[x.s], x.s))]
        return res


        # Return sorted copy of current heap
        #return [s.s for s in sorted(self.curr.minHeap, key=lambda x: (-x.freq, x.s))]




# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)