# OVER-RIDING
class A:
    def fun1(self):
        print('feature_1 of class A')

    def fun2(self):
        print('feature_2 of class A')


class B(A):
    def fun1(self):
        print('Modified feature_1 of class A by class B')

    def fun3(self):
        print('feature_3 of class B')


obj = B()
obj.fun1()

# OVER-LOADING

# In Python, unlike some other languages, method overloading is not
# directly supported. When you define multiple methods with the same
#  name in a class, only the last one defined will be retained.
#  Python will not distinguish between them based on the number or type of arguments.

# If you want to achieve behavior similar to method overloading,
# you can use default values for the parameters and then provide
# appropriate implementations based on the provided arguments.
# Here's how you could modify your code to achieve this:


class C:
    def fun1(self, msg=None):
        if msg is None:
            print('feature_1 of class A')
        else:
            print(f'feature_2 of class A {msg}')


obj = C()
obj.fun1()
obj.fun1('OVERRIDE')
