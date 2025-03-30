log_list =[]


file=open('./mission_computer_main.log', 'r')

        
for line in file:
            parts = line.strip().split(",")
         

            if len(parts) >= 3:
                timestamp = parts[0].strip()
                log_type = parts[1].strip()
                message = ",".join(parts[2:]).strip()
         
                log_list.append([timestamp, log_type, message])
                
print(log_list) 
                
                
log_list.sort(reverse=True)
    
for l in log_list:
        print(l)

log_dic = {log[0]: {"log_type": log[1], "message": log[2]} for log in log_list}
    
print(log_dic)
    
file_2= open('mission_computer_main.json', 'w') 
json_dump= '{\n'
for key, value in log_dic.items(): 
        json_dump +='    "'+ key + '": {\n' 
        json_dump +='    "log_type": "'+ value['log_type'] + '", \n'
        json_dump +='    "message": "'+ value['message'] + '"\n'
        json_dump +='    },\n'


json_dump = json_dump.strip(',\n') +'\n}'

file_2.write(json_dump) 


file.close()
file_2.close()
    
    
  
    
    
                

