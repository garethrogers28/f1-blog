# Testing

Return to [README.md](README.md)

---

## Manual Testing

### Authentication

| #   | User Story          | Test                          | Steps                                                                | Expected Result                                           | Actual Result | Pass/Fail |
| --- | ------------------- | ----------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------- | ------------- | --------- |
| 1   | Register an account | Create a new account          | Navigate to Register page → Enter username, email, password → Submit | Account created, user redirected to home page             | As expected   | Pass      |
| 1   | Register an account | Duplicate username rejected   | Try to register with an existing username                            | Error message displayed, account not created              | As expected   | Pass      |
| 1   | Register an account | Password mismatch rejected    | Enter different passwords in password fields                         | Error message displayed                                   | As expected   | Pass      |
| 2   | Log in              | Log in with valid credentials | Navigate to Login → Enter valid username/password → Submit           | User logged in, redirected to home page                   | As expected   | Pass      |
| 2   | Log in              | Invalid credentials rejected  | Enter wrong password                                                 | Error message displayed, login denied                     | As expected   | Pass      |
| 3   | Log out             | Log out successfully          | Click Logout in navbar                                               | User logged out, redirected to home page, session cleared | As expected   | Pass      |
| 3   | Log out             | Session cleared after logout  | Log out then try accessing protected page                            | Redirected to login page                                  | As expected   | Pass      |

### Blog

| #   | User Story           | Test                                 | Steps                                                   | Expected Result                                               | Actual Result | Pass/Fail |
| --- | -------------------- | ------------------------------------ | ------------------------------------------------------- | ------------------------------------------------------------- | ------------- | --------- |
| 4   | View post list       | Posts displayed on home page         | Navigate to home page                                   | List of blog posts visible with titles, excerpts, images      | As expected   | Pass      |
| 4   | View post list       | Pagination works                     | Navigate to home when more than 6 posts exist           | Pagination controls appear and work                           | As expected   | Pass      |
| 5   | View full post       | Open a post                          | Click on a post title/card                              | Full post content displayed with title, author, date, content | As expected   | Pass      |
| 6   | Add a comment        | Submit a comment as logged-in user   | Log in → Open post → Type comment → Submit              | Comment appears below post, success message shown             | As expected   | Pass      |
| 6   | Add a comment        | Comment blocked when logged out      | Visit post detail while logged out                      | Comment form not visible, login prompt shown                  | As expected   | Pass      |
| 7   | Edit comment         | Edit own comment                     | Click Edit on own comment → Modify text → Submit        | Comment updated, success message shown                        | As expected   | Pass      |
| 7   | Edit comment         | Cannot edit another user's comment   | Check if Edit button appears on other users' comments   | Edit button not visible for other users' comments             | As expected   | Pass      |
| 8   | Delete comment       | Delete own comment                   | Click Delete on own comment → Confirm deletion          | Comment removed, success message shown                        | As expected   | Pass      |
| 8   | Delete comment       | Cannot delete another user's comment | Check if Delete button appears on other users' comments | Delete button not visible for other users' comments           | As expected   | Pass      |
| 11  | Like a post          | Like a post as logged-in user        | Log in → Open post → Click Like button                  | Like count increases by 1, button state changes               | As expected   | Pass      |
| 11  | Like a post          | Can only like once                   | Click Like button again on same post                    | Button shows unlike state, cannot add duplicate like          | As expected   | Pass      |
| 12  | Unlike a post        | Remove like from a post              | Click Unlike button on a previously liked post          | Like count decreases by 1, button reverts                     | As expected   | Pass      |
| 13  | Admin upload image   | Upload image via admin panel         | Log into admin → Create/edit post → Upload image        | Image saved to Cloudinary, linked to post                     | As expected   | Pass      |
| 14  | View images on posts | Images display correctly             | Browse posts with uploaded images                       | Featured images render at correct size on all devices         | As expected   | Pass      |
| 14  | View images on posts | Placeholder shown when no image      | View a post without an uploaded image                   | Default placeholder image displayed                           | As expected   | Pass      |

### UX

