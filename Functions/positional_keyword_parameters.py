def f(x, y, *args):
    print(x + y + sum(args))
    
    
f(1, 2, 3, 4, 5)

# TODO: Make this tutorial for myself well explained with *args, **kwargs, * and / separators for positional and keyword only arguments