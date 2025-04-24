# 📁 Normalização, Compressão e Exportação de Fotos de Colaboradores (UVV)
Sorteador de fotos de colaboradores da UVV. usado para a seleção de fotos de perfil no sistema interno.

---

## ℹ️ Este script em Python automatiza o processamento de imagens de colaboradores:

- **Padroniza os nomes dos arquivos** no formato `Nome.Sobrenome`
- **Remove duplicatas** mantendo apenas o menor arquivo
- **Comprime** imagens maiores que 3.01MB
- **Exporta** os arquivos prontos para uma nova pasta

---

## 🔧 Pré-requisitos

- Python 3.8+
- Pillow (biblioteca de manipulação de imagens)

Instale com:

```bash
pip install pillow

# Se tiver tendo errors com PIP, instale temporariamente ignorando o check de certificado (não é seguro, porém funciona)
pip install pillow --trusted-host pypi.org --trusted-host files.pythonhosted.org
```

---

## ▶️ Como funciona
O script realiza as seguintes etapas:

1. **Limpeza do nome do arquivo**:
     - Remove sufixos como `- Foto 01`, números finais, e `(1)`
     - Exemplo: `WILLIAM CALVI - Foto 01.jpg` → `William.Calvi`
2. **Padronização da capitalização**
     - Capitaliza corretamente todos nomes.
3. **Filtro por tamanho**
     - Seleciona o menor arquivo entre cópias 
     - Exemplo: 
``` 
RENAN NETTO RODRIGUES 1.jpg - 4.88MB
RENAN NETTO RODRIGUES 2.jpg - 8.16MB
→ Mantém: Renan.Rodrigues - 4.88MB
```

4. **Compressão**
     - Se a imagem for maior que 3.01MB, ela será comprimida mantendo o nome original.
5. **Cópia final**
     - Os arquivos processados são copiados para `Fotos Colaboradores Prontas` com o nome padronizado.

---

## 📁 Estrutura

```
📁 Desktop
├── Fotos novas colaborador
│   ├── RENAN NETTO RODRIGUES 1.jpg
│   ├── RENAN NETTO RODRIGUES 2.jpg
│   ├── luiz.filho.jpg
│   ├── JEFERSON (1).jpg
│   └── WILLIAM CALVI - Foto 01.jpg
└── Fotos Colaboradores Prontas  ← (É criada quando o script é rodado)
```

## 🖥️ Exemplo de output

```cmd
⚠️ PARSE ERROR (LENGTH IS 1): Jeferson (1)
⚠️ PARSE ERROR (HAS DOT): luiz.filho
🔧 arquivo RENAN NETTO RODRIGUES 2.jpg comprimido para 2.91MB (quality=65)
Renan.Rodrigues - 2.91MB
✅ Renan.Rodrigues copiado para Renan.Rodrigues.jpg
Luiz.Filho - 1.22MB
✅ Luiz.Filho copiado para Luiz.Filho.jpg
```

## ✍️ Autor
Yuri Assaf – Estagiário de Desenvolvimento @ DTI UVV


