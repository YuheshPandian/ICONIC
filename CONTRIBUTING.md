
# Contributing to ICONIC

First off, thanks for checking out ICONIC — the sleek bubble icon library for devs who like things clean and cool. Whether you're adding a new icon, fixing a bug, or improving the docs, your contribution is appreciated!

---

## 🛠️ How to Contribute

### 1. Fork + Clone

```bash
# Fork the repo and clone it
git clone https://github.com/YOUR_USERNAME/ICONIC.git
cd ICONIC
```

---

### 2. Add an Icon

Got a new icon idea? Awesome.

- 🔧 Use [Inkscape](https://inkscape.org) (recommended) or any SVG editor of your choice.
- 🎨 Open the existing dark/light icon template.
- 🌓 Create **both** dark and light variants of your icon.
- 🗂️ Place them in their respective folders:
  - `icons/dark/your-icon.svg`
  - `icons/light/your-icon.svg`
- 🧼 Ensure the SVGs are:
  - 512x512 in dimension
  - Clean, minimal, and bubble-shaped like the existing ones
  - Named clearly (e.g., `go.svg`, `typescript.svg`)

---

### 3. Run + Test the API (Optional)

If you're modifying the Django API backend:

```bash
cd api
pip install -r requirements.txt
python api/manage.py runserver
```

Make sure everything still works — especially the preview routes!

---

### 4. Commit + Push

```bash
# Create a new branch
git checkout -b add-icon-python

# Commit your changes
git add .
git commit -m "Added Python icon in dark and light variants"

# Push to your fork
git push origin add-icon-python
```

---

### 5. Submit a Pull Request

Open a pull request on GitHub with a clear title and description of what you’ve added or changed. Utilize the PR template to streamline the process.

---

## 📋 Style Guide

- Maintain existing **naming conventions** (lowercase, hyphen-separated if needed).
- Icons should be **512x512 SVGs** with minimal paths.
- Keep it **bubble-themed**, **aesthetic**, and **legible at small sizes**.
- Light and dark icons should have **consistent shapes**, only differing in colors( use the templates ).
- When using Inkscape, convert the standard SVG file into a **plain SVG** format.
- The icon file must be no larger than **10 MB**.

---

## 🙏 Thanks!

You're helping build a better, more beautiful dev world — one icon at a time.

Now go be iconic. 🔥

