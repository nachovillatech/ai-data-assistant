# 🤖 AI Data Assistant (Open WebUI + LM Studio / Ollama + PostgreSQL)

Asistente de IA privado que conecta **Open WebUI** con modelos de lenguaje locales (LLMs) ejecutados a través de **LM Studio / Ollama** y bases de datos PostgreSQL en tiempo real mediante herramientas personalizadas en Python.

Diseñado para permitir a empresas realizar consultas sobre sus propios datos manteniendo **privacidad total (100% On-Premise, sin costes por API y totalmente gratuito)**.

---

## ✨ Características clave

- 🔒 **100% Privado, Gratuito y Local:** Basado en modelos de código abierto ejecutados en local mediante LM Studio o Ollama. Los datos nunca salen de la infraestructura de la empresa.
- ⚡ **Consultas SQL en tiempo real:** Herramienta personalizada de Python que traduce preguntas en lenguaje natural a consultas `SELECT`.
- 🛡️ **Seguridad integrada:** Filtros estrictos de solo lectura (bloqueo de `DELETE`, `UPDATE`, `DROP`) y timeout de ejecución.
- 🐳 **Despliegue en Docker:** Entorno contenedorizado para la interfaz con Open WebUI.
- 📚 **Soporte RAG:** Integración con bases de conocimiento internas (documentación, manuales).

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
|---|---|
| Interfaz de Usuario | Open WebUI |
| Motor de Inferencia Local | LM Studio (Modo Servidor OpenAI-compatible) / Ollama |
| Base de Datos | PostgreSQL |
| Integración Custom | Python (`psycopg2`) con validación de seguridad |
| Contenedores | Docker + Docker Compose |

---

## 🏗️ Arquitectura del Sistema

```
👤 Empleados (Navegador Web)
    │
    ▼
🖥️ Open WebUI (Docker - Puerto 3080)
    │
    ├───────────► 🧠 LM Studio / Ollama (Servidor Local de Inferencia LLM)
    │
    └───────────► 🐍 Custom Python Tool (Validación SQL)
                       │
                       ▼
                 🗄️ PostgreSQL (BBDD en tiempo real)
```

---

## 📸 Demostración del Sistema

### 1. Interfaz de Chat (Open WebUI con acceso a BBDD)
![Open WebUI Chat](docs/openwebui-chat.png)

### 2. Motor de Inferencia Local (LM Studio Modo Servidor)
![LM Studio Server](docs/lmstudio-server.png)

---

## 📁 Estructura del Repositorio

- `docker/`: Archivos `docker-compose.yml` para desplegar Open WebUI.
- `scripts/`: Herramientas personalizadas en Python para Open WebUI (Conector PostgreSQL seguro).
- `docs/`: Capturas de pantalla y documentación gráfica de la arquitectura.

---

## 👤 Autor

**Ignacio** — [GitHub Profile](https://github.com/nachovillatech)
