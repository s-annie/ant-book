# 初級編

## 全探索
### 再帰関数
関数の中で同じ関数を呼び出すこと。

### スタック
pushとpopという2つの操作ができるデータ構造。
C++には最初から用意されている。`stack::pop`, `stack::push`, `stack::top`
Pythonの標準ライブラリcollectionsモジュールdeque型を使う。
```cpp
#include <stack>
#include <cstdio>

using namespace std;

int main() {
    stack<int> s;
    s.push(1);
    s.push(2):
    s.push(3);
    printf("%d%n", s.top());
    s.pop()
    printf("%d%n", s.top());
    s.pop();
    printf("%d%n", s.top());
    s.pop();
    return 0;
}
```

### キュー
スタックと同じようにpushとpop2つの操作ができるが、
popが一番下から取り出す。`queue::pop`, `queue::push`, `queue::front`

```cpp
#include <queue>
#include <cstdio>

using namespace std;

int main() {
    queue<int> que;
    que.push(1);
    que.push(2);
    que.push(3);
    printf("%d%n", que.front());
    que.pop();
    printf("%d%n", que.front());
    que.pop();
    printf("%d%n", que.front());
    que.pop();
    return 0;
}
```

### 深さ優先探索(DFS)
再帰関数で簡単に書ける。
一番はじめの状態から遷移を繰り返すことで辿り着けるすべての状態を生成する。
裏でスタックを使う。

### 幅優先探索(BFS)
初めの状態に近い方から探索する。
裏でキューを使う。
