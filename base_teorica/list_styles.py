from docx import Document

def list_styles(docx_path):
    doc = Document(docx_path)
    print("Available Styles:")
    for s in doc.styles:
        print(f"Name: {s.name}, Type: {s.type}")

if __name__ == "__main__":
    t = r'f:\projetos_opencode\PI2016Django\base_teorica\Modelo_-_Relatorio_Parcial_oficial.docx'
    list_styles(t)
