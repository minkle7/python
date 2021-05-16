def annouance(f):
    def wrapper():
        print("running the function .......")
        f()
        print("done with the task")
    return wrapper
@annouance

def hello():
    print("hello my name is minkle")        


hello()