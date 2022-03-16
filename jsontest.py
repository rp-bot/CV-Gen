import json
context = {
    'name': "Full Name",
    'position': "SDE",
    'location': "somewhere",
    'email_address': "Email",
    'linkedin_username': "Linkedin Username",
    'github_username': "GitHub Username",
    'introduction': "Introduce yourself: I am a computer science major expecting to graduate...",
    'educations': [
        {
            "major": "first something",
            "grad_date": "2020",
            "school_name": "some school",
            "school_loc": "somewhere",
            "gpa": 5,
        },
        {
            "major": "second something",
            "grad_date": "2022",
            "school_name": "some other school",
            "school_loc": "somewhere else",
            "gpa": 4
        },
    ],
    'work_experiences': [
        {
            "title": "Software Developer Intern",
            "start_end": "2022-present",
            "org_name": "something inc",
            "description": [
                "we did this and that",
                "and then we did something else"
            ],
        }
    ]
}
# with open('newdataset.json', "r") as f:
#     data = json.load(f)
#     print(data["name"])

with open('base_context.json', "w") as f:
    json.dump(context, f, indent=4)
