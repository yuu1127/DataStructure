# PythonによるDataStructure及びMock Interview向け

学んだData Strcutureの整理+置き場
## 大前提::コーディング質問ですぐに使えるようにしておくことが必須のもの
`sorted()` ... `reverse=true`やLambdaでソート方法の指定が可能
バブルソートなのでtime complexityはO(NlogN)
```commandline
$ sorted(<list>, reverse=True)
```
`lambda` ... sortedや他のメソッドと使うことが多い
```commandline
$ lambda a, b, c : a + b + c
```
`dictionary` ... 初期値がない状態で処理をしたい場合はdefaultdict。
items()を使いよく(key, value)の形にするほかkeys,valuesもよく使う
```commandline
$ g = {1:'one'}
$ g.update({2:'two'})
$ g.items() 
```
`math sqrt` ... sqrtは意外と使う。sqrt(x**+y**)のような形で
```commandline
$ sqrt(3)
```
`stack(pop()メソッド)`... pythonは通常のlistをstackとして扱える
```commandline
$ stack.append()
$ stack.pop()
```
`while` ... for文に慣れていると書き方忘れている
```commandline
$ while i > 0:
$   print(i)
$   i -= 1
```

`deque ` ... popleft()とかよく使う、主にBinary Treeでよく使う
```commandline
$ deque = collections.deque()
$ deque.append(root)
$ node = deque.popleft()
```
`enumerate` ... iteratorのカウントを返してくれる、index表示に便利
```commandline
$ names = ['Alice','kuma','omae']
$ e = [j for j in enumerate(names)]
```


## 基本データ構造
`stact.py` ... pythonでのstackクラス   
`queue.py` ... pythonでのqueueクラス  
`stack_and_queue.py` ... stack, queueによる探索法

