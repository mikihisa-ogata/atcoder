list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [10, 20, 30]

# zip関数を使って複数のリストの要素をまとめてタプルとして取得
zipped = zip(list1, list2, list3)

# zipオブジェクトをリストに変換して表示
result = list(zipped)
print(result)  # 出力: [(1, 'a', 10), (2, 'b', 20), (3, 'c', 30)]
