import __init__
import manage_DB
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

manage_DB.write_json("base_context", context)
