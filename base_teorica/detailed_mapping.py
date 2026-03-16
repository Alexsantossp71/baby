from docx import Document
import os

def detailed_mapping(path):
    if not os.path.exists(path):
        return
    
    doc = Document(path)
    print(f"--- Detailed Mapping: {os.path.basename(path)} ---")
    
    for i, p in enumerate(doc.paragraphs):
        text = p.text.strip()
        if text:
            # Show style and text to better understand how to replace while keeping formatting
            print(f"P{i:03} [Style: {p.style.name}]: {text[:100]}")

if __name__ == "__main__":
    template_path = r'f:\projetos_opencode\PI2016Django\base_teorica\Modelo_-_Relatorio_Parcial_oficial.docx'
    detailed_mapping(template_path)
