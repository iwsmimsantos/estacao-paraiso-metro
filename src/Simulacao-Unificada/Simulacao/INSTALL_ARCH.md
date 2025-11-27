# 🐧 Instalação no Arch Linux

## Problema Identificado

Seu sistema Arch Linux usa **ambiente Python gerenciado externamente** (PEP 668), o que impede a instalação de pacotes Python diretamente no sistema.

## ✅ Solução: Usar Ambiente Virtual

### Opção 1: Instalação Rápida (Recomendada)

Execute estes comandos **no seu terminal** (zsh):

```bash
# 1. Navegue até o diretório
cd "/home/nicolasramon/Documents/Github Inteli/2025-2B-T13-ES08-G01/src/Simulacao-Unificada/Simulacao"

# 2. Crie o ambiente virtual
python3 -m venv venv

# 3. Ative o ambiente virtual
source venv/bin/activate

# 4. Atualize pip (importante!)
python3 -m pip install --upgrade pip

# 5. Instale as dependências
pip install -r requirements.txt

# 6. Inicie o servidor
python3 main.py
```

### Opção 2: Instalar python-pip globalmente (requer sudo)

Se preferir instalar o pip globalmente:

```bash
# Instalar python-pip via pacman
sudo pacman -S python-pip

# Depois instalar as dependências no venv
cd "/home/nicolasramon/Documents/Github Inteli/2025-2B-T13-ES08-G01/src/Simulacao-Unificada/Simulacao"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## 🔄 Para usar novamente (depois de fechar o terminal)

Sempre que quiser iniciar o servidor novamente:

```bash
cd "/home/nicolasramon/Documents/Github Inteli/2025-2B-T13-ES08-G01/src/Simulacao-Unificada/Simulacao"
source venv/bin/activate
python3 main.py
```

## 🛑 Para desativar o ambiente virtual

```bash
deactivate
```

## 📝 Verificar se funcionou

Depois de instalar, teste:

```bash
# Verificar se FastAPI está instalado
python3 -c "import fastapi; print('✓ FastAPI instalado:', fastapi.__version__)"

# Verificar se uvicorn está instalado
python3 -c "import uvicorn; print('✓ Uvicorn instalado:', uvicorn.__version__)"
```

## 🚀 Acessar as APIs

Após iniciar o servidor com sucesso, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

---

## ⚠️ Problemas Comuns

### Erro: "No module named '_ctypes'"

```bash
sudo pacman -S libffi
```

### Erro: "ensurepip is not available"

```bash
sudo pacman -S python-pip
```

### Erro ao criar venv

```bash
sudo pacman -S python-virtualenv
python3 -m virtualenv venv
```

---

✅ **Pronto!** Seu ambiente estará configurado e as APIs estarão rodando.

