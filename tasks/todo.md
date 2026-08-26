# Project Tasks

## Current Sprint

- [ ] Simplify the portfolio one approved step at a time.
  - [x] Step 1: Remove lower-left `LUMINE / LT-1997` identity labels sitewide.
  - [x] Step 2: Rename `Selected Work` to `Projects`, move the canonical page to `projects.html`, and keep the old URL compatible.
  - [x] Step 3: Simplify the homepage divider and metadata.
  - [x] Step 4: Simplify the Projects page intro and project stats.
  - [x] Step 5: Simplify the Polara navigation, overview, card layout, and closing CTA.
  - [x] Run final cross-page QA after all five review gates; release only after approval.

- [ ] Implement the approved SEO roadmap one review gate at a time.
  - [x] Step 1: Improve the current Polara page title, description, H1, hero copy, and CTA. Awaiting founder review before Step 2.
  - [x] Step 2: Convert the existing Polara case study into the product page after approval. Awaiting founder review before Step 3.
  - [x] Steps 3–4: Embed Ballerina and Ayesha demos in the product page, then add About, Methodology, authorship, and original supporting material. Awaiting founder review before Step 5.
  - [x] Step 5: Add sitemap, robots, canonical URLs, and structured data after approval.
    - [x] Restore the site version to `0.1.0.2` and keep the approved portfolio cleanup in that release record.
    - [x] Add canonical URLs to every active public page.
    - [x] Add a root sitemap and robots discovery rule.
    - [x] Add visible-fact Polara mobile-application structured data.
    - [x] Complete local validation and receive founder approval for deployment.
  - [ ] Step 6: Define the Search Console and analytics iteration workflow after approval.

- [ ] Publish and verify SEO Step 5 on Vercel.
  - [x] Preserve site version `0.1.0.2` and complete local release QA.
  - [ ] Create and merge the SEO Step 5 pull request.
  - [ ] Wait for the Vercel production deployment.
  - [ ] Verify live sitemap, robots, canonicals, structured data, and responsive rendering.

- [x] Strengthen the Polara App Store CTA and audit the page against the shared SEO guidance.
  - [x] Restyle the hero CTA with a Polara-pink fill and white text.
  - [x] Verify the CTA at desktop and mobile sizes.
  - [x] Record prioritized content recommendations for Google and AI search.

- [x] Reframe the Polara index gallery around product screens.
  - [x] Approve retaining the five branded images with screen-first focal points.
  - [x] Apply frame-specific top and bottom positioning.
  - [x] Stack the card early enough to preserve the crops on tablet and small-laptop widths.
  - [x] Verify every frame at desktop, tablet, and mobile sizes.

- [x] Replace contained Polara artwork with a safe full-bleed crop.
  - [x] Approve top-aligned cover treatment with whole primary headlines.
  - [x] Implement the crop without vertical scrolling.
  - [x] Inspect all five frames at desktop and mobile sizes.

- [x] Make Selected Work App Store screenshots fully readable.
  - [x] Diagnose the crop caused by the landscape media pane and `object-fit: cover`.
  - [x] Approve full-image `contain` treatment with Polara-colored gutters.
  - [x] Implement the responsive image-fit change.
  - [x] Verify desktop and mobile gallery behaviour and legibility.

- [x] Publish the approved portfolio cleanup to luminetong.xyz while retaining site version `0.1.0.2`.
  - [x] Confirm GitHub/Vercel deployment infrastructure and production domain.
  - [x] Run release checks.
  - [x] Create and merge the portfolio cleanup pull request.
  - [x] Wait for the Vercel production deployment.
  - [x] Verify the production homepage, Projects index, and Polara product page.

- [x] Inspect the personal website and Polara product context.
- [x] Define the Selected Work information architecture.
- [x] Approve the compact Polara case-study structure.
- [x] Audit the existing subpage design system and the supplied Polara screenshots.
- [x] Approve a design-system-native Selected Work index preview.
- [x] Approve a design-system-native Polara case-study preview.
- [x] Increase sidebar and explanatory-copy readability.
- [x] Expand the Product rail to all seven current App Store screenshots.
- [x] Add restrained, purposeful motion with reduced-motion support.
- [x] Implement the approved Selected Work index and Polara case study.
- [x] Verify desktop and mobile behaviour.

## Review Notes

- Portfolio cleanup Step 1 removes the lower-left identity labels from the homepage,
  Projects, Writings, and all six research article sidebars while retaining every
  article and index-page Back link. Static search, desktop/mobile overflow checks,
  and representative visual inspection passed; Step 2 remains gated on approval.
- Portfolio cleanup Step 2 changes the homepage act, Projects sidebar, document title,
  metadata, and navigation label from `Selected Work` to `Projects`. The canonical
  page now lives at `projects.html`; `selected-work.html` is a noindex compatibility
  redirect. The real homepage click-through, 1440px and 375px layouts, and page
  overflow checks passed.
- Portfolio cleanup Step 3 removes the entire Trait row and replaces the generated
  `L L L...` divider with a semantic-free 1px horizontal rule. The earlier identity
  cleanup already removed `LT-1997 © 2026`. Desktop/mobile checks confirmed the old
  text is absent, the divider spans the panel, and no horizontal overflow was added.
  A design-html refinement then converts both three-row groups to matching grids:
  desktop row steps are 29px with 14px on either side of the divider; tablet/mobile
  row steps are 27px with 10px on either side. All measured values match exactly.
- Portfolio cleanup Step 4 removes the Projects collection metadata and the `100+`
  trick statistic. The remaining Explore Polara action aligns to the lower-right on
  desktop and stays full-width on mobile. Checks at 1440px and 375px passed with the
  removed copy absent, the CTA visible, and no horizontal overflow.
