---
transition: fade
theme: the-unnamed
layout: cover
background: ./assets/slide-00-bg.png
---


---
transition: slide-up
layout: cover
background: ./assets/slide-00-bg.png
---

# Tá bom, Senhor Segurança. **Mas o que isso significa?**

Fiquem confortáveis! <br />
Vocês caíram na minha carta armadilha! <br />
Essa talk na verdade é sobre **linguística** e **biologia**.

<!--
This is a **note**
-->

---
transition: slide-up
theme: the-unnamed
layout: cover
background: ./assets/slide-00-bg.png
---

# **Quem sou eu?**

---
transition: fade
layout: about-me

helloMsg: Olá seres da quinta dimensão!
name: Nilton Frederico
imageSrc: ./assets/slide-02-bg.png
position: left
job: Python Specialist @ JS+
---


---
transition: slide-up
layout: about-me-curiosities

imageSrc: ./assets/slide-02-bg.png
position: left
line1:
line2:
---

<v-click>- Sou de Ribeirão Preto, aqui em São Paulo!
  - <small>Minha primeira Python Brasil foi lá em 2019!</small></v-click>
<v-click>- Sou o sexto Nilton da minha família!</v-click>
<v-click>- Já publiquei um quadrinho!</v-click>
<v-click>- Tenho dois diabretes, digo, gatas! Connie e Luz!</v-click>
<v-click>- Programador desde 2009, Pythonista desde 2014!</v-click>

---
transition: slide-up
layout: cover
background: ./assets/slide-00-bg.png
---

# Imposto felino em 3<v-click>, 2</v-click><v-click>, 1</v-click>...

---
transition: slide-up
layout: two-cols
background: ./assets/slide-00-bg.png
---

<img src="./assets/cat-tax-connie.jpg" />

::right::

<img src="./assets/cat-tax-luz.jpg" />

---
transition: fade-in
layout: about-me-social

linkedin: https://www.linkedin.com/in/nilton-teixeira/
github: https://github.com/niltonfrederico/
telegram: https://t.me/kuresto
bluesky: https://bsky.app/profile/kuresto.bsky.social
---

---
transition: slide-up
layout: about-me-social
highlight_telegram: true

linkedin: https://www.linkedin.com/in/nilton-teixeira/
github: https://github.com/niltonfrederico/
telegram: https://t.me/kuresto
bluesky: https://bsky.app/profile/kuresto.bsky.social
---

---
transition: fade
layout: section
background: ./assets/slide-01-bg.jpg
---

Tudo que é importante começa com uma indagação...

---
transition: fade
layout: section
background: ./assets/slide-01-bg.jpg
---

<h1>Se a terra é redonda, por que ela se chama <b>planeta</b> e não redondeta?</h1>
<div style="text-align: right;">
- Alguém, provavelmente.
</div>

---
transition: fade
layout: section
background: ./assets/slide-01-bg.jpg
---

**Planeta** vem do grego antigo **πλανήτης**, que significa algo como "andarilho" ou "errante", e não tem nada a ver com a forma da Terra, mas sim com o tipo de movimento que ela e os demais planetas realizam.

---
transition: fade
layout: section
background: ./assets/slide-01-bg.jpg
---

<h1>Tá, e eu com isso?</h1>

---
transition: fade
layout: section
background: ./assets/slide-01-bg.jpg
---

<h1>Simples! A origem da palavra, da informação, seu contexto, define seu uso! Ela pode significar "errante" mas você não chama um viajante de planeta!</h1>

---
transition: fade
layout: section
background: ./assets/slide-01-bg.jpg
---

<h1>Seres humanos são criaturas sociais. E na maioria das vezes começamos a nos relacionar com a seguinte indagação: <b>"Qual o seu nome?"</b></h1>

---
transition: slide-up
theme: the-unnamed
layout: image
image: ./assets/slide-03-bg.png
---

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# Vulnerabilidades

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# CWE

## Common Weaknesses Enumeration

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# CVE

## Common Vulnerabilities and Exposures

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# CVSS

## Common Vulnerability Scoring System

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# CAPEC

## Common Attack Pattern Enumeration and Classification

---
transition: slide-up
layout: cover
background: ./assets/slide-04-bg.jpg
---

# Não? Vamos tentar de outra forma...

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# Taxonomia

## Taxonomia é o estudo da organização e classificação dos seres vivos, que agrupa organismos com base em características comuns e relações evolutivas.

## Reino -> Filo -> Classe -> Ordem -> Família -> Gênero -> Espécie

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# Taxonomia de uma vulnerabilidade

