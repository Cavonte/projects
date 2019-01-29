class const(object):
    IMMUTABLE_VALUE = 122


    def   __setattr__(self, *_):
        pass

const = const()

### end
print(const.IMMUTABLE_VALUE)

const.IMMUTABLE_VALUE = 'other'

print(const.IMMUTABLE_VALUE)