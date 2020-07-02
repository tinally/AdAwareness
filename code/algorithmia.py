import os
from Algorithmia.acl import ReadAcl, AclType
from Algorithmia import client


def create_data_collection(api_client, username, data_path):
    dirname = os.path.basename(data_path)
    collection_path = f"data://{username}/{dirname}"
    print(collection_path)
    directory = api_client.dir(collection_path)
    if not directory.exists():
        directory.create()
    acl = directory.get_permissions()
    if acl.read_acl == AclType.my_algos:
        directory.update_permissions(ReadAcl.private)

    assert directory.get_permissions().read_acl == AclType.private

    local_files = os.listdir(data_path)
    host_files = []
    for i, filepath in enumerate(local_files):
        file = f"{collection_path}/{os.path.basename(filepath)}"
        if not api_client.file(file).exists():
            api_client.file(file).putFile(filepath)
            host_files.append(file)
    return collection_path, host_files


def call(algo, input_files):
    result = {}
    for path in input_files:
        try:
            algo.set_options(timeout=300)
            result[os.path.basename(path)] = algo.pipe(path).result
            print(path, algo.pipe(path).result)
        except Exception as error:
            print(error)
    return result


if __name__ == '__main__':
    api_key = 'sfw/NudityDetectioni2v/0.2.13'
    api_client = client(api_key)

    # Instanciate our algorithm
    nudd_algo = api_client.algo('sfw/NudityDetectioni2v/0.2.13')
    tagg_algo = api_client.algo('deeplearning/IllustrationTagger/0.4.0')



