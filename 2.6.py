
import yaml
my_dict = yaml.load(open('C:\\Users\\dyava\\Desktop\\ipl_match.yaml'))
rt=my_dict["innings"][1]["2nd innings"]["deliveries"]
run=0
for x in rt:
    for k,v in x.items():
        for p,q in v.items():
            if p =="wicket":
                for u,v in q.items():
                    if u=="kind" and v=="bowled":
                        print(q.values())
            
        
        

