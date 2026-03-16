from docx import Document
import os

def compare_covers(example_path, v4_path):
    def get_cover_lines(path):
        if not os.path.exists(path): return []
        doc = Document(path)
        lines = []
        for p in doc.paragraphs:
            if p.text.strip():
                lines.append(p.text.strip())
            if p.text.find('\f') != -1 or 'page_break' in str(p._element.xml):
                break
        return lines

    example_lines = get_cover_lines(example_path)
    v4_lines = get_cover_lines(v4_path)
    
    print("--- CAPA EXEMPLO (UNIVESP) ---")
    for l in example_lines: print(f"| {l}")
    print("\n--- SUA CAPA ATUAL (V4) ---")
    for l in v4_lines: print(f"| {l}")

if __name__ == "__main__":
    example = r'f:\projetos_opencode\PI2016Django\base_teorica\EXEMPLO - DRP04-Projeto_Integrador-Relatório Parcial.docx'
    v4 = r'f:\projetos_opencode\PI2016Django\base_teorica\Relatorio_Parcial_Permutas_Baby_V4_ABNT_Final.docx'
    compare_covers(example, v4)
