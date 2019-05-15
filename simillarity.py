from pre_processing import DataProcessing
import sys


def all_values(ref_id):
    obj = DataProcessing()
    type_animes = obj.anime_type()
    qt_ep = obj.ep()
    grades = obj.grades()
    print(grades)
    # num_members = obj.members().copy()
    # gender = obj.normalize_gender().copy()


if __name__ == '__main__':
    try:
        id_video = sys.argv[1]
        all_values(id_video)
    except:
        print("Argumento inválido para começar a playlist")
        exit(404)
