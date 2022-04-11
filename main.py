# %%
from docxtpl import DocxTemplate
import json

# %%
doc = DocxTemplate("./templates/resume_template_basic.docx")
with open('base_context.json', "r") as f:
    context = json.load(f)

# %%
doc.render(context)
doc.save("generated_doc.docx")

# FIXME
