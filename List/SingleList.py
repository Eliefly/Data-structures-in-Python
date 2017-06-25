# coding: utf-8

class LNode(object):
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

class LinkedListUnderflow(ValueError):
    pass

class SingleList(object):
    '''
    单链表
    '''
    def __init__(self, *args):
        if len(args) == 0:
            self._head = None
        else:
            self._head = LNode(args[0])
            for ele in args[1:]:
                self.append(ele)

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def append(self, elem):
        '''
        尾部增加元素
        '''
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop(self):
        '''
        弹出首个元素
        '''
        if self.is_empty() is True:
            raise LinkedListUnderflow('in pop')
        ret = self._head.elem
        self._head = self._head.next
        return ret

    def pop_last(self):
        '''
        弹出最后一个元素
        '''
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next is None:
            ret = p.elem
            self._head = None
            return ret
        while p.next.next is not None:
            p = p.next
        ret = p.next.elem
        p.next = None
        return ret

    def printall(self):
        '''
        打印所有元素
        '''
        p = self._head
        print('[', end='')
        while p is not None:
            if p.next is not None:
                print(p.elem, end=', ')
            else:
                print(p.elem, end='')
            p = p.next
        print(']')

    def __str__(self):
        p = self._head
        outstr = '['
        while p is not None:
            if p.next is not None:
                outstr = outstr + str(p.elem) + ', '
            else:
                outstr = outstr + str(p.elem)
            p = p.next
        outstr = outstr + ']'
        return outstr

    def __repr__(self):
        return self.__str__()


    def foreach(self, proc):
        '''
        遍历处理元素
        '''
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def elements(self):
        '''
        元素生成器
        '''
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def len(self):
        '''
        获取链表长度
        '''
        p = self._head
        i = 0
        while p is not None:
            p = p.next
            i = i + 1
        return i

    def insert(self, pos, elem):
        '''
        表中位置pos插入元素elem
        '''
        if self.len() < pos:
            raise LinkedListUnderflow('in insert')
        if pos == 0:
            self.prepend(elem)
            return
        p = self._head
        index = 0
        while p is not None:
            index = index + 1
            if index == pos:
                break
            p = p.next
        p.next = LNode(elem, p.next)

    def popitem(self, pos=0):
        '''
        位置pos弹出元素
        '''
        if pos < 0 or not isinstance(pos, int):
            raise LinkedListUnderflow('in popitem')
        if pos == 0:
            self.pop()
        elif pos > 0:
            if pos > self.len()-1:
                raise LinkedListUnderflow('in popitem')
            else:
                p = self._head
                index = 0
                while p is not None:
                    pre = p 
                    p = p.next
                    index = index + 1
                    if pos == index:
                        pre.next = p.next
                        break



if __name__ == '__main__':
    lst = SingleList(1, 2, {'name': 'jack'})
    print(lst.len())
    print(lst)

    lst.popitem(1)
    print(lst)


    print(lst.is_empty())
    lst.insert(1, 'DDDD')
    lst.append('B')
    lst.printall()
    print(lst.len())
    print(lst)

    lst.pop()
    lst.prepend('C')

    lst.insert(0, 'FF')
    lst.printall()
    print(lst.len())
    print(lst.is_empty())

    print(type(lst.elements()))

    for ele in lst.elements():
        print(ele)