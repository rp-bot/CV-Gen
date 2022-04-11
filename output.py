from docxtpl import DocxTemplate
import json

doc = DocxTemplate("./templates/resume_template_basic.docx")


def docx_output(context, output_name):
    doc.render(context)
    doc.save(f"{output_name}.docx")
