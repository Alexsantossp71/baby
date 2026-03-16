from docx import Document
import os

def inspect_cover(path):
    if not os.path.exists(path):
        print("File not found")
        return
    
    doc = Document(path)
    print(f"--- Cover Inspection for {os.path.basename(path)} ---")
    
    for i, p in enumerate(doc.paragraphs[:100]):
        text = p.text.strip()
        if text:
            align = p.paragraph_format.alignment
            run = p.runs[0] if p.runs else None
            bold = run.bold if run else False
            font_size = run.font.size.pt if run and run.font.size else "N/A"
            print(f"P{i:02}: [Align:{align}] [Bold:{bold}] [Size:{font_size}] -> {text}")
        
if __name__ == "__main__":
    example = r'f:\projetos_opencode\PI2016Django\base_teorica\EXEMPLO - DRP04-Projeto_Integrador-Relatório Parcial.docx'
    inspect_cover(example)
