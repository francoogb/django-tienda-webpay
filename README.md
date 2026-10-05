<h1 align="center">🛒 Tienda Online con Django + Webpay</h1>

<p align="center">
  Aplicación de e-commerce completa desarrollada con Django e integrada con la pasarela de pago <strong>Webpay</strong> de Transbank.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Webpay-EE0000?style=flat-square&logo=mercadopago&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" />
</p>

---

## 📸 Captura

<!-- Reemplaza esta línea con una captura real del proyecto -->
<p align="center"><em>Agregar aquí captura de la tienda / proceso de pago</em></p>

---

## ✨ Características

- 🛍️ **Catálogo de productos** con slider de productos destacados
- 🛒 **Carrito de compras** persistente
- 💳 **Pago integrado con Webpay** (Transbank) — flujo completo de pago seguro
- 👤 **Autenticación de usuarios** (registro e inicio de sesión)
- 🔐 **Recuperación de contraseña** por correo
- 📂 **Gestión de productos** desde el panel administrativo de Django
- 🖼️ **Carga de imágenes** de productos (manejo de archivos media)
- 🎨 **Diseño responsive** adaptable a móvil y escritorio

---

## 🧱 Stack técnico

| Capa | Tecnología |
|------|------------|
| Backend | Django (Python) |
| Base de datos | SQLite |
| Pasarela de pago | Transbank Webpay Plus |
| Frontend | HTML5, CSS3, JavaScript |
| Autenticación | Sistema de usuarios de Django |

---

## 📂 Estructura del proyecto

```
django-tienda-webpay/
├── acceso/          # App de login, registro y recuperación de contraseña
├── app/             # Configuración principal del proyecto Django
├── carro/           # Lógica del carrito de compras
├── productos/       # App de gestión de productos
├── tienda/          # Vista principal y rutas de la tienda
├── utilidades/      # Funciones auxiliares (Webpay, correos, etc.)
├── media/producto/  # Imágenes de los productos
├── static/          # Archivos estáticos (CSS, JS, imágenes)
├── templates/       # Plantillas HTML
├── db.sqlite3       # Base de datos
└── manage.py        # Comando principal de Django
```

---

## 🚀 Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/francoogb/django-tienda-webpay.git
cd django-tienda-webpay
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En macOS / Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si no existe `requirements.txt`, instala manualmente:
> ```bash
> pip install django transbank-sdk pillow
> ```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario (opcional, para el admin)

```bash
python manage.py createsuperuser
```

### 6. Correr el servidor

```bash
python manage.py runserver
```

Abre tu navegador en: **http://127.0.0.1:8000/**

---

## 💳 Configuración de Webpay

El proyecto usa las credenciales de **ambiente de integración** de Transbank para pruebas. Para pasar a producción, debes:

1. Registrarte como comercio en [Transbank](https://www.transbankdevelopers.cl/)
2. Reemplazar las credenciales en el archivo de configuración de Webpay
3. Cambiar el entorno de `IntegrationType.TEST` a `IntegrationType.LIVE`

### Tarjetas de prueba

Puedes usar las tarjetas de prueba oficiales de Transbank:

- **VISA aprobada:** `4051 8856 0044 6623` · CVV `123`
- **MASTERCARD rechazada:** `5186 0595 5959 0568`

---

## 🎯 Lo que aprendí construyendo este proyecto

- Integración de pasarelas de pago reales (Transbank Webpay)
- Manejo de sesiones y carro de compras en Django
- Envío de correos para recuperación de contraseña
- Gestión de archivos media y servido de imágenes
- Flujo completo de autenticación de usuarios

---

## 📬 Contacto

**Franco Ignacio** · Desarrollador Full Stack
📧 [fran.valdenegr@gmail.com](mailto:fran.valdenegr@gmail.com)
💼 [GitHub @francoogb](https://github.com/francoogb)
📍 Santiago de Chile

---

<p align="center">
  <em>Si te sirvió el proyecto, ⭐ dale una estrella en GitHub.</em>
</p>
