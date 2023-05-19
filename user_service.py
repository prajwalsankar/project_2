from service_hadler import *
from pprint import pprint


args = sys.argv[1:]

if len(args) !=1 :
    print(f"In valid command line args: {args}")
    sys.exit(0)

cmd = args[0]

resp= run_command(cmd)
service_dict = get_proc_dict(resp)

pprint(service_dict)

print("------------------------------------------------")

# pid vs pname

d_pid_pname= {}

for k in service_dict:
    d_pid_pname[k] = service_dict[k][0]

pprint(d_pid_pname)





print("------------------------------------------------")

# pid vs pname

d_mem_pname= {}

for k in service_dict:
    d_pid_pname[k] = service_dict[k][1]

pprint(d_pid_pname)







