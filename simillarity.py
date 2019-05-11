from pre_processing import DataProcessing
import sys


def all_values(ref_id):
    obj = DataProcessing()
    types = obj.anime_type()
    qt_ep = obj.ep()
    grades = obj.grades()
    num_members = obj.members()
    gender = obj.normalize_gender()


try:
    id_video = sys.argv[1]
    all_values(id_video)
except:
    print("Argumento inválido para começar a playlist")
    exit(404)