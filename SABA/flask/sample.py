from flask import Flask,redirect,url_for

a=Flask(__name__)

@a.route('/')
def new():
    return'TVK FOR TN'
@a.route('/tn')
def g():
    return 'Thalapathy'
def f():
    return 'PARAMA PADI DA'
a.add_url_rule('/s',view_func=f)
@a.route('/user/<c>')
def s(c):
    return f'{c} ajitheyyy'
if __name__=='__main__':
    a.run()

