## Leetcode問題 一言メモ
## time complexity + 番号

`217.Contains Duplicate` ... 簡単、ただソートしてSIZEが違うか見るだけ  
`268.Missing Number` ... range(len)を使って解ける  
`448.Find All Numbers Disappeared in an Array` ... setの差でdiffが取れることを覚えておく  
`136.Single Number` ... defauktdict使えばvalueがNoneでも+1出来ることを使うと簡単、O(n)処理  
`70.Climbing Stairs` ... 少し考えるというか知っている必要がある。1歩、２歩しか歩けないなら全てのルートは1個前のルートと２個前の
ルートを足したものとなる。最初の初期値をどう取るかでループ回数が変わる。  
`121.Best Time to Buy and Sell Stock` ... 頭に図を思い浮かべる必要がある。Profitは買った時から値段が上がることにどんどん増えていく。
profitが-になったらそこが限界で0に直す必要がある。 
`53.Maximum Subarray` ... リストの左から値をどんどん足して蓄積していく。ただ蓄積がマイナスの場合足すとどんどん値が下がっていくのでプラスの時のみ足していく  
`303.Range Sum Query - Immutable` ... 正直この問題の主旨がよくわからないがrangeの使い方を知っていればOK  
`338.Counting Bits` ... ビット演算を知っている必要がある。>>は右にずれて値を減らす（1桁目は消える）
<は左に引っ張り０を追加して値を大きくする。value & 1で一番右が1の時True  
`141. Linked List Cycle` ... LinkedListの初歩問題、亀とうさぎの問題でルートが丸だと絶対いつかslowerはfaseterに会う  
`876. Middle of the Linked List` ... 一番簡単な方法は最初にlengthを求めてlength/2でreturnすればいい  
`234. Palindrome Linked List` ... 一番簡単な方法はリストに全部入れてスライスを使えばいい  
`203. Remove Linked List Elements` ... LinkedListの初歩問題、ポイントは一番最初のnodeが消える可能性があるので最初にListNode(-1)というダミーのheadを作ってそれに
対象リストをつないで置けばいい  
`83. Remove Duplicates from Sorted List` ... LinkedListとWhileをうまく使えるか、違う値を持つnodeが出るまでループすればいい  
`206. Reverse Linked List` ... 個人的に割と考えるの難しい、currを定義してcurrを進ませながらcurr.next = prev prev = currと順番を再定義していく  
`21. Merge Two Sorted Lists` ... 今回もdummyを定義して最初の位置を覚えていく、そしてリスト1,2を比較しながらcurr.nextに入れていくが最後が少しポイントで
cur.next = list1 or list2とやることでNoneじゃない方をお尻につけてやればいい  
`704. Binary Search` ... O(log n)でやる必要があるのでタイトルどおりListでBinary Searchする必要がある
sortedリストでこれをやる場合まず真ん中を見てその真ん中次第でleft = mid + 1, right = mid - 1としてループしてやればいい。基本マージソートと考え方が同じ  
`744. Find Smallest Letter Greater Than Target` ... 多分leetcodeの中で一番簡単な問題の部類に入るだろうが左から見てtargetより大きければreturnしてやれば良い  
`852. Peak Index in a Mountain Array` ... 中々面白い問題でリストの中の山を見つけるという問題だがこれもマージソートと同じ考え方で真ん中とその+1を比べて
見る範囲を小さくして(l=m+1, r=m)挟んでいけば最終的にPeakが残る(left == rightになる。)  
`637. Average of Levels in Binary Tree` ... levelごとのBinary Treeなのでdeque使う。他のと同じように根をpopleftして葉をappendすればいい  
`111. Minimum Depth of Binary Tree` ... deque使ってBFSすればいい。葉がleftもrigthもNoneならそこがminimum depth  
`100. Same Tree` ... ２つqueueを使ってもいいがqueue.append((p, q))の形で入れてやればいい  
`112.Path Sum` ... Recursion, targetsum(合計値)からroot.valueをどんどん減らしてけばいい
false or true or false == True
(this left is from previous return left or right so actually do left or right or different left or right)  
`104.Maximum Depth of Binary Tree` ... Binary treeの問題でレベルごとに追っていく問題は基本dequeとpopleftを使えば解決できる  
`543.Diameter of Binary Tree` ... 現在のnodeのheightは1 + max(node.left, node.right)で計算できる  
`617. Merge Two Binary Trees` ... BinaryTreeなのでdeque、mergeの場合どちらかを基準にしてもう一個のnodeを足していくイメージ
（元のnode飲みの場合はvalueが0のnodeを作っておく)  
`235. Lowest Common Ancestor of a Binary Search Tree` ... Binary Treeの構造を理解しておく必要がある
葉がどっちも根より大きいならnode.rightに移動していけばいい（逆も然り）O(log(n))  
`226. Invert Binary Tree` ... BinaryTreeでDFSで処理をしていく、node.leftとnode.rightを入れ替えてやればいい  
`1. Two Sum` ... 一番簡単な方法はリストの組み合わせを使う。
```
for i in range(length - 1):
       for j in range(i + 1, l):
```  
`977. Squares of a Sorted Array` ... かなり簡単、lambda式か内的表現で書けると一行で終わる  
`844. Backspace String Compare` ...
 要は#の時一番後ろの要素を削ればいい+returnのための文字を新しく定義してそれにどんどん追加していけばいいことに気づけばOK
pythonなのでスライス[:-1]でも[].pop()でも最後を取り出すことが可能  
`169. Majority Element` ... defaultdictを使えば簡単だが要素の中の最大がn/2より上ということは要素をcountしていけば絶対出現回数が0より上になるものと同意  
`2022. Convert 1D Array Into 2D Array` ... よく考えればそんな難しくない [].append([Slice])の形が思い浮かぶかどうかが大事  
`242. Valid Anagram` ... LeetCodeの中でも際簡単な部類に入る以下略、listにしてsortしてやればいい  
`49. Group Anagrams` ... パッと見難しそうだが(Mediumだし)よく考えればkeyをanagramにしてそのvaluesを返してやれば終わり
やはりdefaultdictは偉大（何もなくてもdefualtdict(list)だとappendできるから）  
`347. Top K Frequent Elements` ... 各値に対して出現回数用のdefaultdict(int)と各出現頻度に対してのdefaultdict(list)を作ってやり
各出現頻度のkeysに対して２重ループでsizeがkになるまでどんどん値を入れてやればいい  
`238. Product of Array Except Self` ... divisionを使わないでindex以外のelementを乗算する。
つまりindexより左のものと右のものを掛けてやればいい  
`271. Encode and Decode Strings` ... 暗号の形をどうするか、文字列と#を付けてやればいい  
`128. Longest Consecutive Sequence` ... 隣あう要素を比べて行けばいいが前処理としてリスト中に
同じ値の場合が存在するのでsetにして重複を消してsortしてやる必要がある  
