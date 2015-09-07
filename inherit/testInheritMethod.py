# !/usr/bin/evn python
# coding=utf-8

__author__ = 'zuozuo'

class Parent(object):

    def __init__(self):
        print 'Parent init~'
        # self.first_child = self.get_child()
        self.name = 'haha'

    def run(self):
        print 'I can run'

    def fly(self):
        print 'I can fly'

    def let_child_run(self):
        self.get_child().run_and_fly()

    def get_child(self):
        return FirstChild()
class FirstChild(Parent):
    #
    # def __init__(self,):
    #     pass

    def run_and_fly(self):
        super(FirstChild, self).run()
        super(FirstChild, self).fly()
        self.die()
        print self.name

    def die(self):
        print 'I won\'t die!'

    # def run(self):
    #     super(FirstChild, self).run()

Parent = Parent('hehe')
Parent.let_child_run()
