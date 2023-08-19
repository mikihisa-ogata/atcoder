from queue import Queue

# キューの作成
q = Queue()

# 要素の追加
q.put(1)
q.put(2)
q.put(3)

# 要素の取得
# 先入先出
item = q.get()
print(item)  # 出力: 1

# 空でないかの確認
if not q.empty():
    item = q.get()
    print(item)  # 出力: 2

# キューが空かどうかの確認
if q.empty():
    print("キューは空です")

# キューの要素数を取得
size = q.qsize()
print(size)  # 出力: 1

# 複数の要素を追加
q.put(4)
q.put(5)
q.put(6)

# 要素を全て取り出す
while not q.empty():
    item = q.get()
    print(item)
