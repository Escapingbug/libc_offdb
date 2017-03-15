# libc-offdb
A simple tools to extract symbols from libcs

# simple install
    git clone https://github.com/Escapingbug/libc_offdb
    sudo python setup.py install
    download_libcs

# simple usage
    from libc_offdb.libc import find_libc, get_libcs
    libcs = get_libcs # this will take a while, but it gives you all the libcs it has
    wanted_libc = find_libc('a10', 'scanf') # given a offset(last few is OK), and a symbol
    # and this will give you a list of dict of symbols:offset pair
