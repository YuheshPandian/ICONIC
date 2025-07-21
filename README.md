<img src="assets/social_banner.png"/>

> Be iconic, not generic.  
> A dev-focused library of sleek, bubble-shaped skill icons built for GitHub READMEs, portfolios, and resumes.

---

<div align="center">
  
![ICONS COUNTER](https://img.shields.io/github/directory-file-count/YuheshPandian/ICONIC/icons%2Fdark?style=for-the-badge&label=Icons&color=%23753ec1)
![Repo size](https://img.shields.io/github/repo-size/YuheshPandian/ICONIC?style=for-the-badge&color=%23ff5842)
![Issues with label:icon](https://img.shields.io/github/issues/YuheshPandian/ICONIC/icon?style=for-the-badge)

</div>

## ✨ Features

-   🟦 Bubble icons designed for clarity and aesthetics
-   🌙 Light & dark theme variants for every icon
-   🧩 Easy to embed in Markdown, HTML, or anywhere
-   ⚙️ HTML preview API with Django backend
-   💾 Download-ready SVGs

---

## 🧪 Quick Implementation

Here's a sample of some icons:

```markdown
## HTML

<!-- Use div tag for good format and it will show them in one line, without div tag it will be displayed on multiple lines -->
<div style="display: flex; gap: 2px; align-items: center;">
<img src="https://iconic-api.onrender.com/dark/python" width="64px" />
<img src="https://iconic-api.onrender.com/dark/html" width="64px" />
<img src="https://iconic-api.onrender.com/dark/js" width="64px" />
<div>
```

> [!NOTE]  
> It's recommended to use the HTML snippet in GitHub READMEs, as it allows better control over size, styling, and layout.

### Dark:

<div style="display: flex; gap: 2px; align-items: center;">
  <img src="https://iconic-api.onrender.com/dark/python" width="50px" title="Python (Dark)" />
  <img src="https://iconic-api.onrender.com/dark/html" width="50px" title="HTML (Dark)" />
  <img src="https://iconic-api.onrender.com/dark/dart" width="50px" title="Dart (Dark)" />
  <img src="https://iconic-api.onrender.com/dark/css" width="50px" title="CSS (Dark)" />
  <img src="https://iconic-api.onrender.com/dark/git" width="50px" title="Git (Dark)" />
  <img src="https://iconic-api.onrender.com/dark/github" width="50px" title="GitHub (Dark)" />
  <img src="https://iconic-api.onrender.com/dark/linux" width="50px" title="Linux (Dark)" />
  <img src="https://iconic-api.onrender.com/dark/vscode" width="50px" title="VS Code (Dark)" />
  <img src="https://iconic-api.onrender.com/dark/docker" width="50px" title="Docker (Dark)" />
  <img src="https://iconic-api.onrender.com/dark/bash" width="50px" title="Bash (Dark)" />
  <img src="https://iconic-api.onrender.com/dark/figma" width="50px" title="Figma (Dark)" />
  <img src="https://iconic-api.onrender.com/dark/nodejs" width="50px" title="Node.js (Dark)" />
</div>



### Light:

<div style="display: flex; gap: 2px; align-items: center;">
  <img src="https://iconic-api.onrender.com/light/python" width="50px" title="Python (Light)" />
  <img src="https://iconic-api.onrender.com/light/html" width="50px" title="HTML (Light)" />
  <img src="https://iconic-api.onrender.com/light/dart" width="50px" title="Dart (Light)" />
  <img src="https://iconic-api.onrender.com/light/css" width="50px" title="CSS (Light)" />
  <img src="https://iconic-api.onrender.com/light/git" width="50px" title="Git (Light)" />
  <img src="https://iconic-api.onrender.com/light/github" width="50px" title="GitHub (Light)" />
  <img src="https://iconic-api.onrender.com/light/linux" width="50px" title="Linux (Light)" />
  <img src="https://iconic-api.onrender.com/light/vscode" width="50px" title="VS Code (Light)" />
  <img src="https://iconic-api.onrender.com/light/docker" width="50px" title="Docker (Light)" />
  <img src="https://iconic-api.onrender.com/light/bash" width="50px" title="Bash (Light)" />
  <img src="https://iconic-api.onrender.com/light/figma" width="50px" title="Figma (Light)" />
  <img src="https://iconic-api.onrender.com/light/nodejs" width="50px" title="Node.js (Light)" />
</div>

---

## 🚀 Getting Started (Dev Setup)

> ```bash
> # Clone the repository
> git clone https://github.com/YuheshPandian/ICONIC.git
> 
> # Navigate into the project folder
> cd ICONIC
> 
> # (Optional) Create a virtual environment
> python -m venv venv
> 
> # Activate the virtual environment (Linux/Mac)
> source venv/bin/activate
> 
> # Activate the virtual environment (Windows)
> venv\Scripts\activate
> 
> # Install dependencies
> pip install -r requirements.txt
> 
> # Run the Django development server
> python api/manage.py runserver
>
>
> # Visit http://localhost:8000/ for index page
> # Visit http://localhost:8000/gallery/ to view the Icon Gallery
> # Use this query to get the dark icon file http://localhost:8000/dark/[icon_name]
> # Use this query to get the light icon file http://localhost:8000/light/[icon_name]
> ```




---

## 🤝 Contributing

Have a new icon idea or want to help expand the collection?  
Pull requests are welcome!

-   Create your icon using a photo editing software (Inkscape preferred) and open the dark/light icon template and start editing.
-   Add the dual versions of icon in respective dark/light folders
-   Push the changes if completed

> Please follow the existing folder structure (`dark/` and `light/`), keep icon dimensions consistent (e.g., 512x512 SVG), and use meaningful file names.

---

## 📜 License

[MIT License](LICENSE)

---
