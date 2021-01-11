"""
1116. 打印零与奇偶数
假设有这么一个类：

class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // 构造函数
  public void zero(printNumber) { ... }  // 仅打印出 0
  public void even(printNumber) { ... }  // 仅打印出 偶数
  public void odd(printNumber) { ... }   // 仅打印出 奇数
}
相同的一个 ZeroEvenOdd 类实例将会传递给三个不同的线程：

线程 A 将调用 zero()，它只输出 0 。
线程 B 将调用 even()，它只输出偶数。
线程 C 将调用 odd()，它只输出奇数。
每个线程都有一个 printNumber 方法来输出一个整数。请修改给出的代码以输出整数序列
010203040506... ，其中序列的长度必须为 2n。

示例 1：
输入：n = 2
输出："0102"
说明：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。
正确的输出为 "0102"。

示例 2：
输入：n = 5
输出："0102030405"
"""

import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zeroLock = threading.Lock()
        self.evenLock = threading.Lock()
        self.oddLock = threading.Lock()
        self.evenLock.acquire()
        self.oddLock.acquire()

        # printNumber(x) outputs "x", where x is an integer.

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zeroLock.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.evenLock.release()
            else:
                self.oddLock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            if i <= self.n:
                self.evenLock.acquire()
                printNumber(i)
                self.zeroLock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            if i <= self.n:
                self.oddLock.acquire()
                printNumber(i)
                self.zeroLock.release()


"""
此题解法：
* 设3个锁，分别对应0、奇数、偶数，初始将奇数和偶数都锁上
* zero函数，先锁自己，然后输出0，并且当n为偶数时，打开偶数锁，反之是奇数锁
* even函数，锁自己，输出n，开zero锁
* odd函数，锁自己，输出n，开zero锁
"""
