# Get Better - Complete Project Index

## Welcome! 👋

You now have a **complete, production-ready** web application called **"Get Better"** - a non-profit platform helping people quit harmful substances, improve their lifestyle, and enhance their appearance.

## 📚 Documentation Files

### Start Here
1. **[QUICKSTART.md](QUICKSTART.md)** ⭐ **START HERE**
   - How to run locally in 3 steps
   - What files do what
   - How to test the platform
   - Deployment basics

### Understanding the Project
2. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)**
   - What was built and why
   - All features explained
   - Technology stack
   - Key differentiators

3. **[USER_FLOW.md](USER_FLOW.md)**
   - Complete user journey walkthrough
   - Example of how someone uses the platform
   - Screenshots of what users see
   - Detailed explanation of each page

4. **[README.md](README.md)**
   - Complete documentation
   - Installation instructions
   - API endpoints
   - Contribution guidelines
   - License info

### Deployment
5. **[DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)**
   - Pre-deployment checklist
   - Testing steps
   - GitHub setup
   - Render deployment guide
   - Troubleshooting
   - Production requirements

---

## 🗂️ File Structure

```
NonProfit/
│
├── 📄 Documentation
│   ├── README.md              (Full documentation)
│   ├── QUICKSTART.md          (Quick start guide)
│   ├── PROJECT_SUMMARY.md     (What was built)
│   ├── USER_FLOW.md           (User journey)
│   ├── DEPLOYMENT_CHECKLIST.md (Deploy guide)
│   └── INDEX.md               (This file)
│
├── 🐍 Python Backend
│   ├── app.py                 (Flask application - 400+ lines)
│   ├── config.py              (Configuration classes)
│   ├── requirements.txt       (Python dependencies)
│   └── Procfile               (For Render deployment)
│
├── 🎨 Frontend
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css      (Dark theme CSS - 1000+ lines)
│   │   └── js/
│   │       └── main.js        (JavaScript interactivity)
│   │
│   └── templates/
│       ├── base.html          (Navigation + footer)
│       ├── home.html          (Landing page)
│       ├── signup.html        (Sign up form)
│       ├── login.html         (Login form)
│       ├── onboarding.html    (Goal selection - KEY FEATURE)
│       ├── dashboard.html     (User plans with dropdowns)
│       ├── plan_detail.html   (Detailed plan pages)
│       ├── about.html         (About page)
│       └── contact.html       (Contact form)
│
├── ⚙️ Configuration
│   ├── .gitignore             (Git ignore rules)
│   ├── .env.example           (Environment variables template)
│   └── config.py              (Environment configuration)
```

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the App
```bash
python app.py
```

### Step 3: Open in Browser
```
http://localhost:5000
```

Test it out! Create an account and see your personalized plans.

---

## ✨ Key Features

### 🎯 What Makes This Special
- **Multi-Goal Support**: Quit vaping AND get fit at the same time
- **Personalized Plans**: Based on YOUR frequency, stats, and goals
- **Dark Theme**: Modern, eye-friendly interface
- **Mobile First**: Hamburger menu, collapsible dropdowns
- **Non-Corny**: Real information, not motivational nonsense
- **Science-Backed**: Evidence-based recommendations
- **Fully Responsive**: Works perfectly on all devices

### 💊 Substances Covered
1. Vaping/E-cigarettes
2. Nicotine
3. Alcohol
4. Tobacco/Smoking
5. Cannabis/Weed
6. Hard Drugs

### 💪 Lifestyle Options
1. **Fitness & Body Composition**
   - Choose: Build muscle OR lose weight
   - Input: Age, height, weight, activity level
   - Output: 8-week personalized plan

2. **Appearance & Looks**
   - Skincare science
   - Fitness impact
   - Fashion fundamentals
   - What works vs. cope

---

## 🌐 Technology Stack

**Backend**
- Python 3.8+
- Flask (web framework)
- SQLAlchemy (database ORM)
- Werkzeug (security - password hashing)

**Frontend**
- HTML5
- CSS3 (dark theme, responsive)
- Vanilla JavaScript (no jQuery/React - lightweight!)

**Database**
- SQLite (development)
- PostgreSQL (production)

**Deployment**
- Render (PaaS - easy deployment)
- GitHub (version control)

---

## 📋 Database Schema

### Users Table
```sql
id (Primary Key)
email (Unique)
password (Hashed)
created_at (Timestamp)
```

### User Plans Table
```sql
id (Primary Key)
user_id (Foreign Key → User)
category (substance/lifestyle/looks)
selected_items (Comma-separated goals)
plan_data (Full personalized plan)
created_at (Timestamp)
```

---

## 🎯 User Journey (Simplified)

1. **Home Page** → "Start Your Journey"
2. **Sign Up** → Create account
3. **Onboarding** → Select goals (can choose multiple!)
4. **Dashboard** → See collapsible plan cards
5. **Plan Details** → View full personalized plan
6. **Track Progress** → Return anytime to view plans
7. **Edit Plans** → Change selections anytime

---

## 🔐 Security Features

✅ Passwords hashed with Werkzeug  
✅ Session-based authentication  
✅ HTTPS-ready for production  
✅ SQL injection prevention (SQLAlchemy ORM)  
✅ Secure session cookies  
✅ Environment variables for secrets  
✅ No sensitive data in code  

