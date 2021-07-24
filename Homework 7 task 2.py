import os
import yaml

with open('config.yaml') as f:
    templates = yaml.safe_load(f)
directory = os.getcwd()

for i in templates:
    if type(i) == dict:
        super_key = i.keys()
        os.makedirs(*super_key, exist_ok=True)
        for key, content in i.items():
            os.chdir(*super_key)
            for x in content:
                if type(x) == str:
                    with open(x, 'a') as f:
                        f.write("start")
                elif type(x) == dict:
                    super_key_content = x.keys()
                    os.makedirs(*super_key_content, exist_ok=True)
                    for key_x, content_x in x.items():
                        os.chdir(*super_key_content)
                        if type(content_x) == list:
                            for y in content_x:
                                if type(y) == str:
                                    with open(y, 'a') as f:
                                        print(y)
                        elif type(content_x) == dict:
                            for key_z, content_z in content_x.items():
                                super_key_content_z = content_x.keys()
                                os.makedirs(*super_key_content_z, exist_ok=True)
                                os.chdir(*super_key_content_z)
                                for z in content_z:
                                    with open(z, 'a') as f:
                                        f.write("start")
    os.chdir(directory)