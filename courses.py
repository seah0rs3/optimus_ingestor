EDX_DATABASES = {
    'default': {'dbname': 'api', 'mongoname': 'course-v1:AdelaideX+AddictionX+3T2015', 'icon': 'fa-settings'},
    'personcourse': {'dbname': 'Person_Course', 'icon': 'fa-settings'},
    'Course_Event': {'dbname': 'Course_Event', 'icon': 'fa-settings', 'year': ''},
    'AddictionX_3T2015': {'dbname': 'AdelaideX_AddictionX_3T2015', 'mongoname': 'course-v1:AdelaideX+AddictionX+3T2015', 'discussiontable': 'AdelaideX-AddictionX-3T2015-prod', 'icon': 'fa-tree', 'year': '2015'},
    'Code101x_2T2015': {'dbname': 'AdelaideX_Code101x_2T2015', 'mongoname': 'course-v1:AdelaideX+Code101x+2T2015', 'discussiontable': 'AdelaideX-Code101x-2T2015-prod', 'icon': 'fa-heart', 'year': '2015'},
    'Code101x_3T2015': {'dbname': 'AdelaideX_Code101x_3T2015', 'mongoname': 'course-v1:AdelaideX+Code101x+3T2015', 'discussiontable': 'AdelaideX-Code101x-3T2015-prod', 'icon': 'fa-plane', 'year': '2015'},
    'Cyber101x_2T2015': {'dbname': 'AdelaideX_Cyber101x_2T2015', 'mongoname': 'course-v1:AdelaideX+Cyber101x+2T2015', 'discussiontable': 'AdelaideX-Cyber101x-2T2015-prod', 'icon': 'fa-plane', 'year': '2015'},
    'Entrep101X_1T2016': {'dbname': 'AdelaideX_Entrep101X_1T2016', 'mongoname': 'course-v1:AdelaideX+Entrep101X+1T2016', 'discussiontable': 'AdelaideX-Entrep101X-1T2016-prod', 'icon': 'fa-plane', 'year': '2016'},
    'HumBio101x_1T2015': {'dbname': 'AdelaideX_HumBio101x_1T2015', 'mongoname': 'AdelaideX/HumBio101x/1T2015', 'discussiontable': 'AdelaideX-HumBio101x-1T2015-prod', 'icon': 'fa-plane', 'year': '2015'},
    'HumBio101x_2T2015': {'dbname': 'AdelaideX_HumBio101x_2T2015', 'mongoname': 'course-v1:AdelaideX+HumBio101x+2T2015', 'discussiontable': 'AdelaideX-HumBio101x-2T2015-prod', 'icon': 'fa-plane', 'year': '2015'},
    'Lang101x_2T2015': {'dbname': 'AdelaideX_Lang101x_2T2015', 'mongoname': 'course-v1:AdelaideX+Lang101x+2T2015', 'discussiontable': 'AdelaideX-Lang101x-2T2015-prod', 'icon': 'fa-plane', 'year': '2015'},
    'MusonicX_3T2015': {'dbname': 'AdelaideX_MusonicX_3T2015', 'mongoname': 'course-v1:AdelaideX+Cyber101x+2T2015', 'discussiontable': 'AdelaideX-MusonicX-3T2015-prod', 'icon': 'fa-plane', 'year': '2015'},
    'Project101x_1T2016': {'dbname': 'AdelaideX_Project101x_1T2016', 'mongoname': 'course-v1:AdelaideX+Project101x+1T2016', 'discussiontable': 'AdelaideX-Project101x-1T2016-prod', 'icon': 'fa-plane', 'year': '2016'},
    'Wine101x_2T2015': {'dbname': 'AdelaideX_Wine101x_2T2015', 'mongoname': 'course-v1:AdelaideX+Wine101x+2T2015', 'discussiontable': 'AdelaideX-Wine101x-2T2015-prod', 'icon': 'fa-plane', 'year': '2015'},
    'Wine101x_2T2015_2': {'dbname': 'AdelaideX_Wine101x_2T2015_2', 'mongoname': 'course-v1:AdelaideX+Wine101x+2T2015.2', 'discussiontable': 'AdelaideX-Wine101x-2T2015-2-prod', 'icon': 'fa-plane', 'year': '2015'},
}

for DB in EDX_DATABASES:
    EDX_DATABASES[DB]['id'] = DB
