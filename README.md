# 🤖 AI Data Assistant

Asistente de IA privado que conecta modelos de lenguaje locales (LLMs) con bases de datos en tiempo real. Diseñado para que cualquier empresa pueda hacer preguntas sobre sus propios datos sin depender de servicios externos como ChatGPT.

---

## ✨ ¿Qué hace?

- Responde preguntas en lenguaje natural sobre datos reales de una base de datos
- Funciona 100% en local — los datos nunca salen de la empresa
- Integración con bots de Telegram para consultas desde cualquier lugar
- Automatización de flujos con n8n
- RAG con documentos internos (manuales, catálogos, procedimientos)

---

## 🛠️ Tecnologías usadas

| Capa | Tecnología |
|---|---|
| Modelo de IA | Ollama + modelos locales (Qwen, Llama, Mistral) |
| Base de datos | PostgreSQL |
| Interfaz de chat | Open WebUI |
| Automatización | n8n |
| Bots | Telegram Bot API |
| Contenedores | Docker + Docker Compose |
| Backend | Python + FastAPI |

---

## 🏗️ Arquitectura

```
👤 Usuario
    │
    ▼
💬 Telegram Bot  ──────  🖥️ Open WebUI
    │                         │
    └──────────┬──────────────┘
               │
               ▼
        ⚙️ FastAPI (Backend)
               │
       ┌───────┼───────┐
       │       │       │
       ▼       ▼       ▼
  🧠 Ollama  🗄️ PostgreSQL  🔄 n8n
  (LLM local)  (BBDD)    (Automatización)
```

---

## 🚀 Estado del proyecto

- [x] Arquitectura definida
- [x] Conexión LLM local con Open WebUI
- [x] Conexión a PostgreSQL en tiempo real
- [ ] Bot de Telegram funcional
- [ ] RAG con documentos
- [ ] Docker Compose completo

---

## 👤 Autor

**Ignacio** — [GitHub](https://github.com/nachovillatech)
