import json
context = {
    'name': "",
    'position': "",
    'location': "",
    'email_address': "",
    'linkedin_username': "",
    'github_username': "",
    'introduction': "",
    'relevant_skills': [
    ],
    'relevant_courses': [
    ],
    'educations': [
    ],
    'work_experiences': [
    ]
}
# with open('newdataset.json', "r") as f:
#     data = json.load(f)
#     print(data["name"])

with open('base_context.json', "w") as f:
    json.dump(context, f, indent=4)
