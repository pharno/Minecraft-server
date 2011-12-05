import stackless

def make_tasklet(cls):
    def wrap(*args, **kw):
        cl = cls(*args, **kw)
        return stackless.tasklet(cl.run)()
    return wrap