- Portfolio cleanup Step 5 moves a unified `Back` control to the upper-left, relabels
  the opening section `00 / Overview`, removes the sidebar product descriptor and
  device/privacy metadata, and keeps `Remember → Track → Reflect` on one line. The
  closing download panel is removed. Sections 01 and 02 now share exact card sizes:
  740×470px desktop, 455×700px tablet, and 302×630px mobile. Checks at 1440px,
  768px, and 375px passed without overflow; status-button interaction, Projects
  return navigation, and all horizontally lazy-loaded images were also verified.
- Final release QA covered 11 pages at 1440×900 and 375×812. All pages loaded
  without horizontal overflow, broken images, empty links, or isolated console
  errors. Homepage → Projects → Polara, Writings → article → Writings, the
  legacy Selected Work redirect, Polara status controls, and both horizontal
  rails passed. Health score: 100/100; no QA fixes were required.
- SEO Step 5 adds one canonical URL to each of the 11 active public pages and
  lists the same set in the root sitemap. `robots.txt` points crawlers to that
  sitemap; the legacy Selected Work redirect and draft/orphan pages remain out.
  Polara now exposes `MobileApplication` JSON-LD with its App Store destination,
  free offer, author, screenshot, platform, and only product features supported
  by visible page copy. XML, JSON, canonical/sitemap parity, desktop and mobile
  rendering, broken-image, overflow, and browser-console checks all passed.

- Approved structure: Homepage `Selected Work` entry → Selected Work index → Polara.
- Polara uses one product-first page; representative trick demos and product provenance live inline rather than on separate trick URLs.
- The index does not show early-signal metrics.
- Existing subpages are the visual source of truth: Courier New, Modernline branding,
  dark ticket/card surfaces, 1px dividers, restrained uppercase metadata, and grain.
- Polara contributes official product imagery and a limited berry accent; it does not
  introduce a separate portfolio type system or page shell.
- The Selected Work screenshot rail scrolls horizontally at every responsive size.
- Sidebar navigation is 12px with 44px targets; explanatory copy is 16px with higher contrast.
- The Product rail contains all seven current App Store exports and remains horizontal at every breakpoint.
- Motion is limited to hero entrance, hover response, horizontal scroll snapping, and staggered section reveals; reduced-motion users receive a static page.
- Final verification passed at 1440×900, 768×900, and 375×812 with no page-level horizontal overflow or console errors.
- Pre-landing review converged after removing dead assets, correcting product-state copy,
  optimizing the seven screenshots to a 576 KB WebP set, and adding accessible gallery fallbacks.
- Fresh browser QA passed the homepage → Selected Work → Polara path at desktop and mobile sizes;
  all galleries, lazy-loaded images, keyboard scrolling, counters, links, and console checks passed.
- A full-aspect-ratio contain pass was tested and rejected because it made the index artwork feel
  too small; the compact mobile counter was retained because it does not cover screenshot copy.
- A headline-led top-aligned crop was tested and rejected because the marketing typography still
  dominated the product UI; its fourth-frame mobile safe zoom was retained.
- The approved screen-first crop map bottom-aligns frames 1, 2, and 5 and top-aligns frames 3
  and 4, keeping App UI dominant while removing the large external marketing headlines.
- The project card switches to a stacked gallery at 1280px so narrow landscape media panes
  do not reintroduce App Store marketing copy on tablets and small laptops.
- Final pre-release browser QA passed at 1440, 1281, 1280, 1024, 900, 769, 768, and 375px widths;
  all five images loaded, the counter reached `05`, and no overflow or console errors appeared.
- The App Store CTA now uses a deeper Polara berry-pink action color with white text, a
  5.15:1 contrast ratio, and restrained hover elevation. It passed fresh desktop and mobile
  checks with a 44px target, no page overflow, and no browser warnings or errors.
- The SEO audit keeps the portfolio case study focused on brand/creator intent while recommending
  a separate product-led content surface for high-intent pole-dance queries and the public trick library.
- SEO Step 1 gives the existing case study an explicit `Pole Dance Tracker` H1 descriptor,
  answer-first product copy, search-oriented title and description, and a `Download Polara` CTA.
  Desktop and mobile browser checks passed with no overflow or console warnings/errors; the
  founder approved Step 1 before Step 2 began.
- SEO Step 2 converts the existing Polara URL into a product-first page rather than creating a
  duplicate landing page. Product navigation, persistent download actions, user benefits, and
  privacy messaging replace case-study role, scope, design rationale, and implementation-stack copy.
  The product page and Selected Work entry passed fresh checks at 1440px, 768px, and 375px with
  no page overflow or console warnings/errors; Step 3 remains gated on founder approval.
- SEO Steps 3–4 replace the standalone Butterfly demo with an inline product-page section for
  Ballerina and Ayesha. The searchable library and one detail screen per demo show the product
  without publishing the full library. About, Methodology, author, and original-material notes
  establish provenance without presenting technique instruction.
- Steps 3–4 browser QA passed at 1440×900, 768×900, and 375×812. All three displayed demo images
  load at their optimized 900px width when brought into view. Ballerina and Ayesha now show their
  complete 900×1957 App screenshots inside responsive phone frames, with no `cover` crop; the page
  has no horizontal overflow or console errors.
  To learn, Learning, and Landed accept one selection per demo with hover glow, keyboard focus,
  pink selected state, and synchronized `aria-pressed` values.
- Search & Filter, Ballerina, and Ayesha now share one compact three-card horizontal rail modeled
  on How It Works. Each card uses the same split-copy/full-phone composition; scroll snapping,
  desktop and mobile horizontal scrolling, image loading, and console checks pass. The redundant
  counters, instruction labels, and progress bars were removed from both horizontal sections.
