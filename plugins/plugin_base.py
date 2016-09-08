import abc
class base(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getinfo(self):
        pass
