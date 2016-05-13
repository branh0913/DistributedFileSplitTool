import abc

'''
Wrapper for all Database backend's
'''


class DBCommander(object):

    _dbtype = None
    _conn_string = None

    def __init__(self, dbtype):

        self._dbtype = dbtype

    @abc.abstractclassmethod
    def connect(self):
        pass

    @abc.abstractclassmethod
    def insert(self):
        pass

    @abc.abstractclassmethod
    def clear_db(self):
        pass

    @abc.abstractclassmethod
    def close_db(self):
        pass

    def drop_db(self):
        pass


