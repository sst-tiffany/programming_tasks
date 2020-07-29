from pathlib import Path


def dir_siblings(directory):
    return [(p, [p_sib for p_sib in sorted(Path(directory).rglob("*/")) if p_sib != p and
                 len(str(p).split('/')) == len(str(p_sib).split('/')) and
                 str(p).split('/')[:-1] == str(p_sib).split('/')[:-1]])
            for p in sorted(Path(directory).rglob("*/"))]


path_to_A = '/Users/t.kuzenko/'
path_A = f'{path_to_A}A/'
dir_siblings(path_A)
