import json


def transform_json_to_py(json_file):
    file_name = json_file.split('.')[0]
    with open(json_file, 'r') as f:
        json_data = json.load(f)
    with open(file_name + '.py', 'w') as f:
        f.write(f'{file_name.split("/")[-1]} = ' + str(json_data))

if __name__ == '__main__':
    transform_json_to_py('data/tarif_kinesitherapeute.json')
    transform_json_to_py('data/therapists_data.json')
    transform_json_to_py('data/therapists.json')
