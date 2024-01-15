import json
import os
import sys
import glob

def find_error(dir):
    file_list = glob.glob(f'{dir}/*.json')
    error_list = []
    for f in file_list:
        f_name = os.path.basename(f)[:-5]
        with open(f, 'r') as f:
            data=json.load(f)
            img_name = os.path.basename(data['image_filepath'])[:-4]
            if f_name != img_name:
                error_list.append(f_name)
            else:
                pass
            
    print(error_list)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python checking.py find_error /ttony0321/Dataset/train_data/json")
        sys.exit(1)

    function_name = sys.argv[1]
    path = sys.argv[2]

    if function_name == "find_error":
        find_error(path)
    else:
        print(f"Unknown function: {function_name}")