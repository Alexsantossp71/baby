import os
import shutil
from django.core.management.base import BaseCommand
from baby.models import Produto

class Command(BaseCommand):
    help = 'Atualiza as imagens dos produtos com imagens realistas geradas por AI'

    def handle(self, *args, **options):
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

        r_w = ['ROUPA', 'VESTIDO', 'PIJAMA', 'BODY', 'CALÇA', 'SAIA', 'CAMISETA', 'JAQUETA', 'MACACÃO']
        b_w = ['BRINQUEDO', 'BONECO', 'BOLA', 'TAPETE MUSICAL', 'PARQUE', 'PIANO', 'TRICICLO', 'BLOCO', 'BONECA', 'CARRINHO', 'PELÚCIA', 'EDUCO']
        m_w = ['CÔMODA', 'ESTANTE', 'GUARDA ROUPA', 'POLTRONA', 'BERÇO', 'CRIADO', 'MOVEIL', 'MÓVEIS']
        a_w = ['ALIMENTAÇÃO', 'GARRAFA', 'LANCHEIRA', 'COPO', 'BANQUETA']
        ac_w = ['MOCHILA', 'BOLSA', 'BOX', 'LUVA', 'ÓCULOS', 'CHAPEU', 'ACESSÓRIOS']
        h_w = ['LAÇO', 'TIARA', 'PRESILHA']

        produtos = Produto.objects.all()
        count = 0

        for p in produtos:
            titulo = p.titulo.upper()
            target_img = image_map['ROUPA'] # Default
            
            if any(w in titulo for w in r_w): target_img = image_map['ROUPA']
            elif any(w in titulo for w in b_w): target_img = image_map['BRINQUEDO']
            elif any(w in titulo for w in m_w): target_img = image_map['MOVEIS']
            elif any(w in titulo for w in a_w): target_img = image_map['ALIMENTACAO']
            elif any(w in titulo for w in ac_w): target_img = image_map['ACESSORIO']
            elif any(w in titulo for w in h_w): target_img = image_map['HAIR']

            src = os.path.join(brain_dir, target_img)
            if os.path.exists(src):
                new_filename = f"real_{target_img}"
                dest = os.path.join(media_root, new_filename)
                
                # Certificar que o diretório existe
                os.makedirs(media_root, exist_ok=True)
                
                shutil.copy(src, dest)
                p.imagem_principal = f"produtos/{new_filename}"
                p.save()
                count += 1
                self.stdout.write(self.style.SUCCESS(f"Updated: {p.titulo} -> {new_filename}"))
            else:
                self.stdout.write(self.style.WARNING(f"File not found: {src}"))

        self.stdout.write(self.style.SUCCESS(f"Total atualizado: {count}"))