## Não necessariamente é uma hierarquia (pois sua ordem pode variar), mas a relação é similar o bastante.

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

## **A vulnerabilidade** <br /> <v-click>é tipificada por uma CWE <br /></v-click> <v-click>é identificada por uma CVE <br /></v-click> <v-click>é classificada por uma CVSS <br /></v-click> <v-click>é demonstrada por uma CAPEC</v-click>

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

## Mas só existe uma **vulnerabilidade** se existe valor em explorá-la! Todo exploit visa a atacar um dos pilares de segurança: <br /> <v-click>Confidencialidade</v-click><v-click>, Integridade</v-click><v-click>, Disponibilidade</v-click><v-click>, Autenticidade</v-click><v-click> e Irretrabilidade</v-click>

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

## Nosso exemplo: **Heartbleed**. <br> <small>(Provavelmente a segunda vulnerabilidade mais famosa, atrás apenas do SQL Injection)</small>


---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# CWE-126
## [Buffer Over-read](https://cwe.mitre.org/data/definitions/126.html)

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# CVE-2014-0160
## [SSL/TLS Heartbeat Extension Memory Leak](https://nvd.nist.gov/vuln/detail/CVE-2014-0160)

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# CVSS
## 3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N

<!--
3.1 -> Versão
AV:N -> Access Vector: Network (N = Network, A = Adjacent, L = Local, P = Physical)
AC:L -> Access Complexity: Low (L = Low, H = High)
PR:N -> Privileges Required: None (N = None, L = Low, H = High)
UI:N -> User Interaction: None (N = None, R = Required)
S:U -> Scope: Unchanged (Changed significa que afeta mais que o escopo da vulnerabilidade)
C:H -> Confidentiality: High (N = None, L = Low, H = High)
I:N -> Integrity: None (N = None, L = Low, H = High)
A:N -> Availability: None (N = None, L = Low, H = High)
-->

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# CVSS
## <v-click>3.1</v-click><v-click>/AV:N</v-click><v-click>/AC:L</v-click><v-click>/PR:N</v-click><v-click>/UI:N</v-click><v-click>/S:U</v-click><v-click>/C:H</v-click><v-click>/I:N</v-click><v-click>/A:N</v-click>

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# CAPEC-540
## [Overread Buffers](https://capec.mitre.org/data/definitions/540.html)

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# Opnião
## [CVE Feed](https://cvefeed.io/vuln/detail/CVE-2025-59681) é um bom agregador de informações sobre vulnerabilidades.

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# E como posso me proteger?

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# Simples!

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# Não dá!

<!-- Explique que não dá pois se proteger não significa que nada de ruim irá acontecer mas que o risco de exploração diminui -->

---
transition: slide-up
layout: cover
background: ./assets/slide-04-bg.jpg
---

## Proteger não significa que vulnerabilidades passam a mágicamente não existir. <br /> <small>Nem tampouco que não serão exploradas.</small> <br /><v-click><b>Mas podemos mitiga-las!</b></v-click>


---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# Cade o Python?

---
transition: fade
layout: cover
background: ./assets/slide-04-bg.jpg
---

# Existem dois tipos de problemas:

## Meus problemas, os problemas dos outros e nossos problemas.

<!-- Piada com discalculia -->

---
transition: fade
layout: image-right
background: ./assets/slide-04-bg.jpg
image: ./assets/dick.jpg
---

# Meus problemas: Bandit

Instalação:

```python
pip install bandit
```

E para executar:

```python
bandit -r .
```
<!--
Live coding time!
-->
---
transition: fade
layout: image-right
background: ./assets/slide-04-bg.jpg
image: ./assets/dredd.jpg
---

# Problemas dos outros: pip-audit

Instalação:

```python
pip install pip-audit
```

E para executar:

```python
pip-audit --recursive
```
<!--
Live coding time!
-->
---
transition: slide-up
layout: image-right
background: ./assets/slide-04-bg.jpg
image: ./assets/dependabot.svg
---

# Nossos problemas: dependabot

Instalação? [No seu repositório do github!](https://github.com/niltonfrederico/aetna_core/security/dependabot)

<!--
Mostre suas vulnerabilidades.
Mostre as configurações.
Fale sobre o .github/dependabot.yml
-->

---
transition: slide-up
layout: about-me-social

linkedin: https://www.linkedin.com/in/nilton-teixeira/
github: https://github.com/niltonfrederico/
telegram: https://t.me/kuresto
bluesky: https://bsky.app/profile/kuresto.bsky.social
heading: Q/A
---

---
transition: fade-out
layout: cover
background: ./assets/slide-00-bg.png
---