---

## 📱 Responsive Design

**Desktop (> 768px)**
- Full navigation bar
- Multi-column grid layouts
- Expanded dropdowns
- Full feature set

**Mobile (< 768px)**
- Hamburger menu (3-line icon)
- Single column layouts
- Collapsible dropdowns
- Touch-friendly buttons
- Optimized forms

---

## 🚢 Deployment Options

### Option 1: Render (Recommended)
1. Push to GitHub
2. Connect to Render
3. Deploy (automatic)
4. Live in 2-5 minutes

### Option 2: Heroku
Same process, different platform

### Option 3: VPS (DigitalOcean, AWS, etc.)
Manual deployment with gunicorn

**See DEPLOYMENT_CHECKLIST.md for detailed steps**

---

## 🎨 Customization

### Change Colors
Edit `static/css/style.css`:
```css
:root {
    --bg-dark: #0a0e27;        /* Background */
    --accent: #00d4ff;         /* Accent (cyan) */
    --text-primary: #e0e0e0;   /* Main text */
}
```

### Add New Substance
In `app.py`, add to `SUBSTANCE_INFO`:
```python
'your_substance': {
    'name': 'Display Name',
    'health_risks': [...],
    'quit_benefits': [...]
}
```

### Modify Plans
Edit relevant functions in `app.py`:
- `generate_substance_plan()`
- `generate_lifestyle_plan()`
- `generate_looks_plan()`

---

## 📊 Statistics

- **Total Lines of Code**: ~5000
- **Flask App**: 400+ lines
- **CSS**: 1000+ lines
- **HTML Templates**: 9 files
- **JavaScript**: 200+ lines
- **Substances Covered**: 6 types
- **Customizable Plans**: 3 categories
- **Responsive Breakpoints**: 3 (768px, 480px)
- **Mobile-Friendly**: 100%

---

## 🆘 Need Help?

### Getting Started
→ Read **QUICKSTART.md**

### Understanding Features
→ Read **PROJECT_SUMMARY.md** or **USER_FLOW.md**

### Deploying
→ Read **DEPLOYMENT_CHECKLIST.md**

### All Documentation
→ Read **README.md**

### Code Structure
→ Check inline comments in `app.py` and `static/css/style.css`

---

## 🎯 Next Steps

### Immediate (Today)
1. ✅ Read QUICKSTART.md
2. ✅ Run `pip install -r requirements.txt`
3. ✅ Run `python app.py`
4. ✅ Test the platform locally
5. ✅ Create test account and explore

### Short Term (This Week)
1. ✅ Customize colors/branding
2. ✅ Add your own content
3. ✅ Push to GitHub
4. ✅ Deploy to Render
5. ✅ Share with friends

### Medium Term (This Month)
1. ✅ Gather user feedback
2. ✅ Fix bugs/issues
3. ✅ Add features
4. ✅ Grow user base
5. ✅ Consider monetization (donations)

### Long Term
1. ✅ Add community features
2. ✅ Build mobile app
3. ✅ Expand partnerships
4. ✅ Scale infrastructure
5. ✅ Impact thousands

---

## 💡 Key Insights

### Why This Works
- **Fills a gap**: No existing platform does this combination well
- **Science-based**: Real information, not fluff
- **User-friendly**: Dark theme, mobile-optimized, simple interface
- **Multi-goal**: Most apps focus on one thing; this handles multiple
- **Non-profit**: Mission-driven, builds trust
- **Free**: No paywall, removes barriers to entry

### What's Different
- NOT another motivational app
- NOT preachy or corny
- NOT one-size-fits-all
- NOT desktop-only
- NOT overwhelming

### Why You Should Use This
- Start helping people TODAY
- Fully functional, not a template
- Deployment-ready (Render in minutes)
- Well-documented
- Easy to customize
- Made with care and thought

---

## 📞 Contact & Support

**For Users**
- Contact form in app
- Email: hello@getbetter.com

**For Developers**
- GitHub: github.com/yourusername/getbetter
- Issues: Report bugs on GitHub
- Documentation: All files in this repo

**Crisis Support**
- SAMHSA: 1-800-662-4357 (free, 24/7)
- Crisis Text: Text HOME to 741741

---

## 📜 License

This project is open source under the MIT License. You're free to use, modify, and distribute it.

---

## 🙏 Thank You

This platform was built to help people. Whether you're using it to quit substances, get fit, or improve your appearance—know that you're making a real difference in people's lives.

**Get Better: Because you deserve to be your best self.**

---

## 🗺️ Where to Go Next

👉 **Start Here**: [QUICKSTART.md](QUICKSTART.md)

Or choose based on what you want to do:

| I Want To... | Read This |
|---|---|
| Get it running locally | QUICKSTART.md |
| Understand what was built | PROJECT_SUMMARY.md |
| See how users interact | USER_FLOW.md |
| Deploy to the web | DEPLOYMENT_CHECKLIST.md |
| Learn all the details | README.md |
| Customize the code | See inline comments in files |

---

**Last Updated**: February 3, 2026  
**Version**: 1.0 (Production Ready)  
**Status**: ✅ Complete and Ready to Deploy
