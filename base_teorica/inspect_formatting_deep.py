import os
from docx import Document
from docx.shared import Pt, Cm

def inspect_styles(path):
    if not os.path.exists(path):
        return

    doc = Document(path)
    print(f"--- Estilos do Documento: {os.path.basename(path)} ---")
    
    # Inspeciona estilos principais
    for style_name in ['Normal', 'Heading 1', 'Heading 2', 'Heading 3']:
        if style_name in doc.styles:
            s = doc.styles[style_name]
            font = s.font
            size = font.size.pt if font.size else "Default"
            name = font.name if font.name else "Inherit"
            bold = font.bold if font.bold is not None else "Inherit"
            print(f"Estilo '{style_name}': Font={name}, Size={size}, Bold={bold}")
            if hasattr(s, 'paragraph_format'):
                pf = s.paragraph_format
                align = pf.alignment if pf.alignment else "Default"
                space_after = pf.space_after.pt if pf.space_after else "Default"
                line_spacing = pf.line_spacing if pf.line_spacing else "Default"
                print(f"  Alignment={align}, SpaceAfter={space_after}, LineSpacing={line_spacing}")

    print("\n--- Conteúdo dos 40 primeiros parágrafos ---")
    for i, p in enumerate(doc.paragraphs[:40]):
        text = p.text.strip()
        if text:
            print(f"[{i:02}] ({p.style.name}): {text}")

if __name__ == "__main__":
    example_path = r'f:\projetos_opencode\PI2016Django\base_teorica\EXEMPLO - DRP04-Projeto_Integrador-Relatório Parcial.docx'
    inspect_styles(example_path)
