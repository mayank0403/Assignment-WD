from flask import Flask,send_file,render_template,request,make_response
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import StringIO
import re
import math
from math import *
import random

app = Flask(__name__)

@app.route('/')
def init():

    return render_template('Home.html')

@app.route('/mayank')
def mayank():

    return render_template('Mayank.html')

@app.route('/ayush')
def ayush():

    return render_template('Ayush.html')

@app.route('/him')
def himanshu():

    return render_template('Himanshu.html')


@app.route('/contact')
def contact():

    return render_template('Contact_us.html')

@app.route('/developers')
def developers():

    return render_template('Developed_by.html')

@app.route('/plt',methods=['GET','POST'])
def plot():
    if request.method=='POST':
        st=request.form['string']
        return render_template('plot.html',source='/plt/'+st)
    else:
        return render_template('plot.html')



@app.route('/plt/<st>')
def cal(st):
    a=1
    if a==1:
        inp = r"[0-9a-z-/*/)/(/*/./+]*"
        num = re.findall(inp, st)
        print(num[0])
        s=num[0]

        listnum=[]
        num[0]=1
        for j in num:
            if(j!=''):
                listnum.append(float(j))
        print(listnum)

        fig=plt.figure()
        plt.clf()

        class Integrate():


            #a is the lower limit of integration
            #b is the upper limit of integration
            #n is the number of divisions and more the number of divisions,more is the accuracy
            #fn is the function whose integration has to be done
            #method : 1.Trapezoidal Rule 2.Simpsons Rule
            #input : a,b,n,fn

            def line_create(self,a,b,c):
                r = lambda: random.randint(0,255)
                ##colr='#%02X%02X%02X' % (r(),r(),r())
                colr='black'
                b=float(b)
                a=float(a)
                c=float(c)
                if b!=0:
                    t=np.arange(-2,30,0.1)
                    y=lambda t:(c-a*t)/b
                    plt.plot(t,y(t),color=colr)
                else:
                    y=np.arange(-2,30,0.1)
                    t=[(c/a)]*(y.size)
                    plt.plot(t,y,color=colr)


            def trap_create(self,x,y,fn):
                self.line_draw((x,0),(y,0))
                self.line_draw((x,0),(x,fn(x)))
                self.line_draw((y,0),(y,fn(y)))
                self.line_draw((x,fn(x)),(y,fn(y)))

            def line_draw(self,a,b,colr='green'):
                if a[0]==b[0]:
                    if b[1]>a[1]:
                        y=np.arange(a[1],b[1],0.01)
                    else:
                        y=np.arange(b[1],a[1],0.01)

                    x=[a[0]]*y.size
                    plt.plot(x,y,color=colr)

                else:

                    y=lambda x:b[1]+(x-b[0])*((a[1]-b[1])/(a[0]-b[0]))
                    x=np.arange(a[0],b[0],0.0001)
                    plt.plot(x,y(x),color=colr)

            def TrapezoidalRule(self,a,b,n,fn):              #Method:1,function.1
                sol=fn(a)
                x=a
                y=a+(b-a)/n
                self.trap_create(x,y,fn)
                plt.plot(x,0,'bo')
                self.line_draw((x,0),(x,fn(x)),'b')
                for i in range(1,n):
                    x=a+(i*(b-a))/n
                    y=a+((i+1)*(b-a))/n
                    sol=sol+2*fn(a+(i*(b-a))/n)
                    self.trap_create(x,y,fn)
                    ##print "b-a:",b-a," second:",i*(b-a)/n
                self.line_draw((y,0),(y,fn(y)),'b')
                plt.plot(y,0,'bo')
                sol=sol+fn(b)
                sol=(sol*(b-a))/(2*n)
                                                              #We evalute the value needed.
                return sol                                #Now it's time to return this value.

            def SimpsonsRule(self,a,b,n,fn):                 #Method:2,function.2
                sol=fn(a)
                for i in range(1,n,2):
                    sol=sol+ 4*fn(a+(i*(b-a))/n)

                for i in range(2,n,2):
                    sol=sol+ 2*fn(a+(i*(b-a))/n)

                sol=sol+fn(b)
                sol=(sol*(b-a))/(3*n)                     #We evalute the value needed.
                return sol                                #Now it's time to return this value.

            def solve(self,a,b,n,fn,method):            #solve() function :that calls either of the two above functions according to the input method.

                if(method=='trapezoid'):
                    sol=self.TrapezoidalRule(a,b,n,fn)
                    x=np.arange(-10,10,0.01)
                    plt.plot(x,fn(x),color="red")

                    s="("+str(a)+","+str(0)+")"

                    if fn(a)>0 :
                        plt.annotate(s,xy=(a,0),xytext=(a,0-20))
                    else:
                        plt.annotate(s,xy=(a,0),xytext=(a,0+7))

                    s="("+str(b)+","+str(0)+")"

                    if fn(b)>0 :
                        plt.annotate(s,xy=(b,0),xytext=(b,0-20))
                    else:
                        plt.annotate(s,xy=(b,0),xytext=(b,0+7))


                    return sol
                if(method=='simpson'):
                    sol=self.SimpsonsRule(a,b,n,fn)

                    return sol



        f=lambda x:eval(s)
        mx=0
        mn=0
        x1=np.arange(listnum[1],listnum[2],0.1)
        for i in x1:
            if f(i)>mx:
                mx=f(i)
            if f(i)<mn:
                mn=f(i)
        print(mx)
        print(mn)
        plt.xlim(-11,11)
        plt.ylim(mn-6,mx+6)
        igr=Integrate()
        igr.line_draw((-11,0),(11,0),"black")
        igr.line_draw((0,-300),(0,300),"black")

        solution=igr.solve(listnum[1],listnum[2],int(listnum[3]),f,"trapezoid")
        print(solution)
        ##plt.annotate("$f(x) = 100.sin(x)$",xy=(6,250),xytext=(6,250))
        plt.annotate("$x-axis$",xy=(8,-20),xytext=(8,-20))
        plt.annotate("$y-axis$",xy=(-2,250),xytext=(-2,250))
        plt.annotate("$o$",xy=(-0.5,-15),xytext=(-0.5,-15))

        canvas = FigureCanvas(fig)
        output = StringIO.StringIO()
        canvas.print_png(output)
        response = make_response(output.getvalue())
        response.mimetype = 'image/png'
        return response

    else:
        return render_template('plot.html')

@app.route('/avg', methods=['GET', 'POST'])
def calc():
    rest = 0.0
    if request.method=='POST':
        first =request.form['first']
        exp=r"[0-9-/.]*"
        val=re.findall(exp,first)
        l = []
        for i in val:
            if i!='':
                l.append(float(i))
        print(sum(l))
        rest = ((sum(l)) / (len(l)))
        if sum(l)==0.0:
            rest="0.0"

    return render_template('avg.html', result=rest)

if __name__ == '__main__':
    app.run(debug=True)
