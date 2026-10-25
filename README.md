# VedAan Tech Labs — hosting-ready website

## Launch locally
Run `python -m http.server 8000 --directory public` from this folder and open http://localhost:8000. You can also open public/index.html directly for a quick preview.

## Upload to hosting
Upload the **contents of public/** to the website document root. Keep assets/ next to index.html. No build step, Node server, database, API key, or dependency installation is required. This works with ordinary static hosting, cPanel, or Nginx/Apache. For a host asking for an output directory, use public. The included netlify.toml declares this directory for Netlify; _headers is used only by compatible hosts.

Point your domain to your chosen host using its DNS instructions and enable HTTPS there. No domain has been configured or deployment performed by this package. Add a canonical URL, og:url and sitemap.xml once your final domain is known; no placeholder domain is included.

## Interactions
Responsive navigation, service detail dialogs, service selection in the inquiry form, section navigation highlighting, back-to-top, clickable contact icons, and native form validation. Mobile menu supports Escape and outside click. Reduced-motion preferences are respected.

## Contact form
This is a static site with client-side interactions. The form opens the visitor's email application with a prepared message to info@vatechlabs.com. It does NOT send, store, or deliver messages itself. Direct email, telephone, WhatsApp and Google Maps links also work. Automatic submission requires a separately configured form service or backend; do not put SMTP passwords or API secrets in the JavaScript.

## Edit
- public/index.html: layout, contact information, images, and metadata.
- public/assets/styles.css: theme and responsive layout.
- public/assets/app.js: service descriptions and client-side interactions.
- public/assets/image-*: supplied logo and approved hero artwork.

Business details: VedAan Tech Labs Private Limited; info@vatechlabs.com; +91 8801321326; WeWork Rajapushpa Summit, SY. 130P & 115/1P, Nanakramguda Rd, Financial District, Manikonda Jagir, Hyderabad, India.

## Validation
JavaScript syntax, HTML structure, local asset paths, internal navigation targets, contact destinations and ZIP integrity are checked during packaging. Visual browser/device QA remains to be completed before public launch because browser preview was unavailable in this session. Check the mobile menu, service dialogs and email draft on your own devices before launch.


## Validation and fixes update
Name: 2–80 characters, international letters and common name punctuation. Email: valid address format, maximum 254 characters. Company is optional; if supplied, 2–100 characters. Service must be selected from the allowlist. Project description: 20–2,000 characters after trimming. Errors appear beside fields, invalid fields are announced to assistive technology, and submit focuses the first invalid field. The email check validates syntax, not mailbox existence. Client-side validation is not a security boundary; any future backend must validate independently and apply abuse controls.

Long email links are blocked before launching and the visitor can download the inquiry as text instead. No inquiry is stored or sent by this site. Service summaries and complete details are in HTML, with native expandable details that work without JavaScript. The no-JavaScript form has an explicit direct-email fallback. Mobile navigation state resets across breakpoints; an open service dialog locks background scrolling.

Run `npm test` (or `node --test tests/*.test.cjs`) for the validation tests. No npm installation is needed. JavaScript syntax, HTML nesting, IDs, asset references, service content and structured-data JSON were checked. Browser/mobile visual and interaction QA is still outstanding.

## SEO preparation
Unique title and description, Open Graph metadata, one H1, semantic headings, direct HTML service content, original alt text, image dimensions, and Organization structured data are included. This creates a foundation, not a ranking guarantee. Google references: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics and https://developers.google.com/search/docs/crawling-indexing/links-crawlable

Once the actual domain is selected, run `python scripts/configure_domain.py https://YOUR-ACTUAL-DOMAIN` BEFORE uploading public/. Replace the example with your real domain. This adds canonical/sharing URLs, sitemap.xml, the robots sitemap declaration, and the organization's URL/logo. Re-running replaces those settings. Then verify the domain in Search Console and submit the sitemap. There is only one indexable page today; future dedicated service pages should receive their own unique content, titles, canonical URLs and sitemap entries. On your host, configure missing URLs to return an actual HTTP 404 (not a 200 fallback) and redirect HTTP/alternate domain variants to your chosen HTTPS domain. Keep private previews access-controlled until launch.
