import numpy as np
from PIL import Image
import json
import pprint
import glob
import os
import sys

def convert_loop(images_dir, json_dir, output_dir):
    f = glob.glob(f'{json_dir}/*.json')
    
    for json_path in f:
        o_name = os.path.basename(json_path)
        output_path = f'{output_dir}/{o_name}'
        print(o_name)
        convert_segment_json_to_yolo(images_dir, json_path, output_path)

def convert_segment_json_to_yolo(images_dir, json_path, output_path):
    with open(json_path, 'r') as file:
        data = json.load(file)

    yolo_annotations = []
    # print(data)
    # for ann in data:
    #     print(ann)
    for n in range(len(data['tooth'])):
        ann = data['tooth'][n]
        id = ann["teeth_num"]
        category_id = ann["decayed"]
        img_path = os.path.basename(data['image_filepath'])
        
        width, height = Image.open(f'{images_dir}/{img_path}').size

        segments = []
        if "segmentation" in data['tooth'][n]:
            if len(ann['segmentation']) > 1:
                s = merge_multi_segment(ann['segmentation'])
                s = (np.concatenate(s, axis=0) / np.array([width, height])).reshape(-1).tolist()
            else:
                s = [j for i in ann['segmentation'] for j in i]  # all segments concatenated
                s = (np.array(s).reshape(-1, 2) / np.array([width, height])).reshape(-1).tolist()
            s = [category_id] + s

            # Check if the segment is not already in the list
            if s not in segments:
                segments.append(s)

        # Append YOLO formatted annotation to the list
        yolo_annotations.append({
            "teeth_num": id,
            "category_id": category_id,
            "width": width,
            "height": height,
            "segments": segments
        })

    # Save the YOLO formatted annotations to a new JSON file
    with open(output_path, 'w') as outfile:
        json.dump(yolo_annotations, outfile, indent=4)

def min_index(arr1, arr2):
    """Find a pair of indexes with the shortest distance.
    Args:
        arr1: (N, 2).
        arr2: (M, 2).
    Return:
        a pair of indexes(tuple).
    """
    dis = ((arr1[:, None, :] - arr2[None, :, :]) ** 2).sum(-1)
    return np.unravel_index(np.argmin(dis, axis=None), dis.shape)

def merge_multi_segment(segments):
    """Merge multi segments to one list.
    Find the coordinates with min distance between each segment,
    then connect these coordinates with one thin line to merge all
    segments into one.

    Args:
        segments(List(List)): original segmentations in coco's json file.
            like [segmentation1, segmentation2,...],
            each segmentation is a list of coordinates.
    """
    s = []
    segments = [np.array(i).reshape(-1, 2) for i in segments]
    idx_list = [[] for _ in range(len(segments))]

    # record the indexes with min distance between each segment
    for i in range(1, len(segments)):
        idx1, idx2 = min_index(segments[i - 1], segments[i])
        idx_list[i - 1].append(idx1)
        idx_list[i].append(idx2)

    # use two round to connect all the segments
    for k in range(2):
        # forward connection
        if k == 0:
            for i, idx in enumerate(idx_list):
                # middle segments have two indexes
                # reverse the index of middle segments
                if len(idx) == 2 and idx[0] > idx[1]:
                    idx = idx[::-1]
                    segments[i] = segments[i][::-1, :]

                segments[i] = np.roll(segments[i], -idx[0], axis=0)
                segments[i] = np.concatenate([segments[i], segments[i][:1]])
                # deal with the first segment and the last one
                if i in [0, len(idx_list) - 1]:
                    s.append(segments[i])
                else:
                    idx = [0, idx[1] - idx[0]]
                    s.append(segments[i][idx[0]:idx[1] + 1])

        else:
            for i in range(len(idx_list) - 1, -1, -1):
                if i not in [0, len(idx_list) - 1]:
                    idx = idx_list[i]
                    nidx = abs(idx[1] - idx[0])
                    s.append(segments[i][nidx:])
    return s

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python coco2yolo.py convert_loop /ttony0321/test/image /ttony0321/test/conv /ttony0321/test/yolo")
        sys.exit(1)

    function_name = sys.argv[1]
    images_dir = sys.argv[2]
    json_dir = sys.argv[3]
    output_dir = sys.argv[4]

    if function_name == "convert_loop":
        convert_loop(images_dir, json_dir, output_dir)
    else:
        print(f"Unknown function: {function_name}")
        
        #(images_dir, json_dir, output_dir)