# 🤖 AI Data Assistant (Open WebUI + PostgreSQL)

Asistente de IA privado que conecta **Open WebUI** y modelos de lenguaje locales (LLMs) con bases de datos PostgreSQL en tiempo real mediante herramientas personalizadas en Python.

Diseñado para permitir a empresas realizar consultas sobre sus propios datos manteniendo la privacidad total (100% On-Premise).

---

## ✨ Características clave

- 🔒 **100% Privado y Local:** Los datos nunca salen de la infraestructura de la empresa.
- ⚡ **Consultas SQL en tiempo real:** Herramienta personalizada de Python que traduce preguntas en lenguaje natural a consultas `SELECT`.
- 🛡️ **Seguridad integrada:** Filtros estrictos de solo lectura (bloqueo de `DELETE`, `UPDATE`, `DROP`) y timeout de ejecución.
- 🐳 **Despliegue sencillo:** Docker Compose para desplegar el entorno en minutos.
- 📚 **Soporte RAG:** Integración con bases de conocimiento internas (documentación, manuales).

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
|---|---|
| Interfaz de Usuario | Open WebUI |
| Modelo de IA | Ollama / LM Studio (Modelos locales: Qwen, Llama, Mistral) |
| Base de Datos | PostgreSQL |
| Integración Custom | Python (`psycopg2`) con validación de seguridad |
| Contenedores | Docker + Docker Compose |

---

## 🏗️ Arquitectura del Sistema

```
👤 Empleados (Navegador Web)
    │
    ▼
🖥️ Open WebUI (Puerto 3080)
    │
    ├───────────► 🧠 Ollama / LM Studio (Motor LLM)
    │
    └───────────► 🐍 Custom Python Tool (Validación SQL)
                       │
                       ▼
                 🗄️ PostgreSQL (BBDD en tiempo real)
```

---

## 📁 Estructura del Repositorio

- `docker/`: Archivos `docker-compose.yml` para desplegar Open WebUI.
- `scripts/`: Herramientas personalizadas en Python para Open WebUI (Conector PostgreSQL seguro).
- `docs/`: Guías de configuración y capturas del sistema.

---

## 👤 Autor

**Ignacio** — [GitHub Profile](https://github.com/nachovillatech)
