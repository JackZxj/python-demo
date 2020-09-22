import yaml
import os
import csv

file_path = os.path.abspath('yaml')
k8s_type = ['Deployment', 'Service']
service_list = {}


def has_nfs_in_volumes(dict):
    if 'volumes' in dict.keys():
        for volume in dict['volumes']:
            if 'nfs' in volume.keys():
                return str(True)
    return str(False)


def read_yaml(yaml_file):
    with open(yaml_file, 'r') as y:
        yaml_content = y.read()
    content = yaml.load(yaml_content, yaml.FullLoader)
    # print('\n', yaml_file)
    if 'kind' in content.keys():
        if content['kind'] == 'Deployment':
            new_key = content['metadata']['namespace'] + \
                '###' + content['metadata']['name']
            svc = service_list.get(new_key)
            if svc == None:
                svc = dict()
                svc['has_service'] = str(False)
                svc['service_type'] = ''
                svc['ports'] = ''
            svc['namespace'] = content['metadata']['namespace']
            svc['name'] = content['metadata']['name']
            svc['replicas'] = content['spec']['replicas']
            svc['image'] = ','.join(
                container['image'] for container in content['spec']['template']['spec']['containers'])
            svc['has_nfs'] = has_nfs_in_volumes(
                content['spec']['template']['spec'])
            service_list[new_key] = svc
        elif content['kind'] == "Service":
            new_key = content['metadata']['namespace'] + \
                '###' + content['metadata']['name']
            svc = service_list.get(new_key)
            if svc == None:
                svc = dict()
                svc['namespace'] = ''
                svc['name'] = ''
                svc['replicas'] = ''
                svc['image'] = ''
                svc['has_nfs'] = str(False)
            svc['has_service'] = str(True)
            svc['service_type'] = content['spec']['type']
            svc['ports'] = ','.join(str(port)
                                    for port in content['spec']['ports'])
            service_list[new_key] = svc


def read_yaml_from_dir(dir_path):
    for root, _, files in os.walk(dir_path):
        for file in files:
            if '.yaml' in file:
                read_yaml(os.path.join(root, file))
                # print(os.path.join(root, file))


if __name__ == "__main__":
    read_yaml_from_dir(file_path)
    # print(service_list)
    svc_list = []
    for value in service_list.values():
        svc_list.append(value)
    header = [i for i in svc_list[0].keys()]
    # print(service_list.values())
    # header = [i for i in [d.keys() for d in service_list.values()]]
    # header = [i for s in [d.keys() for d in service_list.values()] for i in s]
    # print(header)
    with open('res.csv', 'a') as output_file:
        dict_writer = csv.DictWriter(output_file, restval="-", fieldnames=header)
        dict_writer.writeheader()
        dict_writer.writerows(svc_list)
    print('OK!')