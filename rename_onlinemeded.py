import os
import requests
base_url = 'https://onlinemeded.org/api/v1/spa/categories/'
topics = [{'name': 'Cardiology', 'slug': 'cardiology', 'url': '/spa/cardiology', 'subitems': []}, {'name': 'Pulmonology', 'slug': 'pulmonology', 'url': '/spa/pulmonology', 'subitems': []}, {'name': 'Gastroenterology', 'slug': 'gastroenterology', 'url': '/spa/gastroenterology', 'subitems': []}, {'name': 'Nephrology', 'slug': 'nephrology', 'url': '/spa/nephrology', 'subitems': []}, {'name': 'Hematology Oncology', 'slug': 'hematology-oncology', 'url': '/spa/hematology-oncology', 'subitems': []}, {'name': 'Infectious Disease', 'slug': 'infectious-disease', 'url': '/spa/infectious-disease', 'subitems': []}, {'name': 'Endocrine', 'slug': 'endocrine', 'url': '/spa/endocrine', 'subitems': []}, {'name': 'Neurology', 'slug': 'neurology', 'url': '/spa/neurology', 'subitems': []}, {'name': 'Rheumatology', 'slug': 'rheumatology', 'url': '/spa/rheumatology', 'subitems': []}, {'name': 'Dermatology', 'slug': 'dermatology', 'url': '/spa/dermatology', 'subitems': []}, {'name': 'Pediatrics', 'slug': 'pediatrics', 'url': '/spa/pediatrics', 'subitems': []}, {'name': 'Psychiatry', 'slug': 'psychiatry', 'url': '/spa/psychiatry', 'subitems': []}, {'name': 'OBGYN', 'slug': 'obgyn', 'url': '/spa/obgyn', 'subitems': [{'name': 'Gynecology', 'slug': 'gynecology', 'url': '/spa/gynecology', 'subitems': []}, {'name': 'Obstetrics', 'slug': 'obstetrics', 'url': '/spa/obstetrics', 'subitems': []}]}, {'name': 'Surgery', 'slug': 'surgery', 'url': '/spa/surgery', 'subitems': [{'name': 'Surgery: General', 'slug': 'surgery-general', 'url': '/spa/surgery-general', 'subitems': []}, {'name': 'Surgery: Subspecialty', 'slug': 'surgery-subspecialty', 'url': '/spa/surgery-subspecialty', 'subitems': []}, {'name': 'Surgery: Trauma', 'slug': 'surgery-trauma', 'url': '/spa/surgery-trauma', 'subitems': []}]}, {'name': 'Epidemiology and Stats', 'slug': 'epidemiology-and-stats', 'url': '/spa/epidemiology-and-stats', 'subitems': []}, {'name': 'OMM', 'slug': 'omm', 'url': '/spa/omm', 'subitems': []}, {'name': 'Primer: Methods for Success', 'slug': 'methods-for-success', 'url': '/methods-for-success', 'subitems': []}, {'name': 'Next Level: Intern Content', 'slug': 'intern-content', 'url': '/spa/intern-content', 'subitems': []}]
videos_path = r'C:\Users\moshe\PycharmProjects\OnlineMeded\Videos'


def rename_folder(slug, category):
    old_cat = None

    if category in ['Gynecology', 'Obstetrics']:
        old_cat = 'OBGYN'
    elif category in ["Surgery - General", "Surgery - Subspecialty", "Surgery - Trauma"]:
        old_cat = 'Surgery'

    if not os.path.exists(os.path.join(videos_path, category)):
        os.makedirs(os.path.join(videos_path, category))

    print('Working on ', base_url + slug, 'category: ', category)
    lessons = requests.get(base_url + slug).json()['category']['lessons']
    for i, lesson in enumerate(lessons):
        orig_name = os.path.join(videos_path, old_cat if old_cat else category, f"{lesson['id']}. {lesson['name'].replace(':', ' -').replace('/', '-')}.mp4")
        new_name = os.path.join(videos_path, category, f"{i+1}. {lesson['name'].replace(':', ' -').replace('/', '-')}.mp4")
        os.rename(orig_name, new_name)


for topic in topics:
    if len(topic['subitems']) > 0:
        for item in topic['subitems']:
            rename_folder(item['slug'], item['name'].replace(':', ' -'))
    else:
        rename_folder(topic['slug'], topic['name'].replace(':', ' -'))

#
# for topic in topics:
#     category = topic['slug']
#     new_category_name = topic['name']
#
#     os.makedirs(os.path.join(videos_path, new_category_name), exist_ok=True)
#
#     lessons = requests.get(base_url + category).json()['category']['lessons']
#     for lesson in lessons:
#         orig_name = os.path.join(videos_path, category, lesson['slug'] + '.mp4')
#         new_name = os.path.join(videos_path, new_category_name, f"{lesson['id']}. {lesson['name']}.mp4")
#         os.rename(orig_name, new_name)
