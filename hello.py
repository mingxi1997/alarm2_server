#!/usr/bin/python3
# coding: utf-8

from flask import Flask,request

app=Flask(__name__)

@app.route("/command",methods=['POST'])
def command():
    if request.form.get('key')=='19979476':
        
        with open('absence.txt','r')as f:
            absence=eval(f.read())
        absence[request.form.get('name')]='0'
        with open('absence.txt','w')as f:
            f.write(str(absence))
        
        
        with open('command.txt','r')as f:
            command=f.read()
        return command
    else:
        return 'illigal request'
        
  
    
@app.route("/alarm",methods=['POST'])
def alarm():
    if request.form.get('key')=='19979476':
        with open('alarm.txt','r')as f:
            alarm=eval(f.read())
        alarm[request.form.get('name')]=request.form.get('status')
        with open('alarm.txt','w')as f:
            f.write(str(alarm)) 
        
        return "Success"
    else:
        return 'illigal request'


@app.route("/affirm",methods=['POST'])
def affirm():
    if request.form.get('key')=='19979476':
        with open('affirm.txt','r')as f:
            affirm=eval(f.read())
        if request.form.get('affirm')=='1' or request.form.get('affirm')=='0':
            
            affirm[request.form.get('name')]=request.form.get('affirm')
            with open('affirm.txt','w')as f:
                f.write(str(affirm)) 
            
            return "Success"
        if request.form.get('affirm')=='?':
            return affirm[request.form.get('name')]
        if request.form.get('affirm')=='all0':
            for key in affirm:
                affirm[key]='0'
            with open('affirm.txt','w')as f:
                f.write(str(affirm)) 
            
       
        
        
    else:
        return 'illigal request'
    




@app.route("/leader",methods=['POST'])
def leader():
    if request.form.get('key')=='19979476':
        with open('command.txt','w')as f:
            f.write(str(request.form.get('content')))
        return "Success"

@app.route("/check",methods=['POST'])    
def check():
    if request.form.get('key')=='19979476' :
        with open('alarm.txt','r')as f:
            alarm=eval(f.read())
        with open('affirm.txt','r')as f:
            affirm=eval(f.read())
        with open('terse_absence.txt','r')as f:
            absence=f.read()
        situation={'alarm':alarm,'affirm':affirm,'absence':absence}
        return str(situation)


if __name__=='__main__':
    app.run()