| #   | User Story        | Test                        | Steps                                       | Expected Result                                            | Actual Result | Pass/Fail |
| --- | ----------------- | --------------------------- | ------------------------------------------- | ---------------------------------------------------------- | ------------- | --------- |
| 9   | Responsive design | Site works on mobile        | Open site on mobile device/DevTools (375px) | Layout adapts, all content readable, no horizontal scroll  | As expected   | Pass      |
| 9   | Responsive design | Site works on tablet        | Open site on tablet/DevTools (768px)        | Layout adapts appropriately                                | As expected   | Pass      |
| 9   | Responsive design | Site works on desktop       | Open site on desktop (1200px+)              | Full layout displayed correctly                            | As expected   | Pass      |
| 10  | Clear navigation  | Navbar visible on all pages | Navigate through all pages                  | Navbar present on every page with correct links            | As expected   | Pass      |
| 10  | Clear navigation  | Active page highlighted     | Navigate to different pages                 | Current page link highlighted in navbar                    | As expected   | Pass      |
| 10  | Clear navigation  | Conditional nav links       | Check navbar when logged in vs logged out   | Logged in: My Garage, Logout · Logged out: Login, Register | As expected   | Pass      |

### Predictions

| #   | User Story           | Test                          | Steps                                                    | Expected Result                                    | Actual Result | Pass/Fail |
| --- | -------------------- | ----------------------------- | -------------------------------------------------------- | -------------------------------------------------- | ------------- | --------- |
| 15  | View upcoming races  | Race list displays            | Navigate to Races page                                   | List of upcoming races with names and dates shown  | As expected   | Pass      |
| 15  | View upcoming races  | Race selection available      | Click on a race as logged-in user                        | Prediction form displayed for that race            | As expected   | Pass      |
| 16  | Submit prediction    | Submit pole + podium picks    | Select pole, P1, P2, P3 drivers → Submit                 | Prediction saved, confirmation message shown       | As expected   | Pass      |
| 16  | Submit prediction    | Duplicate drivers rejected    | Select same driver for multiple positions                | Validation error displayed, form not submitted     | As expected   | Pass      |
| 16  | Submit prediction    | Blocked when logged out       | Visit race detail while logged out                       | Redirect to login page                             | As expected   | Pass      |
| 17  | Edit prediction      | Edit before deadline          | Open existing prediction → Change picks → Submit         | Prediction updated, success message shown          | As expected   | Pass      |
| 17  | Edit prediction      | Blocked after deadline        | Try to edit prediction after race deadline               | Edit not allowed, message displayed                | As expected   | Pass      |
| 18  | Admin scoring        | Admin enters results          | Log into admin → Enter race results                      | Predictions scored automatically, points awarded   | As expected   | Pass      |
| 19  | Personal dashboard   | Access My Garage              | Log in → Click My Garage in navbar                       | Dashboard displays stats, prediction history       | As expected   | Pass      |
| 19  | Personal dashboard   | Blocked when logged out       | Navigate to profile URL when logged out                  | Redirected to login page                           | As expected   | Pass      |
| 20  | Leaderboard          | View rankings                 | Navigate to Leaderboard page                             | Users displayed ranked by total points             | As expected   | Pass      |
| 20  | Leaderboard          | Scores update after results   | Admin enters results for a race                          | Leaderboard positions update accordingly           | As expected   | Pass      |
| 21  | Total points         | Points displayed on dashboard | Log in → Go to My Garage                                 | Total points shown clearly                         | As expected   | Pass      |
| 22  | Leaderboard rank     | Rank shown on dashboard       | Log in → Go to My Garage                                 | Current rank/position displayed                    | As expected   | Pass      |
| 23  | Previous predictions | View prediction history       | Log in → Go to My Garage → View history                  | Past predictions listed with race names and scores | As expected   | Pass      |
| 24  | Submission status    | Status indicator shown        | Log in → Go to My Garage                                 | Upcoming race shows submitted/not submitted status | As expected   | Pass      |
| 25  | Update profile       | Edit profile fields           | Log in → My Garage → Edit Profile → Update fields → Save | Profile updated, success message shown             | As expected   | Pass      |
| 25  | Update profile       | Invalid submission rejected   | Submit profile form with invalid data                    | Validation errors displayed                        | As expected   | Pass      |

---

## Code Validation

### HTML Validation

