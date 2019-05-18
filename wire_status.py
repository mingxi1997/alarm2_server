
import time


units_order=['发射一营','发射二营','发射三营','发射四营','发射五营','发射六营','技术一营','技术二营','作战保障营','阵管防卫连','营区大门岗','家属院门岗','油库','机关楼','装备场区','共同训练场']






def initialize(file_name,content):
    init={}
    for unit in units_order:
        init[unit]=content
    with open(file_name,'w')as f:
        f.write(str(init))




def get_wire_status():
    with open('absence.txt','r')as f:
        absence=eval(f.read())
    wire_status=''     
    for unit in units_order:
        wire_status+=absence[unit]
    return wire_status

def fill_wire_status():
    with open('absence.txt','r')as f:
        absence=eval(f.read())
    for key in absence:
        absence[key]='1'
    with open('absence.txt','w')as f:
        f.write(str(absence))
    
def save_wire_status(status):
    with open('terse_absence.txt','w')as f:
        f.write(status)
           
initialize('absence.txt','1')
initialize('affirm.txt','0')    
initialize('alarm.txt','0000')


while True:
    try:
        fill_wire_status()
        time.sleep(4)
        wire_status=get_wire_status()
        save_wire_status(wire_status)
        if int(wire_status)>0:
            pass
    except:
        time.sleep(3)
    
    
    