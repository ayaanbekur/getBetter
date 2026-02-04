# Android Submission Guide - TWA Method (Get Better App)

## Current Status ✅
Your Flask app has been updated with full PWA and TWA support. Here's what was done:

### Changes Made:
1. ✅ Added Flask routes to serve manifest.json and sw.js with correct headers
2. ✅ Added `/.well-known/assetlinks.json` route (critical for TWA!)
3. ✅ Created `.well-known` folder in static directory
4. ✅ Created placeholder assetlinks.json file (will be replaced)
5. ✅ Updated base.html to reference PWA manifests correctly
6. ✅ Added meta tags for web app capability

---

## Step 1: Deploy to Render (or Similar Service)

### Prerequisites:
- [ ] Create a Render account (free tier available)
- [ ] Ensure your app.py is pushed to GitHub
- [ ] Verify requirements.txt is up to date

### Deploy Steps:
1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: get-better (or your preferred name)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Region**: Choose closest to you
5. Click Deploy
6. Wait for deployment (2-3 minutes)
7. Your live URL will be: `https://get-better.onrender.com` (or similar)

**Note**: Keep this URL handy - you'll need it for PWABuilder!

---

## Step 2: Verify PWA Status on Live Site

Before proceeding to Android, verify your PWA works correctly:

1. **Deploy Latest Code**: Push your app.py changes to GitHub and redeploy to Render
2. **Open Live Site**: Visit your deployed URL (e.g., `https://get-better.onrender.com`)
3. **Check Manifest** (F12 → Application tab):
   - Go to Manifest
   - Verify no errors appear
   - Check that icons load correctly
   - Should see: name, short_name, icons, theme_color, etc.
4. **Check Service Worker** (F12 → Application tab):
   - Go to Service Workers
   - Verify Status says "Activated and is running"
   - Should show green circle indicator

**If Issues:**
- Clear cache: DevTools → Application → Clear storage → Unregister service worker
- Hard refresh: Ctrl+Shift+R
- Check browser console for errors

---

## Step 3: Test the .well-known Endpoint

This is critical! Your TWA won't work without this:

1. Visit: `https://your-domain.onrender.com/.well-known/assetlinks.json` in a browser
2. You should see the JSON content (will be updated later)
3. **Status Code**: Should be 200 OK

If you get 404, the Flask route isn't working. Check:
- Restart your Render deployment
- Verify the route exists in app.py
- Check the file exists at `static/.well-known/assetlinks.json`

---

## Step 4: Generate Android App with PWABuilder

This is where the actual Android app gets created!