All pages were validated using the [W3C HTML Validator](https://validator.w3.org/) by direct input (rendering the page source). All pages passed with no errors or warnings.

| Page         | Result | Notes                 |
| ------------ | ------ | --------------------- |
| Home         | Pass   | No errors or warnings |
| Post Detail  | Pass   | No errors or warnings |
| Race List    | Pass   | No errors or warnings |
| Race Detail  | Pass   | No errors or warnings |
| Leaderboard  | Pass   | No errors or warnings |
| My Garage    | Pass   | No errors or warnings |
| Edit Profile | Pass   | No errors or warnings |
| Login        | Pass   | No errors or warnings |
| Register     | Pass   | No errors or warnings |
| 404          | Pass   | No errors or warnings |

<details>
<summary>HTML Validation Screenshots</summary>

![HTML Validation - Home](documents/testing/html-validation-home.png)
![HTML Validation - Post Detail](documents/testing/html-validation-post-detail.png)
![HTML Validation - Profile](documents/testing/html-validation-profile.png)

</details>

### CSS Validation

CSS was validated using the [W3C CSS Validator (Jigsaw)](https://jigsaw.w3.org/css-validator/).

| File      | Result | Notes     |
| --------- | ------ | --------- |
| style.css | Pass   | No errors |

![CSS Validation](documents/testing/css-validation.png)

### JavaScript Validation

JavaScript was validated using [JSHint](https://jshint.com/).

| File      | Result | Notes     |
| --------- | ------ | --------- |
| script.js | Pass   | No errors |

![JavaScript Validation](documents/testing/js-validation.png)

### Python Validation

All Python source files were validated using the [CI Python Linter](https://pep8ci.herokuapp.com/). All files passed with no errors.

| File                                    | Result | Notes     |
| --------------------------------------- | ------ | --------- |
| f1blog/settings.py                      | Pass   | No errors |
| f1blog/urls.py                          | Pass   | No errors |
| blog/admin.py                           | Pass   | No errors |
| blog/forms.py                           | Pass   | No errors |
| blog/models.py                          | Pass   | No errors |
| blog/urls.py                            | Pass   | No errors |
| blog/views.py                           | Pass   | No errors |
| blog/templatetags/cloudinary_filters.py | Pass   | No errors |
| predictions/admin.py                    | Pass   | No errors |
| predictions/forms.py                    | Pass   | No errors |
| predictions/models.py                   | Pass   | No errors |
| predictions/services.py                 | Pass   | No errors |
| predictions/urls.py                     | Pass   | No errors |
| predictions/views.py                    | Pass   | No errors |

<details>
<summary>Python Validation Screenshots</summary>

![Python Validation - settings.py](documents/testing/python-validation-settings.png)
![Python Validation - blog views.py](documents/testing/python-validation-views.png)
![Python Validation - blog models.py](documents/testing/python-validation-models.png)
![Python Validation - blog forms.py](documents/testing/python-validation-forms.png)
![Python Validation - urls.py](documents/testing/python-validation-url.png)
![Python Validation - predictions services.py](documents/testing/python-validation-services.png)
![Python Validation - predictions forms.py](documents/testing/python-validation-prediction-forms.png)
![Python Validation - predictions models.py](documents/testing/python-validation-prediction-models.png)

</details>

---

## Accessibility Testing

### Colour Contrast

All colour combinations were tested using [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) to ensure WCAG AA compliance.

| Foreground           | Background                 | Ratio  | Result     |
| -------------------- | -------------------------- | ------ | ---------- |
| White (#ffffff)      | Red buttons (#e10600)      | 4.53:1 | Pass (AA)  |
| Red text (#e10600)   | White background (#ffffff) | 4.53:1 | Pass (AA)  |
| White (#ffffff)      | Dark navbar (#1a1a1a)      | 17.4:1 | Pass (AAA) |
| Black text (#1a1a1a) | Light grey (#f5f5f5)       | 16.6:1 | Pass (AAA) |
| Username badge       | Dark background            | 7:1+   | Pass (AAA) |
| Blog post cards      | Light background           | 7:1+   | Pass (AAA) |

<details>
<summary>Contrast Test Screenshots</summary>

![Footer Contrast](documents/testing/footer-contrast.png)
![Navbar Links Contrast](documents/testing/navbar-links-navbar-background-contrast.png)
![Main Content H1 Contrast](documents/testing/main-content-h1tags-contrast.png)
![Red Text White Background](documents/testing/red-text-white-background-contrast.png)
![White Text Red Buttons](documents/testing/white-text-red-buttons-contrast.png)
![Username Badge Contrast](documents/testing/username-badge-contrast.png)
![Blog Post Cards Contrast](documents/testing/blog-post-cards-contrast.png)

</details>

### Additional Accessibility Features

- Semantic HTML structure (`<header>`, `<main>`, `<footer>`)
- `aria-current="page"` on active navigation links
- `scope="col"` on all table headers
- `aria-label` on toggle buttons and close buttons
- `alt` text on all images

---

## Lighthouse Testing

All pages were tested using Google Chrome Lighthouse in both desktop and mobile modes.

| Page        | Device  | Performance | Accessibility | Best Practices | SEO |
| ----------- | ------- | ----------- | ------------- | -------------- | --- |
| Home        | Desktop | 98          | 100           | 100            | 100 |
| Home        | Mobile  | 92          | 100           | 100            | 100 |
| Post Detail | Desktop | 98          | 100           | 100            | 100 |
| Post Detail | Mobile  | 88          | 100           | 100            | 100 |
| Race List   | Desktop | 99          | 100           | 100            | 100 |
| Race List   | Mobile  | 92          | 100           | 100            | 100 |
| Race Detail | Desktop | 97          | 100           | 100            | 100 |
| Race Detail | Mobile  | 89          | 100           | 100            | 100 |
| Leaderboard | Desktop | 98          | 100           | 100            | 100 |
| Leaderboard | Mobile  | 91          | 100           | 100            | 100 |
| Profile     | Desktop | 98          | 100           | 100            | 100 |
| Profile     | Mobile  | 90          | 100           | 100            | 100 |

<details>
<summary>Lighthouse Screenshots — Desktop</summary>

![Lighthouse Desktop - Home](documents/testing/lighthouse-desktop-home.png)
![Lighthouse Desktop - Post Detail](documents/testing/lighthouse-desktop-post-detail.png)
![Lighthouse Desktop - Race List](documents/testing/lighthouse-desktop-race-list.png)
![Lighthouse Desktop - Race Detail](documents/testing/lighthouse-desktop-race-detail.png)
![Lighthouse Desktop - Leaderboard](documents/testing/lighthouse-desktop-leaderboard.png)
![Lighthouse Desktop - Profile](documents/testing/lighthouse-desktop-profile.png)

</details>

<details>
<summary>Lighthouse Screenshots — Mobile</summary>

![Lighthouse Mobile - Home](documents/testing/lighthouse-mobile-home.png)
![Lighthouse Mobile - Post Detail](documents/testing/lighthouse-mobile-post-detail.png)
![Lighthouse Mobile - Race List](documents/testing/lighthouse-mobile-race-list.png)
![Lighthouse Mobile - Race Detail](documents/testing/lighthouse-mobile-race-detail.png)
![Lighthouse Mobile - Leaderboard](documents/testing/lighthouse-mobile-leaderboard.png)
![Lighthouse Mobile - Profile](documents/testing/lighthouse-mobile-profile.png)

</details>

---

## Browser Testing

The site was tested on the following browsers with no issues:

| Browser | Version | Result                    |
| ------- | ------- | ------------------------- |
| Chrome  | Latest  | Pass All features working |
| Firefox | Latest  | Pass All features working |
| Safari  | Latest  | Pass All features working |
| Edge    | Latest  | Pass All features working |

---

## Responsiveness Testing

The site was tested at the following breakpoints using Chrome DevTools:

| Device / Width    | Result | Notes                                        |
| ----------------- | ------ | -------------------------------------------- |
| iPhone SE (375px) | Pass   | Navbar collapses, cards stack, tables scroll |
| iPhone 12 (390px) | Pass   | All content readable, no overflow            |
| iPad (768px)      | Pass   | 2-column card layout, tables display fully   |
| iPad Pro (1024px) | Pass   | Content well-spaced                          |
| Desktop (1440px)  | Pass   | Full layout, max-width container centred     |

---

## Bugs

### Fixed Bugs

| #   | Bug                                                     | Cause                                                                                               | Fix                                                                                                                      |
| --- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 1   | Bootstrap CSS not loading — site had no styling         | Bootstrap CDN link was broken/incorrect                                                             | Replaced with correct Bootstrap 5.3.3 CDN link with integrity hash                                                       |
| 2   | SECRET_KEY exposed on GitHub                            | Sensitive environment variables were exposed due to incorrect configuration of environment handling | Removed hardcoded key, added env.py to .gitignore, regenerated SECRET_KEY, set production to raise ValueError if missing |
| 3   | Prettier breaking Django template tags                  | Prettier reformatted `{% if %}` blocks across multiple lines, breaking template logic               | Disabled Prettier for HTML files in VS Code settings                                                                     |
| 4   | Duplicate `rel` attribute on preconnect link            | Had `rel="preconnect"` and `rel="stylesheet"` on same element                                       | Separated into two proper `<link>` elements                                                                              |
| 5   | Low contrast on Like button for non-authenticated users | Default Bootstrap outline styling didn't meet WCAG contrast ratio                                   | Changed to `btn-outline-dark` with `link-dark fw-bold` on login link                                                     |
| 6   | `{% endblock %}` split across lines in profile.html     | Prettier reformatted the tag before being disabled                                                  | Manually fixed and saved without formatting                                                                              |

### Unfixed Bugs

At the time of submission, there are no known major unfixed bugs affecting core functionality.

---

Return to [README.md](README.md)
