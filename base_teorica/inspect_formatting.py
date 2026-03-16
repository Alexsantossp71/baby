import os
from docx import Document

def inspect_docx(path):
    if not os.path.exists(path):
        print(f"Erro: {path} não encontrado.")
        return

    doc = Document(path)
    print(f"--- Inspeção: {os.path.basename(path)} ---")
    
    # Inspeciona seções (margens)
    for i, section in enumerate(doc.sections):
        print(f"Seção {i}: Margens (Top: {section.top_margin.cm:.2f}cm, Bottom: {section.bottom_margin.cm:.2f}cm, Left: {section.left_margin.cm:.2f}cm, Right: {section.right_margin.cm:.2f}cm)")

    # Inspeciona os primeiros 20 parágrafos para estilos e fontes
    print("\n--- Primeiros 20 Parágrafos (Conteúdo e Estilo) ---")
    for i, p in enumerate(doc.paragraphs[:20]):
        style_name = p.style.name
        text = p.text[:50].replace('\n', ' ')
        bold = any(run.bold for run in p.runs)
        font_size = None
        font_name = None
        if p.runs:
            font_size = p.runs[0].font.size
            font_name = p.runs[0].font.name
        
        size_str = f"{font_size.pt}pt" if font_size else "Default"
        print(f"P{i:02} [{style_name}] (Font: {font_name}, Size: {size_str}, Bold: {bold}): {text}...")

if __name__ == "__main__":
    example_path = r'f:\projetos_opencode\PI2016Django\base_teorica\EXEMPLO - DRP04-Projeto_Integrador-Relatório Parcial.docx'
    inspect_docx(example_path)