### Steps:
1. **Go to** [PWABuilder.com](https://www.pwabuilder.com)
2. **Enter URL**: Paste your live site URL (e.g., `https://get-better.onrender.com`)
3. **Click "Start"**: PWABuilder will analyze your site
4. **Review Score**: Should be decent (70+). If low:
   - Check manifest section - fix any errors
   - Ensure icons are valid
   - Verify service worker is active
5. **Click "Build My PWA"**
6. **Select "Android"** platform
7. **Fill in Android Options**:
   ```
   Package ID: com.yourname.getbetter
   (Examples: com.kasim.getbetter, com.mycompany.getbetter)
   
   App Name: Get Better
   
   Launcher Icon: Upload GetBetter.jpg (or use existing)
   
   Maskable Icon: Upload same icon again (or leave default)
   
   Signing Key: Select "Mine, generate a new one"
   ```
8. **Click "Generate"**
9. **Download ZIP File** - Contains:
   - `app-release.aab` - Upload this to Google Play
   - `app-debug.apk` - Test on your phone first
   - `assetlinks.json` - Critical! See Step 5 below
   - signing key (keep this safe!)

---

## Step 5: Update assetlinks.json (Critical Step)

This proves you own the website!

### Steps:
1. **Extract** the `assetlinks.json` from PWABuilder's ZIP
2. **Replace** the placeholder file at: `static/.well-known/assetlinks.json`
3. **Push to GitHub** and **redeploy to Render**
4. **Verify** it works: Visit `https://your-domain.onrender.com/.well-known/assetlinks.json`
5. You should see JSON with your package fingerprint, not the placeholder

**Why This Matters**: Without this file, your TWA will show the browser address bar. With it verified, the app runs in full screen!

---

## Step 6: Test APK on Phone (Optional but Recommended)

Before submitting to Google Play, test the debug APK:

1. **Download** `app-debug.apk` from PWABuilder
2. **Transfer to Android phone** (email, cloud storage, USB)
3. **Install**: 
   - Enable "Unknown sources" in phone settings
   - Tap the APK file
   - Follow installation prompts
4. **Test**: Open the app and verify it works like your website
5. **Check Full Screen**: Address bar should be hidden (if assetlinks.json is correct)

---

## Step 7: Submit to Google Play

### Prerequisites:
- [ ] Google Play Developer Account ($25 one-time fee)
- [ ] `app-release.aab` from PWABuilder
- [ ] Screenshots (3-5, showing app features)
- [ ] Description of your app
- [ ] Icon (at least 512x512 PNG)

### Steps:
1. **Go to** [Google Play Console](https://play.google.com/console)
2. **Create New Application**:
   - Click "Create app"
   - Enter app name: "Get Better"
   - Select category (Health & Fitness or Tools)
3. **Complete Store Listing**:
   - Short description (80 chars)
   - Full description (4000 chars)
   - Upload screenshots (minimum 3)
   - Upload app icon (512x512 minimum)
4. **Content Rating**:
   - Fill out questionnaire (your app will likely get "Everyone" or "12+")
5. **Production Release**:
   - Go to "Release" section
   - Click "Create new release"
   - Select "Production"
   - Upload `app-release.aab`
6. **Review and Rollout**:
   - Review all details
   - Set rollout percentage (start with 5%, then 100%)
7. **Submit**: Click "Send to review"

**Review Time**: Typically 2-3 hours, sometimes overnight

---

## Important Notes

### Keeping Your Signing Key Safe
PWABuilder generated a signing key (usually named something like `get-better.keystore`). 
- **Keep it backed up** - You need it to update the app later
- **Don't share it** - This is like your app's password
- Store it in a secure location (cloud backup, external drive)
- If you lose it, you can't update the app without creating a new app ID

### Updating the App
When you make changes to your Flask code:
1. Update code and test locally
2. Push to GitHub
3. Redeploy on Render
4. **No Android changes needed!** The TWA pulls from your live website

### Version Updates
- Update `version` in manifest.json for website changes
- To submit new Android app version to Google Play:
  - Just re-upload app-release.aab with incremented version number
  - Same signing key used automatically
  - No new signing key needed

---

## Troubleshooting

### App shows browser address bar
- ✅ Verify `assetlinks.json` is accessible at `/.well-known/assetlinks.json`
- ✅ Check it has the correct package ID and fingerprint
- ✅ Redeploy after changes
- ✅ Wait 24-48 hours (Google caches this file)

### Service worker not activating
- ✅ Check browser DevTools Application tab
- ✅ Verify SW registration URL is `/sw.js` (not `static/sw.js`)
- ✅ Check console for JavaScript errors
- ✅ Try clearing cache and hard refresh

### Manifest not loading
- ✅ Check manifest link in base.html points to `/manifest.json`
- ✅ Open DevTools → Network tab, search for manifest.json
- ✅ Verify it returns 200 status, not 404

### PWABuilder reports low score
- ✅ Upload high-quality icons (192x192 and 512x512 minimum)
- ✅ Ensure manifest.json is valid JSON
- ✅ Add more screenshots
- ✅ Improve service worker caching strategy

---

## Deployment Checklist

- [ ] Code pushed to GitHub with TWA updates
- [ ] Deployed to Render with HTTPS enabled
- [ ] Manifest.json accessible at `/manifest.json`
- [ ] Service Worker accessible at `/sw.js`
- [ ] `.well-known/assetlinks.json` accessible (placeholder is fine for now)
- [ ] PWABuilder PWA score is 70+
- [ ] Generated Android app with PWABuilder
- [ ] Updated assetlinks.json with PWABuilder version
- [ ] Tested APK on phone (optional but recommended)
- [ ] Google Play Developer Account created
- [ ] Screenshots and descriptions ready
- [ ] Submitted app-release.aab to Google Play
- [ ] App approved and live on Play Store!

---

## Next Steps

1. **Immediate**: Deploy to Render
2. **This week**: Generate Android app with PWABuilder
3. **Before submission**: Update assetlinks.json and test
4. **Final**: Submit to Google Play Console

Questions? Check the PWABuilder documentation at https://docs.pwabuilder.com/
