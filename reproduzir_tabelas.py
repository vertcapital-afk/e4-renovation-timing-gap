# -*- coding: utf-8 -*-
"""Regenera as tabelas do artigo a partir dos JSON de resultados.
Sem dependencias externas: json e stdlib bastam.
Uso:  python reproduzir_tabelas.py   (os JSON podem estar na mesma pasta,
em ./resultados/ ou em ../resultados/ - o script encontra-os)
"""
import json
import os

_AQUI = os.path.dirname(os.path.abspath(__file__))
_CANDIDATOS = [_AQUI, os.path.join(_AQUI, 'resultados'),
               os.path.join(_AQUI, '..', 'resultados')]
R = next(p for p in _CANDIDATOS
         if os.path.exists(os.path.join(p, 'opcoes_categoria.json')))
cat = json.load(open(os.path.join(R, 'opcoes_categoria.json'), encoding='utf-8'))
pac = json.load(open(os.path.join(R, 'opcoes_pacote.json'), encoding='utf-8'))


def central(v):
    return (v.get('lambda_modo') == 'uniforme' and v.get('c1') == 'central'
            and v.get('c2') == 'central' and v.get('processo') == 'OU'
            and 'f2_cenario' not in v and 'taxa_desconto' not in v)


print('=== Tabela 4.1 - premios de opcao por categoria (EUR/m2, cenario central) ===')
for rb in ('RB1', 'RB6', 'RB8'):
    linha = {v['categoria']: v['valor_opcao'] for v in cat.values()
             if central(v) and v['rb'] == rb}
    print(rb, {k: round(x, 1) for k, x in sorted(linha.items())})

print('\n=== Tabela 4.2 - valor do pacote por epoca x tipologia (media 3 cidades) ===')
EPOCAS = {'<1960': ('RB1', 'RB5'), '1961-90': ('RB2', 'RB6'),
          '1991-05': ('RB3', 'RB7'), '2006-15': ('RB4', 'RB8')}
CIDADES = ('Coimbra', 'Bragan\u00e7a', '\u00c9vora')

def media_pacote(rb, suf=''):
    return sum(pac[f'{rb}|{c}' + suf]['valor_opcao'] for c in CIDADES) / 3

for ep, (sfh, mfh) in EPOCAS.items():
    print(f'{ep:9} SFH={media_pacote(sfh):7.1f}  MFH={media_pacote(mfh):7.1f}')

print('\n=== Tabela 4.4 - F2 fotovoltaico (cenario central) ===')
for rb in ('RB1', 'RB6', 'RB8'):
    base = next(v['valor_opcao'] for v in cat.values()
                if central(v) and v['rb'] == rb and v['categoria'] == 'stpv')
    f2 = {v['f2_cenario']: v['valor_opcao'] for v in cat.values()
          if v.get('f2_cenario', '').startswith('f2_') and 'hp' not in v.get('f2_cenario', '')
          and v['rb'] == rb and v['categoria'] == 'stpv'
          and v.get('lambda_modo') == 'uniforme' and v.get('c1') == 'central'
          and v.get('c2') == 'central' and v.get('processo') == 'OU'}
    print(rb, f'sem F2={base:.1f}', {k: round(x, 1) for k, x in sorted(f2.items())})

print('\n=== 4.5 - robustez a taxa de desconto (pacote, excl. RB4/RB8) ===')
RBs = ('RB1', 'RB2', 'RB3', 'RB5', 'RB6', 'RB7')

def media_geral(suf):
    return sum(pac[f'{rb}|{c}' + suf]['valor_opcao']
               for rb in RBs for c in CIDADES) / (len(RBs) * 3)

m3, m1, m5 = media_geral(''), media_geral('|r1pct'), media_geral('|r5pct')
print(f'3%={m3:.1f}  1%={m1:.1f} ({(m1 - m3) / m3 * 100:+.1f}%)  '
      f'5%={m5:.1f} ({(m5 - m3) / m3 * 100:+.1f}%)')
