# 📊 Calculadora Numérica Interativa

Bem-vindo à Calculadora Numérica, um projeto desenvolvido para explorar métodos de resolução numérica de forma didática e interativa. Através de uma interface amigável e responsiva, é possível navegar entre diferentes algoritmos e visualizar exemplos de entradas e saídas.

---

## ✨ Resumo

Neste projeto, você encontrará:

- **Equações Não Lineares**: Métodos como o Teorema de Bolzano, Bisseção, Newton-Raphson e Secante para encontrar raízes de equações.
- **Sistemas Lineares**: Soluções com Eliminação de Gauss, Gauss-Jacobi, Gauss-Seidel e outros métodos iterativos.
- **Interpolação**: Lagrange, Newton-Gregory e Interpolação Inversa para estimar valores intermediários.
- **Extrapolação**: Aplicação do Método dos Mínimos Quadrados para ajuste de curvas e previsão.
- **Integração**: Utilização do Método do Trapézio Composto para integrais definidas.

Cada método conta com interface visual e exemplos práticos.

---

## 🧠 Equações Não Lineares

### 🔹 Teorema de Bolzano
**Entrada:** `x² - 1 = 0`  
**Saída:** Intervalos possíveis: `[-1.2, -1.0]`, `[0.8, 1.0]`

### 🔹 Bissecção
**Entrada:** `x² - 1 = 0`  
**Saída:** Raízes: `-1.0`, `1.0`

### 🔹 Newton-Raphson
**Entrada:** `x² - 1 = 0`  
**Saída:** Raízes: `-1.0`, `1.0`

### 🔹 Secante
**Entrada:** `x² - 1 = 0`  
**Saída:** Raízes: `-1.0`, `1.0`

---

## 🧮 Sistemas Lineares

### 🔹 Eliminação de Gauss
**Entrada:**
```
4x - y + z = 8  
-x + 3y - z = -11  
x - y + 5z = 3
```
**Saída:** x = 1.24, y = -3.36, z = -0.32

### 🔹 Gauss-Jacobi
**Saída:** x = 1.2399, y = -3.3599, z = -0.3200

### 🔹 Gauss-Seidel
**Saída:** x = 1.24, y = -3.36, z = -0.32

---

## 📊 Interpolação

### 🔹 Lagrange
**Entrada:** (1, 2), (2, 3), (3, 5)  
**Saída:** f(x) = 0.5x² - 0.5x + 2.0

### 🔹 Newton-Gregory
**Entrada:**  
X: 1, 2, 3, 4, 5  
Y: 2, 3, 5, 7, 11  
**Interpolar em:** x = 6  
**Saída:** Resultado ≈ 22

### 🔹 Interpolação Inversa
**Saída:** y = -1 + 2.2x

---

## 📈 Extrapolação

### 🔹 Mínimos Quadrados
**Entrada:** (1,2), (2,3), (3,5)  
**Saída:**
```
f(x) = 0.5x² - 0.5x + 2.0  
Coeficientes: a = 0.5, b = -0.5, c = 2.0
```

---

## ∫ Integração

### 🔹 Trapézio Composto
**Expressão:** x² + 2x + 1  
**Intervalo:** A = 0, B = 1  
**Resultado:** ≈ 2.3354

---

## 🛠️ Tecnologias Utilizadas

- HTML5 + CSS3
- JavaScript Puro
- Responsivo com Flexbox
- Gradientes, sombras e animações CSS

---

## 🚀 Como Usar

1. Clone ou baixe este repositório:
   ```bash
   https://github.com/KayBranco/metodos-numericos
   ```
2. Abra o arquivo `index.html` no seu navegador.
3. Clique em qualquer botão para explorar os métodos numéricos.

> 💡 Recomendo usar o [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) do VS Code para uma experiência fluida.

---

## 🙌 Contribua

Se você encontrar problemas, tiver ideias ou quiser melhorar a interface, fique à vontade para abrir uma **issue** ou enviar um **pull request**.

---

## 👨‍💻 Autor

**Kaiky Lucas De Andrade**  
Engenharia da Computação - UNITAU  
📧 kaikylucas65@gmail.com
🔗 [https://github.com/kaikylucas](https://github.com/kaikylucas)
