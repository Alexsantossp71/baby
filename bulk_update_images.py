import os
import shutil
import uuid
from baby.models import Produto

def bulk_update_images():
    # Caminho do projeto e pasta media
    media_root = r'f:\projetos_opencode\PI2016Django\media\produtos'
    brain_dir = r'C:\Users\arpt1\.gemini\antigravity\brain\593d38a4-505d-4ccc-84b9-6da90c41da3a'
    
    # Mapeamento de Imagens Geradas
    image_map = {
        'ROUPA': 'baby_clothing_boy_1773676328266.png',
        'BRINQUEDO': 'baby_toys_blocks_1773676343766.png',
        'MOVEIS': 'baby_nursery_crib_1773676358879.png',
        'ALIMENTACAO': 'baby_high_chair_1773676375527.png',
        'ACESSORIO': 'baby_diaper_bag_v3_1773676438759.png',
        'HAIR': 'baby_hair_bows_v2_1773676415962.png'
    }
    
    # Lista de produtos (obtida anteriormente)
    # Categorização baseada em palavras-chave no título
    
    produtos = Produto.objects.all()
    count = 0
    
    for p in produtos:
        titulo = p.titulo.upper()
        target_img = 'baby_clothing_boy_1773676328266.png' # Default
        
        if any(w in titulo for w in ['ROUPA', 'VESTIDO', 'PIJAMA', 'BODY', 'CALÇA', 'SAIA', 'CAMISETA', 'JAQUETA', 'MACACÃO']):
            target_img = image_map['ROUPA']
        elif any(w in titulo for w in ['BRINQUEDO', 'BONECO', 'BOLA', 'TAPETE MUSICAL', 'PARQUE', 'PIANO', 'TRICICLO', 'BLOCO', 'BONECA', 'CARRINHO', 'PELÚCIA', 'EDUCO']):
            target_img = image_map['BRINQUEDO']
        elif any(w in titulo for w in ['CÔMODA', 'ESTANTE', 'GUARDA ROUPA', 'POLTRONA', 'BERÇO', 'CRIADO', 'MOVEIL', 'MÓVEIS']):
            target_img = image_map['MOVEIS']
        elif any(w in titulo for w in ['ALIMENTAÇÃO', 'GARRAFA', 'LANCHEIRA', 'COPO', 'BANQUETA']):
            target_img = image_map['ALIMENTACAO']
        elif any(w in titulo for w in ['MOCHILA', 'BOLSA', 'BOX', 'LUVA', 'ÓCULOS', 'CHAPEU', 'ACESSÓRIOS']):
            target_img = image_map['ACESSORIO']
        elif any(w in titulo for w in ['LAÇO', 'TIARA', 'PRESILHA']):
            target_img = image_map['HAIR']

        # Copiar arquivo para a pasta media do Django
        src = os.path.join(brain_dir, target_img)
        if os.path.exists(src):
            # Gerar nome único para evitar colisões no Django
            new_filename = f"real_{target_img}"
            dest = os.path.join(media_root, new_filename)
            shutil.copy(src, dest)
            
            p.imagem_principal = f"produtos/{new_filename}"
            p.save()
            count += 1
            print(f"Updated: {p.titulo} -> {new_filename}")
        else:
            print(f"Skipped (Not Found): {src}")

    print(f"Total updated: {count}")

if __name__ == "__main__":
    bulk_update_images()
