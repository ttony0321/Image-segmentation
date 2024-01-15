import os
import json
import glob
import sys
def json2txt(path):
    label_list = glob.glob(f'{path}/*.json')
    for label in label_list:
        name = os.path.basename(label)[:-5]
        with open(label, 'r') as js:
            data = json.load(js)
        with open(f'{path}/y{name}.txt', 'w') as f:
            for d in range(len(data)):
                if data[0]['segments'][0][0] == True:
                    id = 1
                else:
                    id = 0
                seg = data[0]['segments'][0][1:]
                formatted_string = ' '.join(map(str, seg))

                # f.write(f'{id} '.join(f.strip(), id))
                # f.write(f'{formatted_string}\n')
                f.write(f'{id} ')
                f.write(f'{formatted_string}\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python totxt.py json2txt /ttony0321/test/yolo")
        sys.exit(1)

    function_name = sys.argv[1]
    path = sys.argv[2]

    if function_name == "json2txt":
        json2txt(path)
    else:
        print(f"Unknown function: {function_name}")