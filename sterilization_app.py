import logging
from collections import namedtuple


logger = logging.getLogger(__name__)
logging.basicConfig(filename= 'science_app_log.txt', level= logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s')



container = namedtuple('container',['name','max_volume','max_load'])

#initialize the max volume and max load for each container type
SJ = container('SJ',200,144)
MJ = container('MJ',600,120)
LJ = container('LJ',1500,88)
TT = container('TT',25,400)
Decon = container('Decon',1500,88)
DG = container('DG','NA','NA')
WG = container('WG','NA','NA')


possible_containers = (SJ,MJ,LJ,TT,DG,WG,Decon)


small_container = [x for x in range(1,601)] #if volume is 600mL or less it is a small container
large_container = [x for x in range(601,1501)] #if volume is 600-1500mL it is a large container

volume_to_time = {
                    'small': '30 minutes @ 121C',
                    'large': '45 minutes @ 121C'
                 }


goods_time = {
                    'DG': '10 minutes at 150C',
                    'WG': '20 minutes at 121C'
    }


#this fxn checks to see if user entered a valid container, max volume, and max load
def check_selection(userin):
    for container in possible_containers:
        if userin[0] == container.name: #check to see if entered container in possible_containers
            user_selection = container
            
    if userin[1] <= user_selection.max_volume and userin[2] <= user_selection.max_load:
        return True
    else:
        logger.warning('invalid volume or max load for container ' + str(userin[1]) + str(userin[2]))
        return False

    return False
        

#this fxn calls check_selection and if user input is valid, returns the correct sterilization method
def get_ster_info(userin): 
    if check_selection(userin):
        if userin[1] in small_container:
            return volume_to_time['small']
        elif userin[1] in large_container:
            return volume_to_time['large']
        else:
            return 'Incorrect volume, not between 1 and 1500'
    else:
        return 'Error with entered data, check log for more info'

#end declarations, begin user-side code    


print('Welcome to the sterilization verification checker')
username = input('Enter your username to begin: ')

logger.info('User: ' + username)

print('Welcome %s, here are the valid verification options: ' % username)

for container in possible_containers:
    print(container)
    

#while loop that runs program until user types 'exit'
loop_var = True
while loop_var:
    jar_or_cycle = input('Enter the jar or cycle you will be sterilizing or "exit" to exit: ')
    cycle = jar_or_cycle.upper()
    if jar_or_cycle == 'exit':
        break
    elif cycle in goods_time: #if the cycle entered is WG or DG, no need to ask for volumes or call fxns
        print('Sterilize ' + goods_time[cycle])
    else:
        volume = int(input('Enter the volume of liquid in the jar: '))
        num_containers = int(input('Enter the number of jars in the load: '))
        userin = (cycle, volume, num_containers)
        print(get_ster_info(userin))
        
    
      




