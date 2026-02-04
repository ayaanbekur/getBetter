# Get Better - Quick Start Guide

## Local Development

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

### 3. Open in Browser
```
http://localhost:5000
```

### 4. Test the Application
- **Home Page**: See the landing page and features
- **Sign Up**: Create a test account
- **Onboarding**: Select multiple goals (try substances + lifestyle)
- **Dashboard**: View your personalized plans
- **Plan Details**: Click into each plan to see in-depth information
- **Mobile**: Resize browser to <768px to see mobile hamburger menu

## File Organization

```
NonProfit/
├── app.py                          # Main Flask application with all routes
├── config.py                       # Configuration classes
├── requirements.txt                # Python packages needed
├── Procfile                        # For Render deployment
├── README.md                       # Full documentation
├── QUICKSTART.md                   # This file
├── .gitignore                      # Git ignore rules
├── static/
│   ├── css/
│   │   └── style.css              # Dark theme + responsive CSS
│   └── js/
│       └── main.js                # Interactive features
└── templates/
    ├── base.html                  # Navigation + footer
    ├── home.html                  # Landing page
    ├── signup.html                # Registration
    ├── login.html                 # Login
    ├── onboarding.html            # Goal selection overlay
    ├── dashboard.html             # User plans (with dropdowns)
    ├── plan_detail.html           # Detailed plan information
    ├── about.html                 # About page
    └── contact.html               # Contact form
```

## Key Features Implemented

### ✅ Multi-Goal Support
- Users can select multiple goals simultaneously
- Substances: vaping, nicotine, alcohol, tobacco, weed, drugs
- Lifestyle: fitness, weight loss, muscle building
- Looks: skincare, fashion, grooming

### ✅ Personalized Plans
- Based on user frequency, stats, and goals
- Different strategies for each category
- Week-by-week actionable steps

### ✅ Dark Theme
- Cyberpunk-style dark interface (#0a0e27 background)
- Cyan accent color (#00d4ff)
- Custom scrollbar styling
- Proper contrast ratios

### ✅ Mobile Responsive
- Hamburger menu on screens < 768px
- Collapsible plan dropdowns save space
- Touch-friendly buttons
- Responsive grid layouts

### ✅ Dropdown Menus on Plans
- Plans don't take up full space when collapsed
- Click to expand/collapse details
- Smooth animations

### ✅ Database & Auth
- User account system
- Encrypted password storage
- Session management
- SQLite for development (can use PostgreSQL for production)

### ✅ Non-Corny Content
- Explains WHY substances are harmful (not just "quit now!")
- Real health risks and consequences
- Science-backed recommendations
- Practical, actionable strategies

## Customization

### Change Accent Color
In `static/css/style.css`, modify:
```css
:root {
    --accent: #00d4ff;        /* Change this */
    --accent-hover: #00f0ff;  /* And this */
}
```

### Add New Substance
In `app.py`, add to `SUBSTANCE_INFO` dictionary:
```python
'your_substance': {
    'name': 'Display Name',
    'health_risks': [
        'Risk 1',
        'Risk 2',
    ],
    'quit_benefits': [
        'Benefit 1',
        'Benefit 2',
    ]
}
```

### Modify Onboarding Questions
Edit `templates/onboarding.html` to add/remove buttons and forms.

## Deployment to Render

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Get Better platform"
   git push origin main
   ```

2. **Create Render Account**
   - Go to https://render.com
   - Sign up (free tier available)

3. **Connect Repository**
   - New Web Service
   - Connect GitHub repository
   - Select this repository
   - Choose environment: Python
   - Build command: `pip install -r requirements.txt`
   - Start command: Leave default (reads Procfile)

4. **Environment Variables** (if needed)
   - `SECRET_KEY`: Set a strong secret key
   - `DATABASE_URL`: Optional, uses SQLite by default

5. **Deploy**
   - Click Deploy
   - Takes 2-5 minutes
   - Your app will be live at: `your-app.onrender.com`

## Database

### Development (SQLite)
Automatically created when you run the app. Data stored in `getbetter.db`

### Production (PostgreSQL)
1. Create PostgreSQL database on Render or another provider
2. Set `DATABASE_URL` environment variable
3. App automatically migrates

## Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Port already in use
```bash
python app.py --port 5001
```

### Database issues
Delete `getbetter.db` and restart:
```bash
rm getbetter.db
python app.py
```

### CSS not loading
- Make sure you're in the correct directory
- Check that `static/css/style.css` exists
- Refresh browser cache (Ctrl+Shift+Delete)

## Testing the Platform

### Test Workflow
1. Go to home page
2. Click "Start Your Journey"
3. Create account with test@example.com / password123
4. Select multiple goals (e.g., "Vaping" + "Lifestyle")
5. Enter frequency and personal stats
6. View dashboard with collapsible plans
7. Click plan to see full details

### Mobile Testing
1. Open DevTools (F12)
2. Click device toggle (mobile icon)
3. Hamburger menu should appear
4. Test plan dropdowns on mobile

## Support & Resources

- **Crisis Line**: 1-800-662-4357 (SAMHSA)
- **GitHub Issues**: Report bugs
- **Contact Form**: Users can reach you

## Next Steps

1. ✅ Test locally
2. ✅ Push to GitHub
3. ✅ Deploy to Render
4. ✅ Share with community
5. Consider: Community features, email notifications, mobile app

---

**Your "Get Better" platform is ready to help people transform their lives!**
