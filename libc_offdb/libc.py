import os
from pwn import ELF
from pwn import context
try:
    import cPickle as pickle
except ImportError:
    import pickle

class hide_log():
    def __enter__(self):
        global context
        self.default_log_level = context.log_level
        context.log_level = 'error'

    def __exit__(self, type, value, traceback):
        global context
        context.log_level = self.default_log_level


def find_libc(address, symbol, libc_name=None):
    with hide_log() as hidden:
        ret = []
        if address is int:
            address = hex(address)
        directory = os.path.expanduser('~/.libc_offdb/')
        if libc_name is None:
            for root, dirs, files in os.walk(directory):
                for f in files:
                    if f.endswith('.dump'):
                        with open(os.path.join(directory, f), 'rb') as fp:
                            dic = pickle.load(fp)
                        try:
                            found = dic[symbol]
                            if hex(found).endswith(address):
                                print 'found:'
                                print 'name: ' + f[:-5]
                                ret.append(dic)
                        except KeyError:
                            continue
        else:
            try:
                with open(os.path.join(directory, libc_name)) as fp:
                    dic = pickle.load(fp)
                found = dic[symbol]
                return [dic]
            except KeyError:
                raise KeyError('libc not found')
        if not len(ret):
            raise KeyError('libc not found')
        else:
            return ret


def get_libcs():
    with hide_log() as hidden:
        directory = os.path.expanduser('~/.libc_offdb/')
        walk = os.walk(directory)
        if not os.path.exists(directory):
            raise Exception("You haven't download libc yet, please download libc")
            return None
        elfs = []
        cnt = 0
        for root, dirs,files in walk:
            for f in files:
                cnt += 1
                if f.endswith('.dump'):
                    continue
                elfs.append(ELF(os.path.join(directory, f)))
        if cnt == 1:
            raise Exception("You haven't download libc yet, please download libc")
        return elfs
