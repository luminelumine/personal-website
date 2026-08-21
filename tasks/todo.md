# Project Tasks

## Current Sprint

- [x] Reframe the Polara index gallery around product screens.
  - [x] Approve retaining the five branded images with screen-first focal points.
  - [x] Apply frame-specific top and bottom positioning.
  - [x] Verify every frame at desktop and mobile sizes.

- [x] Replace contained Polara artwork with a safe full-bleed crop.
  - [x] Approve top-aligned cover treatment with whole primary headlines.
  - [x] Implement the crop without vertical scrolling.
  - [x] Inspect all five frames at desktop and mobile sizes.

- [x] Make Selected Work App Store screenshots fully readable.
  - [x] Diagnose the crop caused by the landscape media pane and `object-fit: cover`.
  - [x] Approve full-image `contain` treatment with Polara-colored gutters.
  - [x] Implement the responsive image-fit change.
  - [x] Verify desktop and mobile gallery behaviour and legibility.

- [ ] Publish the approved Polara portfolio work to luminetong.xyz.
  - [x] Confirm GitHub/Vercel deployment infrastructure and production domain.
  - [x] Run release checks.
  - [x] Create pull request #1.
  - [ ] Merge to main and wait for the Vercel production deployment.
  - [ ] Verify the production homepage, Selected Work index, and Polara gallery.

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

- Approved structure: Homepage `Selected Work` entry → Selected Work index → Polara.
- Polara case study is limited to Hero, Product, and Thinking.
- The index does not show early-signal metrics.
- Existing subpages are the visual source of truth: Courier New, Modernline branding,
  dark ticket/card surfaces, 1px dividers, restrained uppercase metadata, and grain.
- Polara contributes official product imagery and a limited berry accent; it does not
  introduce a separate portfolio type system or page shell.
- The Selected Work screenshot rail scrolls horizontally at every responsive size.
- Sidebar navigation is 12px with 44px targets; explanatory copy is 16px with higher contrast.
- The Product rail contains all seven current App Store exports and remains horizontal at every breakpoint.
- Motion is limited to hero entrance, gallery progress feedback, hover response, and staggered Thinking reveals; reduced-motion users receive a static page.
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
