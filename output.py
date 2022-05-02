from docxtpl import DocxTemplate
import json
from database.static.mk_context import context

doc = DocxTemplate("./templates/resume_template_basic.docx")


def docx_output(context, output_name):
    doc.render(context)
    doc.save(f"{output_name}.docx")
