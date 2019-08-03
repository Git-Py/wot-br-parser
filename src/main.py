import pickle,\
       pprint,\
       os,\
       zlib,\
       importlib

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, 'sample_data\\wot-ver-1.dat'), 'rb') as file:

    data = pickle.load(file, encoding='bytes')

    version, battle_result = data
    id, personal_result, full_personal_result, team_result = battle_result

    pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(len(zlib.decompress(full_personal_result)))
    # pp.pprint(full_personal_result)

    personal_result = pickle.loads(zlib.decompress(personal_result), encoding='latin1')
    full_personal_result = pickle.loads(zlib.decompress(full_personal_result), encoding='latin1')
    team_result = pickle.loads(zlib.decompress(team_result), encoding='latin1')

    # battle_results_data = importlib.import_module('battle_results_shared_17')

    pp.pprint(personal_result)
    # pp.pprint(full_personal_result)
    # pp.pprint(team_result)

    # personal_results = battle_results_data.AVATAR_FULL_RESULTS.unpack(personal_result)
